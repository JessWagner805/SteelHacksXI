import json
from openai import OpenAI

# read through json file
with open('boss_helper_data.json', 'r') as json_file:
    data = json.load(json_file)

# extract data from json file and assign to variables
boss = data["Selected Boss"].capitalize()
vigor = data["Vigor"]
mind = data["Mind"]
endurance = data["Endurance"]
strength = data["Strength"]
dexterity = data["Dexterity"]
intelligence = data["Intelligence"]
faith = data["Faith"]
arcane = data["Arcane"]

client = OpenAI(
api_key = "sk-P2th-cAA47bO2H6iIIGdLd0KNoO4WzTmPJ2P0QUh4rT3BlbkFJDCxQHBNzRAB2fd7LjXYpgkLIRGAK0TV6gsg3leRjkA"
)

prompt = "In Elden Ring, how can I beat " + (boss) + " The following answers should include weapons and items from Elden Ring. \n" + "Weapons from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance " + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "Spells and Incantations from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance "  + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "Armor from Elden Ring: \n"  + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance "  + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "list top three items \n" + "List a Strategy for beating " + (boss) + "\n" + "Now list the strategy for beating this boss from Elden Ring"

chat_completion = client.chat.completions.create(

   messages=[

       {
           "role": "system",
           "content": "You are a list of publicly known weapons, spells and incantations, items, and armor from Elden Ring. Make sure this is printed in JSON format. Make sure to number each weapon, spell/incantation, armor, and item in their respective lists. MAKE SURE EACH PROMPT IS FORMATTED THE EXACT SAME AND DO NOT PRINT THE WORD 'NAME'",
       },

       {
           "role": "system",
           "content": "Weapons: \n [Name of Weapon - 'Requires' Stat Reqiuirement], Spells and Incantations: \n [Name of Spells/Incantations - 'Requires' Stat Requirement], Armor: \n [Name of Armor - 'Requires' Stat Requirement], Items: \n [the list of 3 items], Strategy: \n [paragraph of strategy]",
       },

       {
           "role": "user",
           "content": "Given a Boss from Elden Ring, list the best weapons, armour, and items to use against this boss in order to increase your chance of winning against it.",
       },

       {
           "role": "user",
           "content": prompt
       }

   ],

   model = "gpt-3.5-turbo-1106"

)

print(chat_completion.choices[0].message.content)


# clears the json file for new data
open('chatgpt_output.json', 'w').close()

# saves the API output in a json file
with open('chatgpt_output.json', 'w') as f:
    json.dump((chat_completion.choices[0].message.content), f, indent=4)
