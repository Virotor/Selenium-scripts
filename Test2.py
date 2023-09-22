import time



from selenium import webdriver 


from selenium.webdriver.common.by import By

def findButtonByName (list, stringButtonName): 
    if(len(list) == 0):
        return 
    else :
        for i in list:
            if(i.text == stringButtonName):
                return i
    return None     








driver = webdriver.Chrome()

time.sleep(2)

driver.get("https://testing.bsuir.by/calculatorkreditov/")

time.sleep(1)

textAreaSum= driver.find_element(By.ID, "desiredSum")

textAreaSum.send_keys("100000")

textAreaMonth= driver.find_element(By.ID, "monthsCount")

textAreaMonth.send_keys("10")

textAreaInterestRate= driver.find_element(By.ID, "interestRate")

textAreaInterestRate.send_keys("10")

buttonCalculate =findButtonByName(driver.find_elements(By.CLASS_NAME, "btn-primary"), "Calculate")

if(buttonCalculate == None):
    print("Exseption button not found")
    driver.quit()
    exit()

buttonCalculate.click()



buttonCalculate =findButtonByName(driver.find_elements(By.CLASS_NAME, "btn-primary"), "Calculate")

# if(textAreaSum.is_enabled and textAreaMonth.is_enabled and textAreaInterestRate.is_enabled):
#     print("Провверка прошла успешно")
# else:
#     print("Проверка прошла неуспешно")    
time.sleep(10)
driver.quit()

   

        

