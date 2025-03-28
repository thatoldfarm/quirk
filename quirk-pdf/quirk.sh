#!/bin/bash

# Stop the script if any command fails
set -e

# Execute the Python scripts in the correct order
echo "Running quirk_vid_encode.py..."
python3 quirk_vid_encode.py

echo "Running quirk_vid_decode.py..."
python3 quirk_vid_decode.py

echo "Running quirk_gif_encode.py..."
python3 quirk_gif_encode.py

echo "Running quirk_gif_decode.py..."
python3 quirk_gif_decode.py

echo "All scripts executed successfully."
