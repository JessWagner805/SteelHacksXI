import json
from flask import Flask, render_template

app = Flask(__name__)


with open('chatgpt_output.json', 'r') as file:
    data = json.load(file)  

def format_json_data(data):

    if isinstance(data, dict):
        output = ""

       
        output += "<h2>Weapons:</h2><ul>"
        for weapon in data["Weapons"]:
            output += f"<li>{weapon}</li>"
        output += "</ul>"

        
        output += "<h2>Spells and Incantations:</h2><ul>"
        for spell in data["Spells and Incantations"]:
            output += f"<li>{spell}</li>"
        output += "</ul>"

        
        output += "<h2>Armor:</h2><ul>"
        for armor in data["Armor"]:
            output += f"<li>{armor}</li>"
        output += "</ul>"

        
        output += "<h2>Items:</h2><ul>"
        for item in data["Items"]:
            output += f"<li>{item}</li>"
        output += "</ul>"

        
        output += f"<h2>Strategy:</h2><p>{data['Strategy']}</p>"

        return output
    else:
        return "<p>Error: Data is not in dictionary format.</p>"

@app.route('/')
def home():
    
    result = format_json_data(data)

    
    return render_template('output.html', output=result)

if __name__ == '__main__':
    app.run(debug=True)
