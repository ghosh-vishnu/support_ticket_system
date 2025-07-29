# Support Ticket System API

## Overview
This project is a **Support Ticket System REST API** built using Django and Django REST Framework.

- Users can create, view, and update their own tickets (only when the status is "open").
- Admin users can view all tickets, update ticket status, and delete tickets.
- Token-based authentication is implemented for secure API access.

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Apply Migrations and Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 3. Run the Server
```bash
python manage.py runserver
```

## Authentication

Generate a token by sending a POST request:
```http
POST /api/token/
{
  "username": "user1",
  "password": "user123"
}
```

Use the token in request headers:
```
Authorization: Token <your_token>
```

## API Endpoints

| Method | Endpoint                  | Description                       |
|--------|---------------------------|-----------------------------------|
| POST   | /api/tickets/             | Create a new ticket              |
| GET    | /api/tickets/             | View list of tickets             |
| GET    | /api/tickets/<id>/        | Get details of a specific ticket |
| PUT    | /api/tickets/<id>/        | Update an existing ticket        |
| PATCH  | /api/tickets/<id>/status/ | Update the status (admin only)   |
| DELETE | /api/tickets/<id>/        | Delete a ticket (admin only)     |

## Example Request

POST `/api/tickets/`

Headers:
```
Authorization: Token <your_token>
Content-Type: application/json
```

Body:
```json
{
  "title": "Test Ticket",
  "description": "This is my first ticket"
}
```

## Admin Features
- View all tickets
- Update ticket status
- Delete tickets
