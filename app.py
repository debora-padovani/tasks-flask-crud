from flask import Flask


app = Flask(__name__) # se implementado de forma manual __name__ = main

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True) #garantir que só terá o debug quando executado de forma manual ( ou seja, em desenvolvimento local )