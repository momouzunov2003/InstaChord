from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def song_bg(song_name):
    options = Options()
    options.add_experimental_option("detach", True)
    options

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

    driver.get("https://www.akordite.com/index.php")
    driver.maximize_window()

    textbox = driver.find_element(By.ID,"mod_search_searchword")
    textbox.send_keys(song_name)
    textbox.send_keys(Keys.RETURN)

    correct_song_name = song_name[0].upper() + song_name[1:]
    print(correct_song_name)

    xpath = f"//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{correct_song_name.lower()}')]"
    link = driver.find_element(By.XPATH, xpath)

    link.click()
