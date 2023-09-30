from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the URL of the Quillbot login page
login_url = "https://quillbot.com/login?returnUrl=/"

# Your login credentials
username = "course089@gmail.com"
password = "dddd7890"

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get(login_url)

    # Wait for the email input field to be present
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
    )

    # Enter the email address
    email_field.send_keys(username)

    # Wait for the password input field to be present
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )

    # Enter the password
    password_field.send_keys(password)

    # Wait for the "Log In" button to become clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='login-btn']"))
    )
    login_button.click()

    # You can add explicit waits as necessary to ensure page elements are available
    # for further interactions or tasks on the Quillbot website

    input("Press Enter to close the browser...")  # Wait for your input before closing the browser

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the browser when you press Enter
driver.quit()
