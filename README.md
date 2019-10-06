# A Deadlines app

This is a small Django project to register and manage academic Deadlines

Here are the current django apps that compose this project
- tasks (related to academic tasks mangement)
- submissions ( manages submissions of tasks to academic events)
- users (related to the Student that can signup to use this app)


## Install Required Packages

This project requires a few packages. To install them use the following command:

    pip install -r requirements.txt



## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver
    
To access the application go <http://localhost:8000/>

## Running Tests
Tests are been added gradually, we intend to have in the nearest possible future a good test coverage.

To run tests on the application execute:

    python manage.py test

## Linting

To maintain PEP8 coding standard we implement code linting.
To run the linting tool execute: 

`black .`
