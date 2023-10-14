import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telebot

# Load environment variables
load_dotenv()
TOKEN = os.getenv('API_KEY')
GROUP_ID = os.getenv('GROUP_ID')
WEB_LINK = os.getenv('WEB_LINK')
USER_ID = os.getenv('USER_ID')
PASSWORD = os.getenv('PASSWORD')
USER_ID_ELEMENT = os.getenv('USER_ID_ELEMENT')
PASSWORD_ELEMENT = os.getenv('PASSWORD_ELEMENT')
LOGIN_ELEMENT = os.getenv('LOGIN_ELEMENT')

# Telegram bot setup
bot = telebot.TeleBot(TOKEN)

def get_current_timestamp_and_hour() -> tuple[str, int]:
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    ist_now = utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
    current_timestamp = ist_now.strftime('%Y-%m-%d %H:%M:%S')
    current_hour = ist_now.hour
    return current_timestamp, current_hour

def determine_action(current_hour):
    if 1 <= current_hour < 14:
        return "Clocked out"
    return "Clocked in"

def send_telegram_message(message):
    k_button = telebot.types.InlineKeyboardButton(text='Kredily', url=WEB_LINK)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(k_button)
    bot.send_message(chat_id=GROUP_ID, text=message, reply_markup=keyboard)

def setup_webdriver():
    os.chdir('..')
    os.chdir('chromedriver')
    folder = os.getcwd()
    path = os.path.join(folder, 'chromedriver.exe')
    webdriver.Chrome.chromedriver_binary = path
    return webdriver.Chrome()

def main():
    driver = setup_webdriver()
    current_timestamp, current_hour = get_current_timestamp_and_hour()
    action = determine_action(current_hour)

    try:
        # Navigate to the web link
        driver.get(WEB_LINK)
        
        # Wait for the login fields to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, USER_ID_ELEMENT)))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, PASSWORD_ELEMENT)))

        # Find the login fields and enter the credentials
        user_id_elem = driver.find_element(By.ID, USER_ID_ELEMENT)
        password_elem = driver.find_element(By.ID, PASSWORD_ELEMENT)
        
        user_id_elem.send_keys(USER_ID)
        password_elem.send_keys(PASSWORD)
        password_elem.send_keys(Keys.RETURN)  # Press Enter to login

        # Wait for the button to be clickable after logging in
        button_elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, LOGIN_ELEMENT)))
        button_elem.click()

        # Send success message
        send_telegram_message(f"Successfully {action} in Kredily at {current_timestamp}")       

    except Exception as e:
        # Send failure message with the error
        send_telegram_message(f"Failed {action} in Kredily at {current_timestamp}. Error: {str(e)}")

    finally:
        driver.quit()

if __name__ == '__main__':
    main()
