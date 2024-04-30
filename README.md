Authentication using session

Django User Authentication System with Session Management

This Django project implements a robust user authentication system with session management,
providing essential features like signup, login, and logout functionalities. 
It ensures secure user authentication and maintains user sessions across different pages of the application.

Features

User Signup: Allows new users to register by providing essential details such as username, email, and password. 
It validates user input and prevents duplicate usernames.
User Login: Enables registered users to log in securely using their username and password. Invalid login attempts are
handled gracefully with appropriate error messages.
Session Management: Utilizes Django's built-in session management to maintain user sessions securely. Users remain 
authenticated across different pages of the application until they choose to log out. Session data is stored securely 
on the server-side, enhancing security.
Password Matching: Ensures that the password entered during signup matches the confirmation password to prevent typos or mistakes.
Error Handling: Provides informative error messages to users in case of invalid input, duplicate usernames, or incorrect login credentials.
User Logout: Allows authenticated users to log out securely, terminating their session and redirecting them to the homepage.
