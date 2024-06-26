import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from openai_gpt import generate_response as gpt

#settings
site = "https://www.ixl.com/math/algebra-1/solve-a-quadratic-equation-by-completing-the-square"
user = os.environ['user']
password = os.environ['password']

#setup
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')  #remove if memory not an issue

#load page without popup
driver = webdriver.Chrome(options=options)
driver.get(site)
#wait = WebDriverWait(driver, 10)
driver.get(site)

wait = WebDriverWait(driver, 5)

#login
try:
    username_field = driver.find_element(By.ID, 'qlusername')
    username_field.send_keys(user)

    password_field = driver.find_element(By.ID, 'qlpassword')
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, 'qlsudbmit') 
    login_button.click()
    
except Exception as e:
  print("Error entering credentials or wrong IDs:", e)
  driver.quit()

#get problem
time.sleep(3)
problem_class = driver.find_element(By.CLASS_NAME, 'math')
visible_text = problem_class.text
print(visible_text)

#send to chatgpt
try:
  context = "You are answering a math problem on IXL. Only respond with your answer when responding, it is important that you do not respond with any other text. This includes part of the problem. If you have something like x= and the answer is x=-5, only respond -5. Only ever use a comma if you have mutliple answers, an you need to seperate them. For example a quadratic has two answers. If you have to tpye an equation, use keys that are often used to display an operation. For example, if you have to type division use / or ^ for exponents. To decode the problem, the text given below is the html or js code, decode it for the problem."
  response=gpt(context,visible_text)
  print(response)
except Exception as e:
  print("Error generating response", e)
  driver.quit()

while True:
  try:
    time.sleep(2)
  except EOFError:
    driver.quit()
    break