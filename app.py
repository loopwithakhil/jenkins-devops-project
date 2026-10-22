from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to My DevOps CI/CD Pipeline!</h1>
            <h2>Powered by Jenkins, GitHub and Docker</h2>
            <p>My application is running successfully!</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)