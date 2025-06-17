# ✅ Task & Account Management API
A RESTful API built using Django and Django REST Framework that allows users to register, log in, and manage their personal tasks, while administrators can oversee task activity and manage account approvals. Designed with separation of concerns and role-specific views for scalability and control.

## 🔍 Features
- Authentication
- POST /register – Register a new user
- POST /login – Log in to obtain authentication token/session
- POST /logout – Log out and clear session/token

## 📋 Task Operations
- POST /tasks/ – Create a new task
- GET /tasks/<id>/ – View a single task by ID
- GET /tasks/ – View all user tasks
- PUT /tasks/<id>/ – Update a task
- DELETE /tasks/<id>/ – Delete a task

## 🛠️ Admin Functionality
- GET /admin/tasks/ – View all tasks (admin-only)
- GET /admin/tasks/<id>/ – View individual task transaction (admin-only)
- POST /admin/accounts/ – Create a new account
- GET /admin/accounts/approved/ – View all approved accounts

## 🧱 Technologies Used
| Layer         | Technology                                     |
| ------------- | ---------------------------------------------- |
| Backend       | Python 3.9+, Django, Django REST Framework     |
| Database      | SQLite (development), PostgreSQL (production)  |
| API Framework | Django REST Framework                          |
| Auth System   | Django default authentication + DRF Token Auth |


## 🔧 Testing the API
- You can test API endpoints using any of the following tools:
- Postman
- cURL
- httpie

## ✅ Future Improvements
- JWT authentication (via djangorestframework-simplejwt)
- Swagger/OpenAPI documentation
- Role-based permissions
- Automated unit tests
- Docker integration for deployment
