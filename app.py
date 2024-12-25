from flask import Flask, render_template, request
import os  # Add this for compatibility with deployment environments

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission here (save data or send an email)
        return "Message Sent!"
    return render_template('contact.html')

if __name__ == '__main__':
    # Use environment variables for host and port for deployment compatibility
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
