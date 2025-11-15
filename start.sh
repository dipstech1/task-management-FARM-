#! /bin/bash

set -e

PROJECT_DIR=${1:-$(pwd)}

BACKEND_DIR="${PROJECT_DIR}/backend"

echo "Starting backend server from ${BACKEND_DIR}..."

cd "${BACKEND_DIR}" || {
    echo "Failed to get backend directory"
    exit 1
}

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/Scripts/activate
    echo "Virtual env activated"
else
    echo "No virtual environment found"
fi

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Dependencies installed"
else
    echo "No requirements.txt found"
fi

# Start the backend server
echo "Starting the backend server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

