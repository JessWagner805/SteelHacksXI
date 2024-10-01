# Elden Ring Boss Helper
*By: Natalie Goldsworthy, Pearl Singer, Luke Tola, and Jessica Wagner*
### Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [How to Use](#how-to-use)
- [How it Works](#how-it-works)
- [[UPDATED] Video Demonstration](#[UPDATED]-video-demonstration)
- [Devpost Submission](#devpost-submission)

## Overview
This program allows users to select a boss in *Elden Ring* and input their in-game stats. Based on these inputs, the program utilizes AI to provide tailored strategies and advice on how to defeat the selected boss.

## Purpose
Defeating bosses in *Elden Ring* can be challenging, and having non-ideal stats can make it even more difficult to develop an effective strategy. The purpose of this website is to provide users with effective tactics and advice for overcoming specific bosses based on their current character build and stats.

## How to Use
- ![InputUpdated](https://github.com/user-attachments/assets/13d7f8c6-0764-4aed-839b-3c5c83629903)
1. Input your character's numerical stats using the corresponding dropdown options
2. Select the boss you want to defeat
3. Click "Submit"
- ![image](https://github.com/user-attachments/assets/5734a218-d39a-4239-b85a-2a013a67e0fc)
4. The AI generated advice and tactics on how to defeat the boss are displayed on this page

## How it Works
![SteelHacksXI](https://github.com/user-attachments/assets/ace829f7-c342-4cdd-ab89-f6c81fe49d73)
- *HTML input:* "app.py" creates an HTML page in which the user inputs their stats and chooses a boss
- *userInput.json:* based on the user's input, a json file named "boss_helper_data.json" is created
- *main.py:* "main.py" reads through the user input and enters it into ChatGPT API
- *output.json:* based on ChaptGPT's output, a json file named "chatgpt_output.json" is created
- *HTML output:* "test.py" reads through the information from "chatgpt_output.json" and outputs it to the HTML page for the user to view

## [UPDATED] Video Demonstration
[https://youtu.be/Y8o7C-Nmwi0](https://youtu.be/Y9nmaMEY8xc)

## Devpost Submission
https://devpost.com/software/elden-ring-boss-helper
