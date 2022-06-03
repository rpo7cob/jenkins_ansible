import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello and Welcome to QCOM Technologies"

@app.route('/Ravi')
def hello():
    return "I am learning Jenkins and this page is displayed by a Docker Container"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
