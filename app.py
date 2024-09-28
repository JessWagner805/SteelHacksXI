from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data from the request
    vigor = request.form['vig']
    mind = request.form['mind']
    endurance = request.form['end']
    strength = request.form['str']
    dexterity = request.form['dex']
    intelligence = request.form['int']
    faith = request.form['fth']
    arcane = request.form['arc']
    selected_boss = request.form['Boss']

    # Convert form data to a Python dictionary
    user_data = {
        "Vigor": vigor,
        "Mind": mind,
        "Endurance": endurance,
        "Strength": strength,
        "Dexterity": dexterity,
        "Intelligence": intelligence,
        "Faith": faith,
        "Arcane": arcane,
        "Selected Boss": selected_boss
    }

    # Write the data to a JSON file
    with open('boss_helper_data.json', 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    return jsonify(user_data)  # Return the data as JSON response

if __name__ == '__main__':
    app.run(debug=True)