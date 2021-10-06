from PIL import Image
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

def remove_duplicates_from_list(list_to_dedupe):
    if len(list_to_dedupe) == 0:
        return list_to_dedupe
    return list(dict.fromkeys(list_to_dedupe))

def load_text_lines_from_file(filepath):
    result = []
    with open(filepath, 'r') as f:
        result = f.readlines()
    return result

def check_if_text_file_contains_line(filepath,line):
    result = False
    with open(filepath, 'r') as f:
        if line in f.readlines():
            result = True
    return result

def remove_line_from_text_file(filename,line_to_remove):
    with open(filename, "r+") as f:
        all_lines = f.readlines()
        f.seek(0)
        for line in all_lines:
            if line != line_to_remove:
                f.write(line)
        f.truncate()

def watermark_image(image_path,watermark_path):
    #source: https://stackoverflow.com/a/5324782
    background = Image.open(image_path)
    foreground = Image.open(watermark_path)

    background.paste(foreground, (0, 0), foreground)
    background.save(image_path)

def get_selenium_driver(bool_headless):
    chrome_options = Options()
    if bool_headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument('log-level=3')
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)