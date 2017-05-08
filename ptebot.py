from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.pearsonvue.com/pte/activity/")
driver.implicitly_wait(10)
login()




# switch to left frame to click Schedule Exams
driver.implicitly_wait(3)
clickScheduleExams()


# tick PTE-A checkbox
driver.implicitly_wait(3)
checkPTEA()

# find closed test center, click search button
driver.implicitly_wait(3)
driver.find_element_by_xpath('//a[@class="noLine"]/img[@alt="Search"]').click()


# select one center by id 


#driver.find_element_by_id('Pearson Professional Centers-Melbourne').click()


#click next button
driver.find_element_by_xpath('//a[@class="noLine"]/img[@alt="Next"]').click()


# driver.close()

def login():
    username = driver.find_element_by_name('loginusername')
    password = driver.find_element_by_name('loginpassword')
    username.send_keys('minozmel')
    password.send_keys('DpG2t5L2e')
    driver.find_element_by_name('submitlogin').click()
    pass

def clickScheduleExams():
    driver.switch_to.frame('WrapSignInNavMenuFrame')
    driver.find_element_by_class_name('link2_off').click()
    driver.implicitly_wait(3)
    driver.switch_to_default_content()
    pass

def checkPTEA():
    driver.switch_to.frame('appsFrame')
    driver.switch_to.frame('RegSchedPageFrame')
    checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]')
    if (not checkbox.is_selected()):
        checkbox.click()
    driver.find_element_by_name('Continue').click()
    pass

def tickAllCenters():
    driver.implicitly_wait(6)
    driver.execute_script('selectCenter("67712")')
    driver.implicitly_wait(6)
    driver.execute_script('selectCenter("75570")')
    driver.implicitly_wait(6)
    driver.execute_script('selectCenter("74481")')
    driver.implicitly_wait(6)
    pass

def loopTestCenters():
    index = 0
    while index < 3:
        for i in range(4):
            radios = driver.find_elements_by_xpath('//div[@id="choosecenter"]//tbody/tr//input')
            radios[i].click()
            driver.implicitly_wait(10)
        print(index)
        index += 1
    else:
        driver.execute_script("alert('done')")

def checkCenter():
    calendar = driver.find_element_by_id('calendar')
    date = calendar.find_elements_by_xpaht('//a[@class="open"]')
    http://selenium-python.readthedocs.io/waits.html?highlight=expected_conditions
