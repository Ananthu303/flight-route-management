# Flight Routes System

A Django web application for managing airport routes using a binary tree structure. The system allows users to create, search, analyze, and visualize flight route networks, where each airport node can have left and right child connections forming a complete route hierarchy.

## 📋 Project Overview

This project implements a Flight Routes System designed to model airport connections as a binary tree. Each airport represents a node with optional left and right child airports, enabling efficient traversal and analysis of flight routes such as finding the last reachable airport and identifying routes with the shortest or longest durations.

## ✨ Features

### Core Functionality

1. **Airport Route Management (CRUD Operations)**
   - Add new airport routes with code, position, and duration
   - Edit existing airport routes
   - Delete airport routes
   - List all airport routes with details

2. **Question 1: Find Last Reachable Node**
   - Interactive search form with dropdown selection
   - Choose starting airport from existing nodes
   - Select direction (Left or Right)
   - System traverses continuously until reaching the last node
   - Displays comprehensive result with starting and ending points

3. **Question 2: Airport with Longest Duration**
   - Automatically finds and displays the airport with maximum duration
   - Shows complete details including connections

4. **Question 3: Airport with Shortest Duration**
   - Automatically finds and displays the airport with minimum duration
   - Shows complete details including connections

### Additional Features
- **Dashboard**: Home page with statistics and quick actions
- **Admin Panel**: Full Django admin integration for easy management
- **Responsive Design**: Bootstrap 5 for mobile-friendly interface
- **Form Validation**: Comprehensive client and server-side validation
- **User Feedback**: Success/error messages for all operations
- **Professional UI**: Modern gradient design with icons

## 🏗️ Project Structure
```
flight_routes_project/
├── flight_routes/             # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
│
├── airports/                  # Main application
│   ├── migrations/            # Database migrations
│   ├── management/
│   │   └── commands/
│   │       └── load_sample_data.py  # Management command
│   ├── templates/             # HTML templates
│   │   └── airports/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── add_airport.html
│   │       ├── edit_airport.html
│   │       ├── delete_airport.html
│   │       ├── airport_list.html
│   │       ├── search_last_reachable.html
│   │       ├── longest_duration.html
│   │       └── shortest_duration.html
│   ├── __init__.py
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # AirportRoute model
│   ├── forms.py               # Django forms
│   ├── views.py               # View functions
│   ├── urls.py                # App URL configuration
│   └── tests.py               # Unit tests
│
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database (created after migration)
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 🗄️ Database Model

### AirportRoute Model

```python
class AirportRoute(models.Model):
    airport_code = CharField       # Unique code (e.g., JFK, LAX)
    position = CharField           # Position in network
    duration = IntegerField        # Flight duration in minutes
    left = ForeignKey('self')      # Left child airport
    right = ForeignKey('self')     # Right child airport
    created_at = DateTimeField     # Auto timestamp
    updated_at = DateTimeField     # Auto timestamp
```

**Key Methods:**
- `get_last_reachable_node(direction)`: Traverse tree to find last node
- `get_airport_with_longest_duration()`: Class method for max duration
- `get_airport_with_shortest_duration()`: Class method for min duration

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12+ or higher
- Django 4.2 or higher
- pip package manager

### Step-by-Step Installation

1. **Clone the repository and navigate to the root folder:**
   ```bash
   cd flight-route-management
   ```

2. Create and Activate a Virtual Environment

   It is recommended to use a virtual environment to manage dependencies for this project. Here’s how to create and activate it:

   For **Windows**:
   ```bash
   python -m venv venv

   venv\Scripts\activate
   ```

   For **macOS/Linux**:
   ```bash
   python3 -m venv venv

   source venv/bin/activate
   ```

Once activated, your terminal should show something like `(venv)` indicating that the virtual environment is active.
3. **Navigate to the project directory and install dependencies**
   ```bash
   cd flight_routes_project
   pip install -r requirements.txt
   ```


4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

6. **Load sample data using management command for testing:**
   ```bash
   python manage.py load_sample_data
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Main Application: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📱 Usage Guide

### Adding Airport Routes

1. Navigate to "Add Airport" from the menu or dashboard
2. Fill in the required fields:
   - **Airport Code**: Unique identifier (e.g., JFK, LAX, DEL)
   - **Position**: Description of position in network
   - **Duration**: Flight duration in minutes
   - **Left/Right**: Optional connections to other airports
3. Click "Add Airport Route"

### Finding Last Reachable Node (Question 1)

1. Go to "Queries" → "Last Reachable Node"
2. Select a starting airport from the dropdown
3. Choose direction (Left or Right)
4. Click "Find Last Reachable Node"
5. View the result showing the path traversed

### Viewing Longest Duration (Question 2)

1. Go to "Queries" → "Longest Duration"
2. The system automatically displays the airport with maximum duration
3. View complete details including connections

### Viewing Shortest Duration (Question 3)

1. Go to "Queries" → "Shortest Duration"
2. The system automatically displays the airport with minimum duration
3. View complete details including connections


## 📊 Sample Data Structure

Example of a binary tree structure:

```
                ROOT (Main Hub, 90 min)
               /                        \
        LEFT (East Coast, 45 min)   RIGHT (West Coast, 60 min)
           /
    TERMINAL (Regional Hub, 30 min)
```

In this example:
- Starting from ROOT going Left → Last reachable: TERMINAL
- Starting from ROOT going Right → Last reachable: RIGHT
- Longest duration: ROOT (90 min)
- Shortest duration: TERMINAL (30 min)

**Note:** The "position" field is simply a descriptive text field. You can use any meaningful descriptions like:
- "Main Hub"
- "Regional Terminal"
- "International Gateway"
- "Domestic Hub"
- etc.

## 🎨 Technologies Used

- **Backend**: Django 4.2+
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Bootstrap Icons
- **Template Engine**: Django Templates

### URLs (airports/urls.py)

Main routes:
- `/` - Home dashboard
- `/airports/` - List all airports
- `/airports/add/` - Add new airport
- `/airports/edit/<id>/` - Edit airport
- `/airports/delete/<id>/` - Delete airport
- `/search/last-reachable/` - Question 1
- `/airports/longest-duration/` - Question 2
- `/airports/shortest-duration/` - Question 3
---

**Note**: This application fully implements the required functionality for the Flight Routes System.
