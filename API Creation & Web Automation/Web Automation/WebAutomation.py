from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Opens the browser, navigates to the Flask API's home page, extract the cat fact, and returns the cat fact.
def get_cat_fact() -> str:
    # make sure that the executable_path below points to your Chromedriver installation
    service = Service(executable_path='E:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Visits the Flask application's home page
        driver.get('http://localhost:5000/home')
        # Allow some time for the page to load
        time.sleep(2)
        # Extract the cat fact from the element with id "Cat-Fact"
        cat_fact_element = driver.find_element(By.ID, "Cat_Fact")
        fact_text = cat_fact_element.text
    finally:
        driver.quit()  # make sure that the browser is closed

    return fact_text

# Opens the browser, navigates to the Flask API's breeds page, extract the cat breed, and returns the cat breed.
def get_cat_breed() -> str:
    # make sure that the executable_path below points to your Chromedriver installation
    service = Service(executable_path='E:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        # Visits the Flask application's breeds page
        driver.get('http://localhost:5000/breeds')
        # Allow some time for the page to load
        time.sleep(2)
        # Extract the cat breed from the element with id "Cat-Breed"
        cat_breed_element = driver.find_element(By.ID, "Cat_Breed")
        breed_text = cat_breed_element.text
    finally:
        driver.quit()  # make sure that the browser is closed

    return breed_text


if __name__ == '__main__':
    fact = get_cat_fact()
    print(f"Cat Fact from the Website is: {fact}")

    breed = get_cat_breed()
    print(f"Cat Breed from the Website is: {breed}")
