from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h3>Hello, Welcome to Flask series</h3>'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

