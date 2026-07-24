from flask import Flask
app = Flask(_name_)
@app.route("/")
def home():
 return "Hello! Welcome to Render PaaS."
@app.route("/about")
def about():
 return "This application is deployed on Render."
if _name_ == "_main_":
 app.run(host="0.0.0.0", port=5000)