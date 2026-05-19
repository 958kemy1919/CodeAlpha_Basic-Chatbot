chatbot = {
    "hello": "Hi!",
    "how are you": "I'm fine",
    "how old are you": "I am 18",
    "where": "In the hotel",
    "when": "Yesterday morning",
    "who": "My best friend",
    "bye": "Goodbye",
}
while True:
    user_input = input("You: ").lower()
    if user_input in chatbot:
        print(f"Bot: {chatbot[user_input]}")
        if user_input == "bye":
            break
    else:
        print("BOT: I don't understand!")

