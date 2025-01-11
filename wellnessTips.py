#Description: This file contains the code for the wellnessResponse function which generates 5 actionable and personalized wellness tips for the user based on the conversation history between a user and a self-care assistant.
from backAndForth import *

def wellnessResponse(conversationHistory):
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
    messages=[{"role": "system", "content": prompt}]
    for dict in conversationHistory:
        messages.append(dict)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",  #specifies the model to use for the completion
    messages=messages
    )
    print(completion.choices[0].message.content) #completion is the response object returned by the API
#choices contains a list of possible completions, most requests return a single completion so choices[0] is used
#message is the actual response from the assistant includeing the role and content
