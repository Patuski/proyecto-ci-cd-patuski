from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Despues de tres/cuatro días he conseguido llegar a este punto, lo siguiente será hackear la NASA"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
