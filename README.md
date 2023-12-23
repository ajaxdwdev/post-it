# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
# Post-It Notes Web App

## Overview

This full-stack web application allows users to create a personal account and manage their "post-it" notes from any internet-connected browser. It serves as a practical exercise for building a comprehensive web application.

## Features

- **User Authentication:** Users can create accounts, log in, and securely access their personalized notes.

- **Create and Manage Notes:** Users can create, edit, and delete post-it notes with customizable titles and content.

- **Categorize Notes:** Each note can be categorized as Business, Social, or Important, providing organization and quick identification.

- **Responsive Design:** The application is designed to work seamlessly across various devices and screen sizes.

## Technologies Used

- **Frontend:**
  - HTML, CSS, JavaScript
  - Bootstrap for responsive styling
  - jQuery for dynamic frontend interactions

- **Backend:**
  - Python with Flask framework
  - SQLAlchemy for database interactions
  - Flask-Login for user authentication

- **Database:**
  - SQLite for development
  - Consider using a more robust database (e.g., PostgreSQL) for production.

## Project Structure

- **`templates/`:** HTML templates for different views.
- **`static/`:** Static files such as stylesheets and JavaScript.
- **`models.py`:** Defines the database models (User, Note).
- **`views.py`:** Contains Flask routes and views.
- **`index.js`:** JavaScript code for frontend interactions.

## Setup and Installation

1. Clone the repository: `git clone https://github.com/ajaxdwdev/post-it.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up a virtual environment (optional but recommended).
4. Run the application: `python app.py`

## Usage

1. Open the application in a web browser.
2. Register for a new account or log in if you already have one.
3. Create, edit, or delete your post-it notes.
4. Categorize notes for better organization.
5. Log out to securely end your session.

## Contribution

Contributions are welcome! If you find a bug or have a feature request, please create an issue or submit a pull request.
