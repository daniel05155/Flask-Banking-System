# Banking-System-Using-Flask

## Overview
This is an online banking management system developed in Python. The project aims to simulate basic banking operations, including user registration, login/logout, withdrawals, deposits, and balance inquiries. Currently, the system comprises two main components: a fully functional Command-Line Interface (CLI) version and a Flask-based web version under development.

**Note：** This is a work in progress, and some features may not be fully implemented or optimized.

## Current Features

### CLI Version (Fully Implemented)
- [x] User Registration
- [x] User Login/Logout
- [x] Deposit Functionality
- [x] Withdrawal Functionality
- [x] Fund Transfer
- [x] Balance Inquiry
- [x] Developer Mode (for debugging)

### Web Version ( **Partially Implemented** )
- [x] User Registration (frontend form)
- [x] User Login/Logout (frontend form)
- [ ] Deposit Functionality (to be implemented)
- [ ] Withdrawal Functionality (to be implemented)
- [ ] Balance Inquiry (to be implemented)

## Tech Stack
- Backend: Python 3.x
- Web Framework: Flask
- Data Storage:
  - CLI Version: JSON file
  - Web Version: MySQL (using Flask-MySQLdb)
- Frontend: HTML, CSS (basic implementation)

## File Structure
- `customer_account.json`: Stores user account information (used by CLI version)
- `function.py`: Contains main functionality implementation for CLI version
- `main.py`: Main file for Flask application, contains routes and functionality for web version

## Installation
1. Clone this repository:
   ```
   git clone [repository URL]
   ```
2. Navigate to the project directory:
   ```
   cd Online-Banking-Management-System
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. For the web version, set up MySQL database and update database connection details in `main.py`.

## Usage
### CLI Version
Run the main program:
```
python function.py
```

### Web Version
1. Ensure MySQL service is running.
2. Run the Flask application:
   ```
   python main.py
   ```
3. Access in browser: `http://localhost:5000`

## Roadmap
- [ ] Complete all basic banking functionalities for the web version
- [ ] Improve user interface design
- [ ] Implement robust security measures (e.g., password encryption, two-factor authentication)
- [ ] Add transaction history functionality
- [ ] Integrate error handling and logging
- [ ] Implement unit tests and integration tests

## Known Issues
- We currently implements basic registration and login functionality only in the web version.
- It uses JSON file for data storage, which may pose security risks in the CLI version.
- Lack of proper error handling mechanisms.


<!-- ## Contributing
Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## Contact
[Your Name] - [Your Email]

Project Link: [Project GitHub/GitLab URL] -->

