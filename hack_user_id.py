from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

start_time = time.time()

browser = webdriver.Chrome('C:/chromedriver.exe') # ﻿Путь до драйвера
browser.get('https://stepik.org/lesson/222126/step/5?auth=login&unit=195047')
time.sleep(1)

username = browser.find_element_by_id("id_login_email") #
password = browser.find_element_by_id("id_login_password")

username.send_keys("") ﻿# Логин
password.send_keys("") # Пароль
time.sleep(3)

formBtn = browser.find_element_by_css_selector('.sign-form__btn')
formBtn.click()
time.sleep(3)


df = pd.read_excel('hacker_task.xlsx')
list_of_id = df['ID'].tolist()

for i in list_of_id:
    print(i)
    form = browser.find_element_by_xpath("//input[1]")
    form.send_keys(i)
    time.sleep(2)

    form.send_keys(Keys.RETURN)
    time.sleep(2)

    form = browser.find_element_by_xpath("//input[1]").clear()
    #time.sleep(2)

    i += 1


print("--- %s seconds ---" % (time.time() - start_time))
﻿# Приятного ожидания!