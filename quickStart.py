from openai import OpenAI #imports OpenAI class, which provides a structured interface to interact with OpenAI's API
client = OpenAI() #creates an instance of the OpenAI class. Client object is used to send requests to the API

completion = client.chat.completions.create(
    model="gpt-4o-mini",  #specifies the model to use for the completion
    messages=[ #list of messages forming context of conversation. Each message has a role and content.
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message) #completion is the response object returned by the API
#choices contains a list of possible completions, most requests return a single completion so choices[0] is used
#message is the actual response from the assistant includeing the role and content