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
- TO DO (instert picture of drop down screen)
1. Input your character's numerical stats using the corresponding dropdown options
2. Select the boss you want to defeat
3. Click "Submit"
- TO DO (instert picture of output)
4. AI generated advice and tactics on how to defeat the boss are displayed

## How it Works
![SteelHacksXI](https://github.com/user-attachments/assets/ace829f7-c342-4cdd-ab89-f6c81fe49d73)
- *HTML input:* "app.py" creates a website in which the user inputs their stats and chooses a boss
- *userInput.json:* based on the user's input, a json file named "boss_helper_data.json" is created
- *main.py:* "main.py" reads through the user input and enters it into ChatGPT API
- *output.json:* based on ChaptGPT's output, a json file named "chatgpt_output.json" is created
- *HTML output:* the information from "chatgpt_output.json" is output to the website for the user to view

## Video Demonstration
TO DO
(insert screen recording of website running)
