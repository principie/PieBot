from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'user': 'root',
    'password': 'Principie!@123',
    'host': 'localhost',
    'database': 'users'
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    print("Received JSON data:", data)  # Log the entire incoming JSON

    intent_name = data['queryResult']['intent']['displayName']

    print(f"Received intent: {intent_name}")

    if intent_name == 'course_selection':
        try:
            course_name = data['queryResult']['parameters']['course_name'][
                0]  # Assuming it's a list, get the first element
            name = data['queryResult']['parameters']['cust_name']
            email = data['queryResult']['parameters']['cust_mail']
            phone_number = data['queryResult']['parameters']['cust_contact']

            print(f"Course Name: {course_name}, Name: {name}, Email: {email}, Phone Number: {phone_number}")

            success = store_user_details(course_name, name, email, phone_number)
            if success:
                response = {
                    'fulfillmentText': f"User {name} with email {email} and phone {phone_number} enrolled in {course_name} added successfully."
                }
            else:
                response = {
                    'fulfillmentText': "Failed to add user. Please try again later."
                }
        except KeyError as e:
            print(f"KeyError: {e}")  # Log the missing key
            response = {
                'fulfillmentText': f"Missing parameter: {e}. Please ensure all required information is provided."
            }
        return jsonify(response)

    else:
        response = {
            'fulfillmentText': "No matching intent handler found."
        }
        return jsonify(response)


def store_user_details(course_name, name, email, phone_number):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO user_details (course_name, name, email, phone_number) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (course_name, name, email, phone_number))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


if __name__ == "__main__":
    app.run(debug=True)
