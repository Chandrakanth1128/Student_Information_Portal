from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return"""
    <h1>Student Information Portal</h1>
    <a href='/about'>About</a><br>
    <a href='/contact'>Contact</a>
    """
@app.route('/about')
def about():
    return"""
    <h2>About Portal</h2>
    <p>This portal manages student information.</p>
    """
@app.route('/contact')
def contact():
    return"""
    <h2>Contact Us</h2>
    <p>Email:admin@college.com</p>
    """
@app.route('/student/<int:id>')
def student(id):
    return f"""
    <h2>Student Profile</h2>
    Student ID: {id}
"""
if __name__ == "__main__":
    app.run(debug=True)