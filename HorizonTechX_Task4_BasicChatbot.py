def chatbot():
    print("===== BASIC CHATBOT =====")
    print("Type 'bye' or 'exit' to stop the chatbot.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input in ["hello", "hi"]:
            print("Bot: Hi! How can I help you?")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")
        elif user_input == "help":
            print("Bot: You can say hello, ask how I am, or say bye.")
        elif user_input in ["bye", "exit"]:
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
