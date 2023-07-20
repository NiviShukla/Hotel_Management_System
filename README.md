# Hotel_Management_System

The Hotel Management System Django App is a web application that allows users to register, login, and book rooms in a hotel. Users can view their profile, including booking details and personal information like name and email. The app provides different categories of rooms for users to choose from while booking.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Features

- User Registration: Users can create a new account by providing their name, email, and password.

- User Login: Existing users can log in using their registered email and password.

- Room Booking: Authenticated users can book rooms from a selection of different categories available in the hotel.

- Profile Page: Users can view their profile, including booking history, personal details, and other relevant information.

- Security: The app uses secure authentication mechanisms to protect user data.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/NiviShukla/Hotel_Management_System.git
   
   cd hotel-management-system
   ```
2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   
   source venv/bin/activate # On Windows, use venv\Scripts\activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations to set up the database:
   ```
   python manage.py migrate
   ```
5. Create a superuser (admin) account:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

The app will be accessible at `http://localhost:8000/`.

## Usage

1. Open your web browser and go to `http://localhost:8000/`.

2. Register a new account using the "Sign Up" link on the home page.

3. Log in using your registered email and password.

4. Browse the available room categories and select a room to book.

5. Go to your profile page to view your booking history and personal details.

## Technologies Used

- Django: Web framework used for building the application.
- Python: Programming language used for backend development.
- HTML/CSS: Markup and styling for the user interface.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or open an issue on the GitHub repository.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
