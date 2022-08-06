from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/about")
def about():
    name = "Karen"
    location = "Elk Grove"

    return f"My name is {name}, and I live in {location}."

@app.route("/contact")
def contact():
    email = "karen@example.com"

    return f"Questions? Comments? Complaints? Shoot an email to {email}."

if __name__ == "__main__":
    app.run(debug=True)