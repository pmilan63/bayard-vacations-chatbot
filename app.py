from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Bayard Vacations Chatbot is running"})

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()
        user_message = data.get("message") if data else None
    else:
        user_message = request.args.get("message")

    if not user_message:
        return jsonify({"response": "Please provide a message"}), 400

    bot_reply = get_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

