# Simple rule-based chatbot using dictionary responses

chatbot = {
    "hello": "Hi!",
    "how are you": "I'm fine, thanks!",
    "how old are you": "I am 18",
    "where": "In the hotel",
    "when": "Yesterday morning",
    "who": "My best friend",
    "bye": "Goodbye!"
}

print("Chatbot is running... Type 'bye' to exit.\n")

while True:

    # Get user input and normalize it
    user_input = input("You: ").lower()

    # Check if input exists in predefined responses
    if user_input in chatbot:
        print(f"Bot: {chatbot[user_input]}")

        # Exit condition
        if user_input == "bye":
            break

    # Default response for unknown inputs
    else:
        print("Bot: I don't understand!")

