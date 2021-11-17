from urllib import request

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/query-string-test")
def query_string_test():
    return request.args.get('tainted')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    title = "Bob"
