import logging
import os

from flask import Flask, jsonify

app = Flask(__name__)

# Application configuration
APP_NAME = "DevOps CI/CD Demo"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# Configure application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    logger.info("Home page requested")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>DevOps CI/CD Demo</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to My DevOps CI/CD Pipeline!</h1>
            <h2>Powered by Jenkins, GitHub and Docker</h2>
            <p>My application is running successfully!</p>
            <p>Application Version: 1.0.0</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    logger.info("Health check requested")

    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/ready")
def readiness():
    logger.info("Readiness check requested")

    return jsonify({
        "status": "ready"
    }), 200


@app.route("/version")
def version():
    logger.info("Version requested")

    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)