# iVolunteer - Connect Volunteers with NGOs
(Deployed Link: https://sneha23.pythonanywhere.com/)

**iVolunteer** is a web application designed to bridge the gap between NGOs and volunteers, providing an intuitive platform for users to explore, register for, and manage events organized by NGOs.

## Features

- **Browse Events by Category**: Easily explore NGO events across various categories like education, health, environment, and more.
- **Location-Based Filtering**: Find events based on your preferred location for convenience.
- **User Authentication**: Secure signup and login for a personalized experience.
- **Event Registration**: Register for events directly from the platform. Duplicate registrations are automatically prevented.
- **My Events Dashboard**: View and manage all your registered events in one place, complete with event details.
- **Admin Management**: Admins can manage categories, events, and users via the Django admin interface.

## Technology Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Django (Python)
- **Database**: MySQL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ivolunteer.git
   cd ivolunteer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at `[http://127.0.0.1:8000/](https://sneha23.pythonanywhere.com/)`.
