import json
from openai import OpenAI

client = OpenAI(
api_key = "sk-P2th-cAA47bO2H6iIIGdLd0KNoO4WzTmPJ2P0QUh4rT3BlbkFJDCxQHBNzRAB2fd7LjXYpgkLIRGAK0TV6gsg3leRjkA"
)

prompt = input("Ask a question about Elden Ring. " )
#How do you make a Gold-Pickled Fowl Foot in Elden Ring

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model = "gpt-3.5-turbo-1106"
)

    
print(chat_completion.choices[0].message.content)

with open('chatgpt_output.json', 'w') as f:
    json.dump((chat_completion.choices[0].message.content), f, indent=4)

        
    