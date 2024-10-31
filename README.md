# Excel Contact Manager

Excel Contact Manager is an API project built with Django and Django REST Framework to manage and upload contact numbers from Excel files into a MongoDB database using Djongo.

---

## Features

- Upload Excel files with contact numbers.
- CRUD APIs for managing contact numbers.
- Bulk data handling for efficient processing.

---

## Prerequisites

- Python (3.8 or higher)
- Django
- Django REST Framework
- Djongo (for MongoDB integration)
- pandas (for handling Excel files)

---

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yousefvafaei/ExcelContactManager.git
   cd ExcelContactManager
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

---

## API Usage

### Upload Excel File

- **Endpoint:** `/api/upload-phone-numbers/`
- **Method:** `POST`
- **Description:** Upload an Excel file with a `mobile` column to add contacts to the MongoDB database.


### CRUD Endpoints

- **List Contacts:** `GET /api/phone-numbers/`
- **Create Contact:** `POST /api/phone-numbers/`
- **Retrieve a Contact:** `GET /api/phone-numbers/<id>/`
- **Update Contact:** `PUT /api/phone-numbers/<id>/`
- **Delete Contact:** `DELETE /api/phone-numbers/<id>/`

---
