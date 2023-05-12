# Artistic_Pixel - Django

This is a Digital Art Gallery website used to store digital art. It uses the [Django](https://docs.djangoproject.com/en/4.2/) web framework,[DRF](https://www.django-rest-framework.org/) ,[Ajax](https://code.djangoproject.com/wiki/AJAX) and [PostgreSql](https://www.psycopg.org/docs/).Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd Artistic_Pixel
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your Secret_key to the newly created `.env` file.

8. For PostgreSQL database setup, add database name,username,password,host,port to `.env` file. 

8. Run the app:

   ```bash
   $ python manage.py runserver
   ```

You should now be able to access the app at [http://localhost:8000](http://localhost:5000)!


## Screen shot

1. Home:
![Home page](https://github.com/Grahanam/mylibrary/assets/68738881/7b7dd29c-7459-4156-b128-3c2386d1e187)

2. Create Form:
![Create Form](https://github.com/Grahanam/mylibrary/assets/68738881/f86ea797-d5bb-4f12-8670-a4c15c2c9e96)

3. Edit Form:
![Edit Form](https://github.com/Grahanam/mylibrary/assets/68738881/fdc1c6b2-fd27-4b8a-88a6-66a2845d7647)

