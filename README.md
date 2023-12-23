# Post-It Notes Web App

#### Video Demo: https://youtu.be/goXLDeRpzX4

#### Description:

## Overview

This full-stack web application allows users to create a personal account and manage their "post-it" notes from any internet-connected browser. It serves as a practical exercise for building a comprehensive web application.

### User Authentication

- **User Registration**: Users can create a new account by providing a valid email address, first name, last name, and a secure password.
- **User Login**: Registered users can log in securely with their email and password.

- **User Logout**: Users can log out of their accounts, ensuring the security of their sessions.

### Note Management

- **Create Notes**: Users can create new digital notes with a title and description. These notes are stored securely in the database.

- **View Notes**: Users can view all their notes on the dashboard, organized by categories.

- **Update Notes**: Users can edit the content of their existing notes.

- **Delete Notes**: Unwanted notes can be easily deleted.

### Categorization

- **Categorize Notes**: Each note can be categorized into different types such as Business, Social, or Important. Users can assign or update the category of each note.

- **Category Color-coding**: The UI visually represents the categories with distinct colors, providing a quick overview.

### Responsive UI

- **Responsive Design**: The web application is designed to be responsive, ensuring a consistent and user-friendly experience across various devices and screen sizes.

### Flash Messages

- **Flash Messages**: Users receive informative flash messages for successful actions (e.g., creating a note) or error notifications (e.g., invalid input).

### Modal for Adding Notes

- **Add Notes Modal**: A modal is provided for users to conveniently add new notes. It includes fields for the note title and description.

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
