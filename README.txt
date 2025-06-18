# Project API Documentation

## Overview

This project is a Django REST API that includes user authentication with JWT, device management, and API schema documentation.

---

## API Endpoints

### Authentication

Base URL: `/api/auth/`

- **POST** `/register/`
  Register a new user.
  **Request body:**
  {
    "email": "user@example.com",
    "password": "your_password"
  }
  **Response:**
  - 201 Created on success
  - 400 Bad Request if validation fails

- **POST** `/token/`
  Obtain JWT tokens (access and refresh) for authentication.
  **Request body:**
  {
    "email": "user@example.com",
    "password": "your_password"
  }
  **Response:**
  - 200 OK with access and refresh tokens
  - 401 Unauthorized if credentials are invalid

- **POST** `/token/refresh/`
  Refresh the access token using a refresh token.

---

### Devices

Base URL: `/api/devices/`

- **GET** `/my-devices/`
  Retrieve the list of devices for the authenticated user.
  **Authentication required:** Bearer token (JWT) in Authorization header.
  **Response:**
  - 200 OK with a list of devices

---

### API Schema and Documentation

- **GET** `/api/schema/`
  Returns the OpenAPI schema in JSON format.

- **GET** `/api/schema/swagger-ui/`
  Swagger UI documentation for the API.

- **GET** `/api/schema/redoc/`
  ReDoc documentation for the API.

---

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <project_directory>

2. Create and activate a virtual environment:

    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:

    pip install -r requirements.txt

4. Apply migrations:

    python manage.py migrate

5. Create a superuser (optional, for admin access):

    python manage.py createsuperuser

6. Run the development server:

    python manage.py runserver

Access the API documentation at:

    Swagger UI: http://localhost:8000/api/schema/swagger-ui/

    ReDoc: http://localhost:8000/api/schema/redoc/