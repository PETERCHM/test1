# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a function to automate Turnitin
def automate_turnitin():
    # Create a WebDriver instance for Firefox
    driver = webdriver.Chrome()

    # Function to remove the top <span> element
    def remove_top_span():
        js_code = """
        var topSpan = document.getElementById("top_nav");
        if (topSpan) {
            topSpan.remove();
        }
        """
        driver.execute_script(js_code)

    # Step 3: Automate the Login Process
    login_url = "https://www.turnitin.com/login_page.asp?lang=en_us"
    driver.get(login_url)

    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "user_password")

    email = "lucynjoka53@gmail.com"  # Replace with your email
    password = "KEnya@4567890"  # Replace with your password

    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the login to complete (adjust the timeout as needed)
    try:
        WebDriverWait(driver, 1000).until(EC.url_contains("t_home.asp"))  # Check if URL contains a specific part of the URL
    except Exception as e:
        print("Login failed:", str(e))
        driver.quit()
        exit()

    # Step 4: Access Turnitin Pages
    class_home_url = "https://www.turnitin.com/t_home.asp?login=1&svr=6&lang=en_us&r=73.1424157141831"
    driver.get(class_home_url)

    # Remove the top <span> element (if it exists) on each page
    while True:
        remove_top_span()

        time.sleep(1)  # You need to import the time module



# Call the function to automate Turnitin
automate_turnitin()
