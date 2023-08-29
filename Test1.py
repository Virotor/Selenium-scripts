import time

from selenium import webdriver 


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


time.sleep(5)


driver.get("https://testing.bsuir.by/")
time.sleep(5)

textareaFirst= driver.find_element(By.LINK_TEXT, "Калькулятор меню")
textareaSecond = driver.find_element(By.LINK_TEXT, "Аптека")
textareaThird= driver.find_element(By.LINK_TEXT, "Калькулятор кредитов")





time.sleep(5)

if(textareaFirst.is_enabled and textareaSecond.is_enabled and textareaThird.is_enabled):
    print("Провверка прошла успешно")
else:
    print("Проверка прошла неуспешно")    

driver.quit()
