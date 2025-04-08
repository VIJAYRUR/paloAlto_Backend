# FitFoodie Backend Documentation

Welcome to the FitFoodie Backend documentation. This directory contains comprehensive documentation for the FitFoodie backend API.

## Table of Contents

- [Setup Guide](SETUP.md) - Instructions for setting up and running the backend
- [Architecture Overview](ARCHITECTURE.md) - Details about the backend architecture
- [API Documentation](API.md) - Information about the API endpoints
- [Current Implementation Status](IMPLEMENTATION_STATUS.md) - Current state of the backend implementation
- [Future Tasks](FUTURE_TASKS.md) - Planned enhancements and future development tasks

## Quick Start

To get started with the FitFoodie Backend, follow these steps:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `python run.py`

For more detailed instructions, see the [Setup Guide](SETUP.md).

## Project Overview

The FitFoodie Backend is a RESTful API built with Flask that serves as the backend for the FitFoodie mobile application. It provides endpoints for user authentication, meal management, influencer profiles, and order processing.

### Key Features

- **User Authentication**: Register, login, and manage user sessions
- **User Profiles**: Store and retrieve user profiles with physical attributes and dietary preferences
- **Meal Management**: Create, read, update, and delete meals with macronutrient information
- **Influencer Profiles**: Manage influencer profiles and their content
- **Order Processing**: Handle ingredient orders with affiliate links

## Contributing

If you'd like to contribute to the FitFoodie Backend, please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## Support

If you encounter any issues or have questions, please:

1. Check the existing documentation
2. Look for similar issues in the GitHub repository
3. Create a new issue with detailed information about your problem

## License

This project is licensed under the MIT License - see the LICENSE file for details.
