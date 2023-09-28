import time
from selenium import webdriver 
from selenium.webdriver.common.by import By



def findButtonByName (list : [], stringButtonName : str): 
    if(len(list) == 0):
        raise Exception("List is empty")
    else :
        for elem in list:
            if(elem.text == stringButtonName):
                return elem
    return None     

def checkResultElement(list : [], stringNameElement : str):

    if(len(list) == 0):
        raise Exception("List is empty")
    for elem in list:
        if(deleteComma(elem.text) == stringNameElement):
            return True       
    return False

def deleteComma ( string : str ):
    return string.replace(',','')


def calculateCredit(mouthsCount : float, desiredSum : float, interestRate : float): 
    result = []
    result.append(desiredSum * (1+(interestRate/100) * (mouthsCount/12)))
    result.append(result[0] / mouthsCount)
    return result



    

driver = webdriver.Chrome()

time.sleep(2)

driver.get("https://testing.bsuir.by/calculatorkreditov/")

time.sleep(1)


mounthsCount = 20
desiredSum = 10000
interestRate = 10

textAreaSum= driver.find_element(By.ID, "desiredSum")

textAreaSum.send_keys(str(desiredSum))

textAreaMonth= driver.find_element(By.ID, "monthsCount")

textAreaMonth.send_keys(str(mounthsCount))

textAreaInterestRate= driver.find_element(By.ID, "interestRate")

textAreaInterestRate.send_keys(str(interestRate))

try: 
    buttonCalculate =findButtonByName(driver.find_elements(By.CLASS_NAME, "btn-primary"), "Calculate")
except Exception as error:
    print ('Calculate button exception: ', error)
    driver.quit()
    exit()

    

buttonCalculate.click()
try:
    calculateResult = calculateCredit(mounthsCount, desiredSum, interestRate )
except Exception as error: 
    print ('Result  exception: ', error)
    driver.quit()
    exit()


resultMounth = round(calculateResult[1], 3)
totalResult = round(calculateResult[0], 3)


if(checkResultElement(
    driver.find_elements(
        By.TAG_NAME, "div"),
        'Calculate\nMonthly charge:\n'+ str(resultMounth) + '\nTotal sum:\n'+ str(totalResult))
    ):
    print("Проверка прошла успешно")
else:
    print("Проверка прошла неуспешно")    
time.sleep(1)
driver.quit()

   

        

