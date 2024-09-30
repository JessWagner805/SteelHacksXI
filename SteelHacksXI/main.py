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
api_key = #OpenAI API Key must be added manually.
)

prompt = "In Elden Ring, how can I beat " + (boss) + " The following answers should include weapons and items from Elden Ring. \n" + "Weapons from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance " + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "Spells and Incantations from Elden Ring: \n" + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance "  + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "Armor from Elden Ring: \n"  + "list top three that have stat requirments under " + (vigor) + " vigor " + (mind) + " mind " + (endurance) + " endurance "  + (strength) + " strength " + (dexterity) + " dexterity " + (intelligence) + " intelligence " + (faith) + " faith " + (arcane) + " arcane \n " + "list top three items \n" + "List a Strategy for beating " + (boss) + "\n" + "Now list the strategy for beating this boss from Elden Ring"

chat_completion = client.chat.completions.create(

        response_format = {"type": "json_object"},

   messages=[

       {
           "role": "system",
           "content": "You are a list of publicly known weapons, spells and incantations, consumables, and armor from Elden Ring. Make sure this is printed in JSON format. The name of the weapon and the stat requirements should all be on the same line. No need to include any descriptions. Make sure that the weapons are obtainable before" + (boss),
       },

       {
           "role": "system",
           "content": "Weapons: \n [Name of Weapon - 'Requires' Stat Reqiuirement], Spells and Incantations: \n [Name of Spells/Incantations - 'Requires' Stat Requirement], Armor: \n [Name of Armor - 'Requires' Stat Requirement], Items: \n [the list of 3 consumables], Strategy: \n [paragraph of strategy]",
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

   model = "gpt-4-turbo-2024-04-09"

)

print(chat_completion.choices[0].message.content)


# clears the json file for new data
open('chatgpt_output.json', 'w').close()

# saves the API output in a json file
with open('chatgpt_output.json', 'w') as f:
    json.dump((chat_completion.choices[0].message.content), f, indent=4)
