# Import the 'app' instance from the 'app' module (assuming 'app.py' contains your Flask app)
from app import app
# Import the 'os' module for environment variables
import os

# Check if this script is being run directly
if __name__ == "__main__":
    # Run the Flask application
    # Listen on all available network interfaces (0.0.0.0) and use the port specified in the 'PORT' environment variable,
    # defaulting to port 8888 if 'PORT' is not set
    app.run("0.0.0.0", port=os.getenv('PORT', 8888))
