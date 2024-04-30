from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set the window size

# Initialize the driver with the specified options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

def verify_title():
    driver.get("https://www.google.com/")
    title = driver.title
    expected_title = "Google"
    if title == expected_title:
        print("Title verification successful!")
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")
    driver.quit()

if __name__ == "__main__":
    verify_title()



