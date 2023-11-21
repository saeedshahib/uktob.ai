# uktob.ai
Notes Project

# Project Name: Note-Taking Application

## Overview
This project is a note-taking application developed with Django. It allows users to perform CRUD operations on notes and includes JWT authentication for secure access.

## Features
- User registration and login
- CRUD operations for notes
- JWT Authentication
- (Optional) LangChain integration for note summarization

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x
- Pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/saeedshahib/uktob.ai.git
   cd uktob
2. **Set Up a Virtual Environment (Optional)**
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\\Scripts\\activate`
3. **Install Dependencies**
     ```bash
     pip install -r requirements.txt
4. **Database Migrations**
     ```bash
     python manage.py makemigrations
     python manage.py migrate

## Running the application

1. **Start the Django Server**
     ```bash
     python manage.py runserver
2. **Access the Application**
   The application will be available at http://localhost:8000/.

## Testing

1. For automated tests, run:
   ```bash
   python manage.py test

## API Endpoints

+/api/register/: User registration
+/api/login/: User login
+/api/notes/: List and create notes
+/api/notes/<id>/: Retrieve, update, and delete a specific note
