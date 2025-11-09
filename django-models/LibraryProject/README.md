LibraryProject - Django Setup Assignment

Objective:
Gain familiarity with Django by setting up a Django development environment and creating a basic Django project.
This task introduces the workflow of Django projects, including project creation and running the development server.

Task Description:
Install Django and create a new Django project named LibraryProject.
This setup serves as the foundation for developing Django applications.
You will also explore the project’s default structure to understand the roles of its components.

Steps:

1. Install Django:
   - Ensure Python is installed on your system.
   - Install Django using pip:
     pip install django

2. Create Your Django Project:
   - Run the command to create a new project:
     django-admin startproject LibraryProject

3. Run the Development Server:
   - Navigate into your project directory:
     cd LibraryProject
   - Create a README.md file inside LibraryProject
   - Start the development server:
     python manage.py runserver
   - Open a web browser and go to:
     http://127.0.0.1:8000/
     You should see the default Django welcome page.

4. Explore the Project Structure:
   - settings.py: Configuration for the Django project.
   - urls.py: URL declarations for the project; acts as a “table of contents” for your Django-powered site.
   - manage.py: A command-line utility to interact with the Django project.
