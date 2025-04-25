from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Used for flashing messages

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')  # Make sure this file exists

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

#skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

#Upload work page
@app.route('/uploadwork')
def uploadwork():
    return render_template('uploadwork.html')

#hobbies page
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

#academics page
@app.route('/academics')
def academics():
    return render_template('academics.html')

#experience page
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Handle form logic (save to DB, send email, etc.)
        print(f"New message from {name} ({email}): {message}")
        
        flash('Thank you for reaching out! I will get back to you soon.')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
