from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the URL of the StudyPool login page
login_url = "https://www.studypool.com/documents/5422518/login"

# Your login credentials
username = "lisa089"
password = "west7890"

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get(login_url)

    # Wait for the "Login" link to be present
    login_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Login')]"))
    )

    # Click the "Login" link using JavaScript
    driver.execute_script("arguments[0].click();", login_link)

    # Wait for the username input field to be present
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "UserLogin_username"))
    )

    # Enter the username
    username_field.send_keys(username)

    # Wait for the password input field to be present
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "UserLogin_password"))
    )

    # Enter the password
    password_field.send_keys(password)

    # Find and click the "Login" button
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    # You can add explicit waits as necessary to ensure page elements are available
    # for further interactions or tasks on the StudyPool website

    input("Press Enter to close the browser...")  # Wait for your input before closing the browser

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the browser when you press Enter
driver.quit()
