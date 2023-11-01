from flask import Flask

app = Flask(__name__)


# route bisa diatur sendiri urlnya kemana
@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True, port=80)  # default port di 5000
