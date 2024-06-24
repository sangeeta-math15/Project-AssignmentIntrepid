# Intrepid Documentation

Welcome to the Intrepid Application. This documentation provides details on the Intrepid application.

## Requirements

All the installed packages and their versions are listed in the `requirements.txt` file, which serves as a record of the project dependencies.

### Dependencies:
- asgiref==3.8.1
- Django==4.2.13
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- mysqlclient==1.4.6
- pillow==10.3.0
- PyJWT==2.8.0
- PyMySQL==1.1.1
- python-dotenv==1.0.1
- sqlparse==0.5.0
- typing_extensions==4.12.2

## Getting Started

Follow these steps to get the project up and running on your local machine.

1. Clone the Repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the root directory of your Django project using the terminal or command prompt.

    ```bash
    cd intrepid
    ```

3. Create and activate the virtual environment:

    - On Windows: `python -m venv venv && venv\Scripts\activate`
    - On macOS/Linux: `python3 -m venv venv && source venv/bin/activate`

4. Install the dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

5. *Database Configuration:*

   Open the settings.py file in your Django project and update the DATABASES setting with your MySQL database credentials.
    ```bash
   python DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'OPTIONS': {
               'init_command': "SET default_storage_engine=INNODB",
           },
           'NAME': 'database name',     # Replace with your database name
           'USER': 'your username',     # Replace with your MySQL server username
           'PASSWORD': 'your password', # Replace with your database password
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the server:

    ```bash
    python manage.py runserver
    ```

## Table of Contents

1. [Welcome Message](#1-welcome-message)
2. [Register User](#2-register-user)
3. [User Login](#3-user-login)
4. [User Logout](#4-user-logout)
5. [List Packages](#5-list-packages)
6. [Create Package](#6-create-package)
7. [Retrieve Package](#7-retrieve-package)
8. [Update Package](#8-update-package)
9. [Partial Update Package](#9-partial-update-package)
10. [Delete Package](#10-delete-package)
11. [List Reviews](#11-list-reviews)
12. [Create Review](#12-create-review)
13. [Retrieve Review](#13-retrieve-review)
14. [Update Review](#14-update-review)
15. [Partial Update Review](#15-partial-update-review)
16. [Delete Review](#16-delete-review)
17. [List Images](#17-list-images)
18. [Upload Image](#18-upload-image)
19. [Retrieve Image](#19-retrieve-image)
20. [Update Image](#20-update-image)
21. [Partial Update Image](#21-partial-update-image)
22. [Delete Image](#22-delete-image)

## API Endpoints

### 1. Welcome Message

- **URL:** `/welcome/`
- **Method:** `GET`
- **Description:** Returns a welcome message.
- **Access:** Public

### 2. Register User

- **URL:** `/auth/register/`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Access:** Public
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password",
        "email": "your_email@example.com"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "username": "your_username",
        "email": "your_email@example.com"
    }
    ```

### 3. User Login

- **URL:** `/auth/login/`
- **Method:** `POST`
- **Description:** Logs in a user and returns JWT tokens.
- **Access:** Public
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
        "refresh": "your_refresh_token",
        "access": "your_access_token"
    }
    ```

### 4. User Logout

- **URL:** `/auth/logout/`
- **Method:** `POST`
- **Description:** Logs out a user by blacklisting the refresh token.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:**
    ```json
    {
        "refresh": "your_refresh_token"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Successfully logged out."
    }
    ```

### 5. List Packages

- **URL:** `/api/packages/`
- **Method:** `GET`
- **Description:** Retrieves a list of packages.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 6. Create Package

- **URL:** `/api/packages/`
- **Method:** `POST`
- **Description:** Creates a new package.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:**
    ```json
    {
        "name": "New Package",
        "overview": "Overview of the new package",
        "cost": 1200.00,
        "hotels": [1, 2]
    }
    ```
- **Response:**
    ```json
    {
        "id": 3,
        "name": "New Package",
        "overview": "Overview of the new package",
        "cost": 1200.00,
        "hotels": [
            {
                "id": 1,
                "name": "Hotel 1",
                "description": "Description of hotel 1"
            },
            {
                "id": 2,
                "name": "Hotel 2",
                "description": "Description of hotel 2"
            }
        ],
        "images_set": [],
        "reviews": []
    }
    ```

### 7. Retrieve Package

- **URL:** `/api/packages/{id}/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific package.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 8. Update Package

- **URL:** `/api/packages/{id}/`
- **Method:** `PUT`
- **Description:** Updates a package.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:** Same as the create package request body.
- **Response:** Same as the create package response.

### 9. Partial Update Package

- **URL:** `/api/packages/{id}/`
- **Method:** `PATCH`
- **Description:** Partially updates a package.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:** Partial fields to be updated.
- **Response:** Same as the create package response.

### 10. Delete Package

- **URL:** `/api/packages/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes a package.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 11. List Reviews

- **URL:** `/api/reviews/`
- **Method:** `GET`
- **Description:** Retrieves a list of reviews.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 12. Create Review

- **URL:** `/api/reviews/`
- **Method:** `POST`
- **Description:** Creates a new review.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:**
    ```json
    {
        "package": 1,
        "review_text": "Amazing experience!",
        "rating": 4.5
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "package": 1,
        "reviewer": 1,
        "reviewer_username": "logged_in_user_username",
        "review_text": "Amazing experience!",
        "rating": 4.5
    }
    ```

### 13. Retrieve Review

- **URL:** `/api/reviews/{id}/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific review.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 14. Update Review

- **URL:** `/api/reviews/{id}/`
- **Method:** `PUT`
- **Description:** Updates a review.
- **Access:** Reviewer (logged-in user who created the review) or Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:** Same as the create review request body.
- **Response:** Same as the create review response.

### 15. Partial Update Review

- **URL:** `/api/reviews/{id}/`
- **Method:** `PATCH`
- **Description:** Partially updates a review.
- **Access:** Reviewer (logged-in user who created the review) or Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:** Partial fields to be updated.
- **Response:** Same as the create review response.

### 16. Delete Review

- **URL:** `/api/reviews/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes a review.
- **Access:** Reviewer (logged-in user who created the review) or Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 17. List Images

- **URL:** `/api/images/`
- **Method:** `GET`
- **Description:** Retrieves a list of images.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 18. Upload Image

- **URL:** `/api/images/`
- **Method:** `POST`
- **Description:** Uploads a new image.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body (form-data):**
    - `package`: `1`
    - `image`: `<image_file>`
- **Response:**
    ```json
    {
        "id": 1,
        "package": 1,
        "package_name": "Package 1",
        "image": "/packages/images/your_image.jpg"
    }
    ```

### 19. Retrieve Image

- **URL:** `/api/images/{id}/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific image.
- **Access:** Logged-in users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

### 20. Update Image

- **URL:** `/api/images/{id}/`
- **Method:** `PUT`
- **Description:** Updates an image.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:** Same as the upload image request body.
- **Response:** Same as the upload image response.

### 21. Partial Update Image

- **URL:** `/api/images/{id}/`
- **Method:** `PATCH`
- **Description:** Partially updates an image.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```
- **Request Body:** Partial fields to be updated.
- **Response:** Same as the upload image response.

### 22. Delete Image

- **URL:** `/api/images/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes an image.
- **Access:** Admin users
- **Headers:** 
    ```http
    Authorization: Bearer <your_access_token>
    ```

## Important Details

- Ensure that the `SECRET_KEY` in `intrepid/settings.py` is set to a secure value.
- Customize the `SIMPLE_JWT` settings in `intrepid/settings.py` as per your requirements.
- Regularly update dependencies and apply security patches.