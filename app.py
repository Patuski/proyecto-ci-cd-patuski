from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "¡Hola Patuski! Mi primer Pipeline CI/CD funciona al 100%."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
