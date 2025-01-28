import pause
import time
import os
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta, date


def getDriver():
    print("\nInitializing/Checking webdriver....\n")
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.maximize_window
    driver.close()


def NowOrLater():
    print("Would you like to run this script now or at a specified time?")
    print("(1) Now\n(2) Choose a Time")
    choice = input("Waiting for your input... ")
    if choice != "2":
        print("The Script will run now...\nLoading... ")
        Register()
    if choice == "2":
        print("\nChoose a time and date to register (perphaps according to your PRN)\n")

        global year, month, day, hour, minute
        print("Please specify the month, day, and time like your registration opens up")
        year = "2024"
        month = input("month (e.g. 5 for May): ")
        day = input("day: ")
        hour = input("hour (e.g.: 16 for 4:00 PM): ")
        minute = input("minute: ")
        print(
            "The Script will run",
            month + "/" + day + "/" + year,
            "@ " + hour + ":" + minute,
        )
        print("\nPending script execution...\nLeave the Code running...")
        pause.until(
            datetime(int(year), int(month), int(day), int(hour), int(minute), 00)
        )
        Register()


def Register():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver.maximize_window

    print("Opening BlackBoard")
    login_url = "https://bb.ndu.edu.lb/"
    driver.get(login_url)
    print("Completed")

    print("Agreeing to cookies...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "agree_button"))
    ).click()
    print("Completed")

    print("Entering Your Credentials...")
    userID = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "user_id"))
    )
    PIN = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    userID.send_keys(X_number)
    PIN.send_keys(PIN_number)
    print("Completed")

    print("Submiting the form...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "entry-login"))
    ).click()
    print("Completed")

    print("Finding your Assignments and tests...")
    #### DIDN'T FIX IT
    dropdown_button = driver.find_element(By.ID, "filter-stream-value")

    # Click the dropdown button to open the list
    dropdown_button.click()

    # Find the "Assignments and Tests" option (adapt the locator if needed)
    choice = "AssignmentsAndTests"
    assignments_option = (
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//li[@data-filter-type='" + choice + "']")
            )
        )
    ).click()
    print("Completed")


def main():
    week_count()
    getDriver()
    global courses, X_number, PIN_number, semester, PRN, num_of_courses
    """
    DON'T FORGET TO ENTER THE CORRECT CREDENTIALS 
    """
    X_number = "ENTERUSERNAME"
    PIN_number = "ENTERPASSWORD"

    NowOrLater()


def week_count():
    today = date.today()
    week_ago = today - timedelta(days=7)
    print(week_ago)


if __name__ == "__main__":
    main()
