#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install necessary libraries
pip install pydub sudo apt-get install ffmpeg

echo "Setup complete. Virtual environment created and libraries installed."