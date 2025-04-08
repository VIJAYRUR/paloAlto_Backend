#!/bin/bash

# Create scripts directory if it doesn't exist
mkdir -p scripts

# Script to start the FitFoodie backend
echo "Starting FitFoodie backend..."

# Check if virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies..."
  pip install -r requirements.txt
fi

# Start the Flask server
echo "Starting Flask server..."
python run.py

# Exit with the same code as the Flask command
exit $?
