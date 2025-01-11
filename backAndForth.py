#File to take care of back and forth conversation between user and AI. Run by running the command "python backAndForth.py" in the terminal and type back and forth with the API.
from openai import OpenAI

client = OpenAI()
import os

def chat_with_gpt():
    print("ChatGPT: Hello! How can I assist you today?")

    # Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        # Get user input
        user_input = input("You: ")
        #print("\n")
        
        if user_input.lower() in {"exit", "quit"}: #if user says exit or quit, the conversation ends
            print("ChatGPT: Goodbye!")
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Call the API
        try:
            response = client.chat.completions.create(model="gpt-4o-mini",messages=conversation_history)
            reply = response.choices[0].message.content
            print(f"ChatGPT: {reply}")

            # Add assistant reply to conversation history
            conversation_history.append({"role": "assistant", "content": reply})

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_gpt()
