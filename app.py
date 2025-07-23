from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Example routes for navigation (optional for now)
@app.route("/route")
def route():
    return "Route Optimizer Module"

@app.route("/damage")
def damage():
    return "Damage Detection Module"

@app.route("/behavior")
def behavior():
    return "Driving Behavior Dashboard"

@app.route("/eta")
def eta():
    return "Delivery Time Predictor"

if __name__ == "__main__":
    app.run(debug=True)
