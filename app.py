from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge = json.load(file)


def get_response(user_input):
    user_input = user_input.lower().strip()

    # Check patterns
    for topic in knowledge["patterns"].values():
        for pattern in topic["patterns"]:
            if pattern.lower() in user_input:
                return topic["response"]

    # Check AI knowledge
    for item in knowledge["knowledge"]:
        question = item["question"].lower()

        keywords = (
            question.replace("what is", "")
                    .replace("what are", "")
                    .replace("?", "")
                    .strip()
        )

        if keywords in user_input:
            return item["answer"]

    return "Sorry, I don't know the answer to that question."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = get_response(user_message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)