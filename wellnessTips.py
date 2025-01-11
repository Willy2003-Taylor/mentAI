from backAndForth import *

def wellnessResponse():
    prompt = """
    You are a wellness assistant specializing in creating personalized wellness tips. I will provide you with a conversation history between a user and a therapist stored in a Python list of dictionaries. Each dictionary has a "role" key (which can be "user", "system", or "chatbot") and a "content" key (which contains the message text).

    Analyze the conversation history to identify the user's challenges, needs, and concerns. Based on this, create 5 actionable and personalized wellness tips for the user. Focus on areas such as stress management, emotional well-being, physical health, and mindfulness.

    Here is the conversation history:
    {{conversation_history}}

    Please ensure the wellness tips:
    1. Address the specific concerns or goals mentioned in the conversation.
    2. Are practical and easy to follow.
    3. Avoid medical advice and remain focused on general wellness.

    Format your response as follows:
    """
    completion = client.chat.completions.create(
    model="gpt-4o-mini",  #specifies the model to use for the completion
    messages=[ #list of messages forming context of conversation. Each message has a role and content.
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]

