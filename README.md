# Auto_Web_Logger
Auto_Web_Logger is an automated script designed to handle daily login and logout tasks on web platforms. Using the power of Selenium, it ensures timely and consistent attendance logging without any manual intervention. Additionally, it provides real-time notifications via Telegram about its actions, ensuring you're always informed.

## Features
Automated Login/Logout: Set it up once and let it handle your daily clock-ins and clock-outs.
Telegram Notifications: Receive instant notifications about successful logins, logouts, or any errors.
Time-Based Actions: The script operates based on IST, ensuring timely actions.
Error Handling: In case of any issues, the script gracefully handles errors and ensures you're notified.

## Requirements
Python 3.x
Selenium
Telebot
Chrome Webdriver
pytz

## Configuration
Replace the constants in the code with your specific values. This includes the web link, user ID, password, and other element identifiers.

## Scheduling
This script is designed to be scheduled to run at specific times. You can use platforms like AWS Lambda or PythonAnywhere to schedule the script to run at your desired login and logout times.

## Enjoy!!!
