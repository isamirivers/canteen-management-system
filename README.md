# Canteen Management System

A web application for managing orders in an educational institution's canteen.

## Features

- Menu and dish management
- Order creation
- User administration
- Order status tracking
- Archive of completed orders

## Requirements

- Python 3.8+
- MongoDB 4.4+
- Web browser with modern standards support

## Installation

1. Clone the repository:
    ```sh
    git clone <repository URL>
    cd canteen-management-system
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the settings in the `config.py` file:
    - Open the `config.py` file in a text editor.
    - Change the `SECRET_KEY` value to a random string to ensure session security.
    - Ensure the MongoDB settings (`MONGODB_HOST`, `MONGODB_PORT`, `MONGODB_DB`) match your environment.
    - Optionally, change the Flask settings (`DEBUG`, `HOST`, `PORT`).

    Example:
    ```python
    class Config:
        # MongoDB settings
        MONGODB_HOST = 'localhost'
        MONGODB_PORT = 27017
        MONGODB_DB = 'stolovaya'

        # Flask settings
        SECRET_KEY = 'your-secure-random-string'
        DEBUG = False

        # Server settings
        HOST = '0.0.0.0'
        PORT = 5000
    ```

5. Start the MongoDB server if it is not already running.

6. Create an admin user:
    ```sh
    python create_admin.py
    ```

7. Run the application:
    ```sh
    python main.py
    ```

8. Open a web browser and go to `http://localhost:5000`.
