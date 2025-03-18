import json
import os

# Save object to JSON file
def save_object_to_file(obj, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(obj, f)
        return True
    except Exception as error:
        print(f'Error saving object: {error}')
        return False

# Load object from JSON file
async def load_object_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as error:
        print(f'Error loading object: {error}')
        return None

# Read file content
async def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as error:
        print(f'Error reading file: {error}')
        return None

# Create file
async def create_file(file_path, content=''):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except Exception as error:
        print(f'Error creating file: {error}')
        return False
