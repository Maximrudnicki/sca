# SCA (Spy Cat Agency)

## About

This project was originally a test task for a Golang Junior Position. You can find the Go version of the application [here](https://github.com/Maximrudnicki/Spy-Cat-Agency).

This version of the project is implemented using Django (Python) and PostgreSQL. The application includes custom logger middleware and an external API call to validate the breed of a cat.

### The Task

The Spy Cat Agency (SCA) needs a management application to streamline their spying operations. The system should allow SCA to manage their cats, the missions they undertake, and the targets assigned to them.

## How to Start

1. **Clone the Project**
    ```bash
    git clone https://github.com/Maximrudnicki/sca.git
    cd sca
    ```

2. **Create an `.env` File**
   
   Create a `.env` file in the root directory of the project and add the following fields:
    ```plaintext
    DJANGO_SECRET_KEY=

    POSTGRES_HOST=
    POSTGRES_PORT=
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    ```

   **Note:** You can use `host.docker.internal` instead of `localhost` to connect the app from a Docker container to the PostgreSQL database running on your local machine.

3. **Running the App with Docker**

   Build and start the application using Docker:
    ```bash
    docker build -t sca .
    docker run -p 8000:8000 sca
    ```

4. **Running the App Locally**

   Alternatively, you can run the application on your local machine.

   - Ensure Python and pip are installed:
     ```bash
     python --version
     pip --version
     ```

   - Install the necessary dependencies:
     ```bash
     pip install --no-cache-dir -r requirements.txt
     ```

   - Apply migrations and start the application:
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```

5. **Access the Application**

   Once everything is up and running, visit [http://localhost:8000](http://localhost:8000) in your web browser.

   Alternatively, you can test the API using Postman by visiting this collection: [SCA Postman Collection](https://www.postman.com/navigation-engineer-62741940/workspace/rudnytskyi-test/collection/25383927-2ea6fdcf-a203-4ca9-b2c9-f09eb1bbb83b?action=share&creator=25383927)
