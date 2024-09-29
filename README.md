# Elden Ring Boss Helper
*By: Natalie Goldsworthy, Pearl Singer, Luke Tola, and Jessica Wagner*
### Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [How to Use](#how-to-use)
- [How it Works](#how-it-works)
- [Video Demonstration](#video-demonstration)

## Overview
This program allows users to select a boss in *Elden Ring* and input their in-game stats. Based on these inputs, the program utilizes AI to provide tailored strategies and advice on how to defeat the selected boss.

## Purpose
Defeating bosses in *Elden Ring* can be challenging, and having non-ideal stats can make it even more difficult to develop an effective strategy. The purpose of this website is to provide users with effective tactics and advice for overcoming specific bosses based on their current character build and stats.

## How to Use
![Screenshot 2024-09-28 230241](https://github.com/user-attachments/assets/4142211e-88b0-4cb0-a03b-511cdad5c54d)
1. Input your character's numerical stats using the corresponding dropdown options
2. Select the boss you want to defeat
3. Click "Submit"
- ![image](https://github.com/user-attachments/assets/e5301adc-773e-461c-b832-a7838d78f690)
4. Ideally, the AI generated advice and tactics on how to defeat the boss are displayed on this page
   - Note: in this version, this information is printed in the terminal due to time constraints
![image](https://github.com/user-attachments/assets/a1b0f1fb-c27e-4a20-bdf3-0bd39fb01c53)


## How it Works
![SteelHacksXI](https://github.com/user-attachments/assets/ace829f7-c342-4cdd-ab89-f6c81fe49d73)
- *HTML input:* "app.py" creates a website in which the user inputs their stats and chooses a boss
- *userInput.json:* based on the user's input, a json file named "boss_helper_data.json" is created
- *main.py:* "main.py" reads through the user input and enters it into ChatGPT API
- *output.json:* based on ChaptGPT's output, a json file named "chatgpt_output.json" is created
- *HTML output:* "test.py" reads through the information from "chatgpt_output.json" and would ideally output it to the website for the user to view. However in this version, the information is output to the terminal.

## Video Demonstration
**TO DO**
(insert screen recording of website running)
