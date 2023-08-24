# Automated-Content-Generator
## Overview
* This project is an Automated Content Generator written in Python language.
* It is a Python automation tool for creating short videos for YouTube Shorts and Instagram Reels.

## Features
* A Python tool to streamline the process of creating short videos for platforms like Instagram and YouTube.
* Integration of Reddit Post Scraping, Text-to-Speech conversion, and Generation of Customized Images/Background Video, resulting in engaging, distinct and dynamic videos.
* Streamlined video creation process with Content Collection, Assembly, and Automatic Upload.
* Implemented Scheduled Upload functionality enabling consistent content sharing (e.g., 1 video every 5 hours), reducing manual effort while maintaining a steady online presence.

## Automation Steps:
* Scraping Reddit posts for content.
* Converting scraped content to text-to-speech audio.
* Generating gameplay background video.
* Creating images (screenshots) of Reddit posts.
* Assembling content into a short video.
* Uploading the final video to YouTube and Instagram.

## Requirements
* [Python](https://www.python.org/downloads/)
* [VS Code (Or Any Other IDE)](https://code.visualstudio.com/download)
* [FFmpeg](https://ffmpeg.org/download.html)
* A Reddit Bot

## Initial Setup
* Install FFmpeg tool from [here](https://ffmpeg.org/download.html). Make sure its included in the environment variables.
* For Linux, you can just type into terminal - ```sudo apt install ffmpeg```
* Setup Reddit Application by following these steps -
  * Goto this [link](https://www.reddit.com/prefs/apps) and click on create application.
  * Fill the details (You can fill anything). Choose "Web App" as application type.
  * Click on Create App and note down the Client_ID, Client_SECRET and Username.
* To use the auto-upload to Instagram feature -
  * Enable 2FA on your Instagram Account and note down the SECRET code.
* To use the auto-upload to Youtube feature -
  * This script uses [Tokland](https://github.com/tokland/)'s [youtube-upload](https://github.com/tokland/youtube-upload) tool to upload the videos to youtube. Check out the repo and set it up.

## Usage
* Clone the repository and open with VS Code (or any other suitable IDE).
* Install Dependencies - 

  ```pip install -r requirements.txt```

* For Linux, install the chromedriver from the following command -

  ```sudo apt install chromium-chromedriver```
  
* Download some videos to use for background and place them in the ```assets/backgrounds``` folder.
* Place your profile_picture in assets folder as ```assets/profile.png```.
* Rename the .env.template file to .env and fill out the details. (Reddit Application details which we obtained earlier & Instagram Account Details)
* Open the config.py file and fill the details as per your discretion.
* Run the script by typing -

  ```python main.py```

## Result
The generated video will be as follows and will automatically be uploaded to Instagram and Youtube.


[Video](https://github.com/aka-nikko/Automated-Content-Generator/assets/54620652/3a9dfd6a-2f1b-4db3-a6e6-4c9621e70b3c)

