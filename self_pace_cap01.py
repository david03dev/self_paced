#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

wait = WebDriverWait(driver,10)


def test_case_01():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys("admin")

    password = "admin123"
    wait.until(EC.presence_of_element_located((By.NAME,"password"))).send_keys(password)

    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    login_btn.click()

    confirmation_status = wait.until(EC.visibility_of_element_located((By.XPATH,
                                    "//span[@class='oxd-topbar-header-breadcrumb']//h6[text()='Dashboard']"))).text

    assert "Dashboard" in confirmation_status, "TC_01 Failed"
    if "Dashboard" in confirmation_status:
        print("TC_01 passed ")
    else:
        print("TC_01 failed")
"""
def Test_case_02():
    print("Test_02 is under construction")

#call test case 01
Test_case_01()

#call test case 02
Test_case_02()


driver.quit()

"""