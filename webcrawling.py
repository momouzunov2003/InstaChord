from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers

def song_bg(song_name):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_extension("./AdBlock.crx")
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

    driver.get("https://www.akordite.com/index.php")
    driver.maximize_window()

    textbox = driver.find_element(By.ID,"mod_search_searchword")
    textbox.send_keys(song_name)
    textbox.send_keys(Keys.RETURN)

    correct_song_name = song_name[0].upper() + song_name[1:]
    print(correct_song_name)

    try:
        link = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT, correct_song_name))
        )
        link.click()
    except Exception:
        print("song not found or error occured while trying to find it")

    current_url = driver.current_url
    driver.quit()
    return current_url

    

def song_en(song_name):
    correct_song_name = helpers.capitalize_after_space(song_name)
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_extension("uBlock-Origin.crx")
    #options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                            options=options)

    driver.get("https://www.ultimate-guitar.com/")
    driver.maximize_window()

    agree_button = driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
    agree_button.click()

    try:
        textbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,'value'))
        )
        textbox.send_keys(correct_song_name)
        textbox.send_keys(Keys.RETURN)
        print("Page loaded successfully!")
    except Exception:
        print("search error")

    try:
        chords_button = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Chords"))
        )
        chords_button.click()
        chords_button.click()
    except Exception:
        print("chords button click error")

    links = driver.find_elements(By.LINK_TEXT,correct_song_name)
    if len(links) <= 1:
        links[0].click()
    else:
        links[1].click()

    try:
        agree_button2 = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME,'css-197f1ny'))
        )
        agree_button2.click()
    except Exception:
        print("second agree button click error")

    source = driver.page_source
    driver.quit()
    return source

