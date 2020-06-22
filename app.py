from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def receive_get_request():
    print("GET request")
    return "GET response"


@app.route("/", methods=['POST'])
def receive_post_request():
    print("POST request")
    return "POST response"


if __name__ == "__main__":
    app.run()
