from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
app = Flask(__name__)
# Set the static folder for serving static files like CSS, JavaScript, etc.
app.static_folder = 'static'
# Enable debugging mode, which provides detailed error messages
app.debug = True

# Define a route for the homepage ('/') that renders an HTML template
@app.route('/')
def index():
    """
    Render the index.html template for the homepage.
    This route is responsible for displaying the home page.
    """
    return render_template('index.html')

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run()
