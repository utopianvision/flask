from flask import Flask
from flask import render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html', title="Home Page")

@app.route('/about')
def about():
    return "This is the About page."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)