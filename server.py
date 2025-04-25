from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔐 Google Gemini API Key
API_KEY = "AIzaSyAi-T726fwJy0YdaTlFxwqwIge1Ic36_eM"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Home Route
@app.route("/")
def home():
    return "Nebula AI is running! 🚀 Try sending a request to /chat."

# ✅ Chatbot API Route — Handles both GET and POST
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "👋 This is the Nebula AI /chat endpoint. Please send a POST request with a message."

    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # 🧠 Add prompt for Gemini
        prompt = f"""
        You are Nebula AI, a powerful and friendly chatbot. 
        Always introduce yourself as 'Nebula AI' and not 'Gemini'.
        Keep responses clear and engaging.

        User: {user_input}
        """

        response = model.generate_content(prompt)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
