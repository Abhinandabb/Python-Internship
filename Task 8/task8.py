print("Hello! I'm your chatbot. Type 'Quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye! 👋")
        break
    elif "hello" in user_input.lower() or "hi" in user_input.lower():
        print("Chatbot: Hello there! How can I assist you today? 😊")
    elif "how are you" in user_input.lower():
        print("Chatbot: I'm doing great! I hope you are too! 😄")
    elif "what is your name" in user_input.lower():
        print("Chatbot: I am your chatbot, your virtual assistant! 🤖")
    elif "today's date" in user_input.lower():
        from datetime import datetime
        today = datetime.now()
        print("Chatbot: Today's date is", today.strftime("%Y-%m-%d"))
    elif "what is the weather" in user_input.lower():
        print("Chatbot: I currently don't have permission to access weather data. Try checking a weather app. 🌤️")
    elif "tell me a joke" in user_input.lower():
        print("Chatbot: Q: Why do Python programmers prefer snakes?\nA: Because they hate semicolons! 🐍❌;")
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
