Email Validation System
This is a simple, yet elegant, web-based email validation system built with Flask and a custom Python validator. It allows users to check if an email address is valid and saves all valid emails to a text file.

Features
Frontend Interface: A clean and modern user interface built with HTML, CSS, and vanilla JavaScript.

Backend Logic: A Python backend using the Flask web framework to handle validation requests.

Custom Validator: A robust, custom-built email validation function to ensure accuracy.

Data Persistence: All successfully validated emails are automatically saved to emails.txt.

Automatic Launch: The web application automatically opens in your default browser upon execution.

Project Structure
This project is organized into three main files:

app.py or main.py: The core Flask application that handles routing and integrates the frontend with the backend validation logic.

index.html: The user-facing web page with a form to input an email address.

validator.py: A separate Python module containing the validate_email function. (You'll need to create this file based on your validation logic).

How to Run
Follow these steps to get the project running on your local machine:

Clone the repository:

git clone <your-repository-url>
cd <your-repository-name>
Install dependencies: This project requires Flask. It's recommended to use a virtual environment.

pip install Flask
Run the application: Execute the main Python file.
python app.py
or
python main.py
This will start the server and automatically open the application in your default web browser at http://127.0.0.1:5000.

Technologies Used
Python: The main programming language for the backend.

Flask: A micro web framework for Python.

HTML/CSS/JavaScript: Used to build the frontend user interface.

Git: For version control.

How it Works
The frontend index.html sends a POST request with the email to the /validate endpoint on the Flask server. The server then uses the validate_email function from validator.py to check the email's validity. A JSON response is returned to the frontend, which dynamically updates the page to show whether the email is valid or not. If the email is valid, it is also appended to the emails.txt file.
