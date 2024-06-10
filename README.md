# Introduction
Piebot is an intelligent chatbot designed to assist users in selecting and enrolling in various courses. Utilizing Dialogflow for natural language processing and a Flask web application for backend operations, Piebot efficiently collects user details and preferences, storing them in a MySQL database. The chatbot can also offer personalized recommendations based on user interactions.

# Objectives
The primary objectives of Piebot are:

To provide a seamless course selection and enrollment process.
To collect and store user details such as name, email, phone number, and selected course.
To offer personalized course recommendations based on user preferences.
# System Architecture
Piebot consists of the following key components:

Dialogflow: For understanding and processing user inputs.
Flask Web Application: For handling backend operations.
MySQL Database: For storing user details.
# How Piebot Works
## Interaction Flow
User Inquiry: The user initiates a conversation with Piebot, expressing interest in enrolling in a course.
Course Selection: Piebot presents a list of available courses using buttons for easy selection.
User Details Collection: Upon selecting a course, the user is prompted to provide their name, email, and phone number.
Data Storage: The collected details are stored in a MySQL database.
Confirmation Message: Piebot confirms the successful enrollment of the user.
## Detailed Process
Course Selection Intent:
The want.course intent in Dialogflow is triggered by user phrases indicating interest in courses.
Piebot responds with buttons for each course using a custom payload.
User Details Intent:

The course_selection intent is triggered when the user selects a course.
Piebot collects the user's name, email, and phone number and stores these details in the MySQL database.
# Code Explanation
## Flask Application Code
python
Copy code
from flask import Flask, request, jsonify
import mysql.connector
