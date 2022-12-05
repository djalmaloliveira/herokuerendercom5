from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'app renderizado'


@app.route("/inscrito/<nome_inscrito>")
def inscrito(nome_inscrito):
    return f"Olá {nome_inscrito}"


if __name__ == '__main__':
    app.run(debug=True)