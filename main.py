import json
from openai import OpenAI

boss = "Radahn"
vigor = "10"
mind = "20"
endurance = "20"
strength = "17"
dexterity = "20"
intelligence = "15"
faith = "30"
arcane = "10"

client = OpenAI(
api_key = "sk-P2th-cAA47bO2H6iIIGdLd0KNoO4WzTmPJ2P0QUh4rT3BlbkFJDCxQHBNzRAB2fd7LjXYpgkLIRGAK0TV6gsg3leRjkA"
)


prompt = "In Elden Ring, how can I beat " + (boss) + " The following answers should include weapons and items from Elden Ring. \n" + "Weapons from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance " + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "Spells and Incantations from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance " + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "Armor from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance " + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "list top three items \n" + "List a Strategy for beating " + (boss) + "\n" + "Now list the strategy for beating this boss from Elden Ring"
#How do you make a Gold-Pickled Fowl Foot in Elden Ring

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a list of publicly known weapons, items, and armor from Elden Ring",
        },
        {
            "role": "user",
            "content": "Given a Boss from Elden Ring, list the best weapons, armour, and items to use against this boss in order to increase your chance of winning against it.",
        },
        {
            "role": "assistant",
            "content": "Weapons: \n [list  3 weapons], Armor: \n [list 3 armor], Items: \n [list 3 items]"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    model = "gpt-3.5-turbo-1106"
)

    
print(chat_completion.choices[0].message.content)

with open('chatgpt_output.json', 'w') as f:
  json.dump((chat_completion.choices[0].message.content), f, indent=4)

        
    