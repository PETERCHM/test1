from selenium import webdriver
from selenium.webdriver.common.by import By

# Specify the URL of the login page
login_url = "https://www.cliffsnotes.com/users/log-in"

# Your login credentials
username = "lucynjoka93@gmail.com"
password = "lisa7890"

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get(login_url)

    # Find the email input field by its ID
    email_field = driver.find_element(By.ID, "user_email")

    # Enter the email address
    email_field.send_keys(username)

    # Find the password input field by its ID
    password_field = driver.find_element(By.ID, "user_password")

    # Enter the password
    password_field.send_keys(password)

    # Find the "Log In" button by its attributes and click it
    login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log In']")
    login_button.click()

    # Wait for a few seconds for the login to complete
    driver.implicitly_wait(5)

    # Do further interactions or tasks here as needed

    input("Press Enter to close the browser...")  # Wait for your input before closing the browser

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the browser when you press Enter
driver.quit()
