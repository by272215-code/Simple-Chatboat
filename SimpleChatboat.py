def chatbot():
    print("=================================")
    print("      Welcome to My Chatbot")
    print("Type 'bye' to exit the chat")
    print("=================================")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks for asking!")

        elif user_input == "what is your name":
            print("Bot: My name is SimpleBot.")

        elif user_input == "who made you":
            print("Bot: I was created using Python.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()