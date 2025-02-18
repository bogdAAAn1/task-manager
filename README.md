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


## Screenshots

![Login page](screenshots/img_1.png)

![Task List page](screenshots/img_2.png)

![Add Task page](screenshots/img_3.png)

![Edit Task page](screenshots/img_4.png)

![Delete Task page](screenshots/img_5.png)

![Position List page](screenshots/img_6.png)

![Add Position page](screenshots/img_7.png)

![Edit Position page](screenshots/img_8.png)

![Delete Position page](screenshots/img_9.png)

![Task Type List page](screenshots/img_10.png)

![Add Task Type page](screenshots/img_11.png)

![Edit Task Type page](screenshots/img_12.png)

![Delete Task Type page](screenshots/img_13.png)

![Worker List page](screenshots/img_14.png)

![Worker Detail page](screenshots/img_18.png)

![Add Worker page](screenshots/img_15.png)

![Edit Worker page](screenshots/img_16.png)

![Delete Worker page](screenshots/img_17.png)
