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


@app.route("/api-info")
def api_info():
    return jsonify({
        "service": "Fintech Demo API",
        "version": "1.0",
        "environment": "development"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)