import random
import json
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
}

def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
        

    return random.choice(responses["default"])

def chatbot():
    print("chatbot: Hi How can i assist you today?")
    while True:

        user_input = input("user:  ").lower()
        response = get_response(user_input)
        print("chatbot: " , response)

        if user_input == "goodbye":
            break