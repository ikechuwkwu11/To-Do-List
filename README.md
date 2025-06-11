Task & Account Management API
This is a Django REST Framework-based API that allows users to register, log in, manage tasks, and manage accounts. It provides endpoints for basic user authentication and CRUD operations for Task and Account models.

Features
- Authentication
- User registration (/register)
- User login (/login)
- User logout (/logout)

Task Operations
- Create a new task
- View a single task by ID
- View all tasks
- Update a task
- Delete a task

Admin Functionality
- View all tasks (admin overview)
- View individual task transaction (admin)
- Create a new account (admin)
- View all approved accounts
  
Technologies Used
- Django – Web framework
- Django REST Framework (DRF) – API development
- SQLite / PostgreSQL – Default and production databases
- Python 3.9+

Testing the API
Use tools like:
- Postman
- cURL
- httpie
