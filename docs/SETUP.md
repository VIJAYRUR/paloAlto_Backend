# FitFoodie Backend Setup Guide

This guide provides detailed instructions for setting up and running the FitFoodie Backend API.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or newer
- pip (Python package manager)
- Git for version control
- MongoDB (optional, for local development)

## Setup Instructions

### Clone the Repository

```bash
git clone <repository-url>
cd FitFoodie-Backend
```

### Create a Virtual Environment

It's recommended to use a virtual environment to isolate the project dependencies:

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the root directory with the following variables:

```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
MONGODB_URI=your_mongodb_connection_string
```

Replace `your_secret_key` with a secure random string and `your_mongodb_connection_string` with your MongoDB connection string.

### Database Setup

#### Option 1: MongoDB Atlas (Recommended for Production)

1. Create a MongoDB Atlas account at [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new cluster
3. Create a database user with read/write privileges
4. Get your connection string and add it to the `.env` file

#### Option 2: Local MongoDB (Development)

1. Install MongoDB locally following the [official documentation](https://docs.mongodb.com/manual/installation/)
2. Start the MongoDB service
3. Use `mongodb://localhost:27017/fitfoodie` as your connection string in the `.env` file

### Running the Server

Start the Flask development server:

```bash
python run.py
```

Or use the provided script:

```bash
./scripts/start.sh
```

The server will start at `http://localhost:5000`.

### Verify the Setup

To verify that the server is running correctly, open a web browser or use a tool like curl to access:

```
http://localhost:5000/api/health
```

You should see a response indicating that the API is running.

## Development Workflow

### Running Tests

Run the test suite to ensure everything is working correctly:

```bash
pytest
```

### Code Style

This project follows PEP 8 style guidelines. To check your code:

```bash
flake8
```

### Database Migrations

If you make changes to the database models, you'll need to create and apply migrations:

```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you've activated the virtual environment and installed all dependencies.
2. **Connection Error**: Check that your MongoDB instance is running and the connection string is correct.
3. **Permission Denied**: Ensure that the script files have execute permissions (`chmod +x scripts/*.sh`).

### Getting Help

If you encounter issues not covered here, please:
1. Check the existing issues on the GitHub repository
2. Create a new issue with detailed information about your problem

## Deployment

### Option 1: Heroku

1. Install the Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create fitfoodie-backend`
4. Add a MongoDB add-on: `heroku addons:create mongodb`
5. Set environment variables: `heroku config:set SECRET_KEY=your_secret_key`
6. Deploy the app: `git push heroku main`

### Option 2: AWS

1. Create an EC2 instance
2. Install Python, pip, and other dependencies
3. Clone the repository
4. Set up a virtual environment and install dependencies
5. Configure environment variables
6. Use Gunicorn and Nginx to serve the application
7. Set up a MongoDB Atlas cluster or use Amazon DocumentDB

### Option 3: Docker

1. Build the Docker image: `docker build -t fitfoodie-backend .`
2. Run the container: `docker run -p 5000:5000 fitfoodie-backend`

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
