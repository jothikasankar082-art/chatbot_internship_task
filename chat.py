# Rule-Based Chatbot

print("=" * 50)
print("      Welcome to Rule-Based Chatbot")
print("=" * 50)

print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower().strip()

    # Greeting
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # How are you
    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    # Name
    elif "your name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    # AI
    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    # Python
    elif "python" in user:
        print("Bot: Python is a popular programming language used in AI.")

    # Internship
    elif "internship" in user:
        print("Bot: An internship helps students gain practical experience.")

    # College
    elif "college" in user:
        print("Bot: College is a place for learning and skill development.")

    # Time
    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Date
    elif "date" in user:
        from datetime import datetime
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    # Thanks
    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    # Bye
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Default
    else:
        print("Bot: Sorry, I don't understand that.")