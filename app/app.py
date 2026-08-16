from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Fintech Demo",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/transaction")
def transaction():
    return jsonify({
        "message": "Transaction service is working",
        "status": "successful"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)