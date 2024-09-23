from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (Make sure to specify the path if not in PATH)
driver = webdriver.Chrome()  # or use webdriver.Firefox(), etc.

# Navigate to your Flask app URL
driver.get("http://127.0.0.1:5000/")

# Loop through the range of numbers
for i in range(1, 100):
    # Generate the item name
    item_name = f"tjtest{i:04d}"

    # Find the input field and fill it
    input_field = driver.find_element(By.NAME, "item_name")
    input_field.clear()  # Clear the input field if necessary
    input_field.send_keys(item_name)

    # Submit the form
    input_field.send_keys(Keys.RETURN)

    # Wait a moment for the page to reload
    time.sleep(1)  # Adjust the delay as necessary

# Optionally, you can close the browser after completion
driver.quit()
