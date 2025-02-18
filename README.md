# Task Manager

## Check it out!

[Task Manager project deployed to Render](https://task-manager-rl8w.onrender.com/)
```
login: user
password: user12345
```

# Installation

Clone the repository by running the command:

```:sh
git clone https://github.com/bogdAAAn1/task-manager.git
```

Change to the project directory:

```:sh
cd py-task-manager
```

If necessary, switch to the `develop` branch:

```:sh
git checkout develop
```

Create a virtual environment:

```:sh
python -m venv venv
```

Activate the virtual environment:

- On Linux/MacOS:

  ```:sh
  source venv/bin/activate
  ```

- On Windows:

  ```:sh
  venv\Scripts\activate
  ```

Install the required dependencies:

```:sh
pip install -r requirements.txt
```

## Environment Configuration

Copy the sample environment file:

```:sh
cp .env.sample .env
```

Open the `.env` file in your preferred text editor and update the settings. You must set:

- `SECRET_KEY`: Your Django secret key.
- `DEBUG`: `True` for development or `False` for production.
- `DATABASE_URL`: Specify your database connection (SQLite is used by default, but you can update it for other databases).

Update any other required environment variables as needed.

## Usage

Apply database migrations:

```:sh
python manage.py migrate
```

Start the Django development server:

```:sh
python manage.py runserver
```

Access the application in your web browser at:

```:sh
http://127.0.0.1:8000/
```

## Live Demo

You can access the live version of the application at:

https://task-manager-rl8w.onrender.com/
