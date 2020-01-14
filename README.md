# Shredded

A workout reviewer and scheduler that you can use to track your workouts. Shredded will help you to make your own workouts and review them as you doing it. You will be able to check which one you did that day and your progress from one exercise to another, including weights and performances.

## Techs

1. Flask
1. Flask-SQLAlchemy
1. Flask-Migrate

### How to configure your local environment

1. Using virtual environment:

    To create on virtual environment in windows:

    ```bash
    python -m venv venv
    ```

    The second venv will be the name of the environment, the name can be anything. After that, you must activate. To activate, you should access the file activate inside the folder of your virtual enviroment.

    ```bash
    .\venv\Scripts\activate
    ```

    To deactivate:

    ```bash
    deactivate
    ```

    After that you run step 2.

1. Running pip install to install requirements file:

    You must run pip command to install project dependencies from the project.

    ```bash
    pip install -r requirements.txt
    ```
1. Initialize database:
    
    ```bash
    flask db init
    ```

1. Run migrations:

    To have your local database updated to the actual version of it, must run migrations from Flask:

    ```bash
    flask db upgrde
    ```
