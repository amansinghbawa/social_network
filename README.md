# Social Networking API

This is a Django Rest Framework-based API for a social networking application. The API supports user signup, login, searching users, managing friend requests, and more.

## Features

- User Signup and Login with JWT authentication.
- Search users by email or name.
- Send, accept, reject friend requests.
- List friends and pending friend requests.
- Rate limiting on friend requests (max 3 requests per minute).



## Installation with docker:

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/SINGHBAWA/social_network.git
cd social_network
```

### Step 2. Environment Variables
Create a .env file in the root directory of the project to define your environment variables:
```environment
POSTGRES_DB=social_network_db
POSTGRES_USER=social_network_user
POSTGRES_PASSWORD=your_db_password
```

### Step 3. Build and Run the Containers
Use Docker Compose to build and start the containers:

```bash
docker-compose up --build
```
This command will:
- Build the Docker images for the application.
- Start the PostgreSQL database service.
- Start the Django application, running the necessary database migrations and then starting the development server on http://localhost:8000.

### Step 4. Accessing the Application
Once the containers are up and running, you can access the API via http://localhost:8000.

### Step 5. Stopping the Containers
To stop the containers, press Ctrl+C in the terminal where the containers are running. Alternatively, you can use the following command:
```bash
docker-compose down
```
This will stop and remove the containers, but the database volume will persist.


## Installation on local system

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- A virtual environment tool (optional but recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/SINGHBAWA/social_network.git
cd social_network
```

### Step 2: Create and Activate a Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```


### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database
Update the postgres DATABASES settings in .local_env file

### Step 5: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Run the Development Server
```bash
python manage.py runserver
```

### Step 8: Test the API
You can use tools like Postman or cURL to interact with the API. The server will be running at http://127.0.0.1:8000/.


## API Endpoints
[POSTMAN Collection](Social_media_app.postman_collection.json)

### User Management
- Signup: POST /api/users/signup/
- Login: POST /api/users/login/

Note: GET TOKEN USING login API and use it to access further APIs in HEADERS.
```
Authorization: Bearer <ACCESS TOKEN>
```

### User Search
- Search Users: GET /api/users/search/?keyword=<search_keyword>

### Friend Requests
- Send Friend Request: POST /api/users/friend-request/send/
- Accept Friend Request: PUT /api/users/friend-request/accept/<pk>/
- Reject Friend Request: DELETE /api/users/friend-request/reject/<pk>/
- List Friends: GET /api/users/friends/
- List Pending Friend Requests: GET /api/users/friend-requests/pending/



