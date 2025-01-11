#File to take care of back and forth conversation between user and AI. Run by running the command "python backAndForth.py" in the terminal and type back and forth with the API.
from openai import OpenAI
from addToConversationHistory import *
import time
from boldText import *
client = OpenAI()
import os

conversationHistory = [{"role": "system", "content": "You are a Smart Journaler and Therapist, designed to guide users through reflecting on their day and gathering insights about their mental health. Your primary goal is to create a safe, supportive space where users feel encouraged to share details about their daily experiences, emotions, and thoughts. You will ask exactly one open-ended question to the user's response to gather as much information as possible and, once the conversation concludes, provide this data for analysis by another AI model, which will generate personalized mental wellness tips for the user."}]
def chat_with_gpt():
    print(boldText("Self-Care Companion: ") + "Hello! How was your day?")
    start_time = time.time()  # Record the start time
    duration = 60*2  # Duration in seconds

    while time.time() - start_time < duration:
        # Get user input
        user_input = input(boldText("You: "))
        #print("\n")
        
        if user_input.lower() in {"exit", "quit"}: #if user says exit or quit, the conversation ends
            print(boldText("Self-Care Companion: ") + "Goodbye!")
            break

        # Add user input to conversation history
        addToConversationHistory(conversationHistory,{"role": "user", "content": user_input})

        # Call the API
        try:
            response = client.chat.completions.create(model="gpt-4o-mini",messages=conversationHistory)
            reply = response.choices[0].message.content
            print(boldText("Self-Care Companion: ") + reply)

            # Add assistant reply to conversation history
            addToConversationHistory(conversationHistory,{"role": "assistant", "content": reply})

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_gpt()