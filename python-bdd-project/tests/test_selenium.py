# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from selenium.webdriver.common.by import By 
# from utilities.selenium_driver import get_driver


# def test_selenium():
#     driver = get_driver()
#     driver.get("https://www.python.org/")
#     driver.maximize_window()
#     assert "Python" in driver.title

#     driver.find_element(By.XPATH, "").click()  # Replace with actual XPath
#     # driver.quit()



from utilities.selenium_driver import get_driver

def test_open_browser():
    driver = get_driver()
    driver.get("https://www.python.org/")
    driver.maximize_window()
    assert "Python" in driver.title
    driver.quit()



