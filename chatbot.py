import json
from datetime import datetime

# Load the knowledge base
with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge = json.load(file)


def get_response(user_input):
    user_input = user_input.lower().strip()

    # Dynamic Responses
    if "time" in user_input:
        return "Current Time: " + datetime.now().strftime("%I:%M:%S %p")

    if "date" in user_input:
        return "Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    # Check pattern responses
    for topic in knowledge["patterns"].values():
        for pattern in topic["patterns"]:
            if pattern.lower() in user_input:
                return topic["response"]

    # Check knowledge base
    for item in knowledge["knowledge"]:

        question = item["question"].lower()

        # Remove "what is", "what are", "?" for flexible matching
        keywords = (
            question.replace("what is", "")
                    .replace("what are", "")
                    .replace("?", "")
                    .strip()
        )

        if keywords in user_input:
            return item["answer"]

        if question in user_input:
            return item["answer"]

    return "Sorry, I don't know the answer to that question."


print("=" * 60)
print("        RULE-BASED AI CHATBOT")
print("=" * 60)
print("Ask me anything about AI.")
print("Type 'bye' or 'exit' to quit.\n")

while True:

    user = input("You : ")

    response = get_response(user)

    print("Bot :", response)
    print()

    if user.lower() in ["bye", "goodbye", "exit", "see you"]:
        break