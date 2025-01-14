Features
Event Creation and Management: Admins can create, update, and delete events, specifying details such as date, time, venue, and description.
User Registration: Users can register for events, providing necessary personal information.
Ticket Booking: Users can book tickets for events, with options for different ticket types and quantities.

Admin Panel: A secure admin interface for managing events, users, and bookings.

Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python
Database: SQLlite3
Installation
  1.Clone the Repository:
  bash
  git clone https://github.com/SaurabhBhakare/Event_Management_System.git
  
  2.Set Up the Server:
  Ensure you have a local server environment like XAMPP or WAMP installed.
  Place the cloned repository in the server's root directory (e.g., htdocs for XAMPP).
  
  3.Configure the Database:
  Start the Apache and MySQL services.
  Access phpMyAdmin via http://localhost/phpmyadmin/.
  Create a new database named event_management.
  Import the provided SQL file (event_management.sql) located in the repository to set up the necessary tables.
  
  4.Configure Database Connection:
  Open the config.php file in the project's root directory.
  Update the database connection parameters (host, username, password, database) to match your local setup.
  
  5.Access the Application:
  Navigate to http://localhost/Event_Management_System/ in your web browser to access the user interface.
  For admin functionalities, go to http://localhost/Event_Management_System/admin/.

Usage
Admin:
Log in to the admin panel using the default credentials:
Username: admin
Password: Admin123
Manage events, view user registrations, and handle ticket bookings.

User:
Browse available events on the homepage.
Register for an account to book tickets.
Log in to view and manage your bookings.

Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
This project was developed as part of a learning exercise and is based on various open-source event management systems available on GitHub.

For any issues or inquiries, please contact Saurabh Bhakare.
