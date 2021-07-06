import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver

from parse_flyer_json import parse_json_as_items

import sys
for p in sys.path:
    print(p)

firefox_path = '/Applications/Firefox.app/Contents/MacOS/firefox'
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# binary = FirefoxBinary(firefox_path)
# driver = webdriver.Firefox(firefox_binary=binary)

options = Options()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.saveonfoods.com/circular")


def find_flyer_data():
    flyer_json = None
    for r in driver.requests:
        if not r.response:
            continue
        if 'flyer_data' in r.url:
            rtype = r.response.headers['Content-Type']
            rstatus = r.response.status_code
            # print(rstatus, r.url, rtype)
            flyer_json = r.response.body
            break

    return flyer_json


flyer_json = find_flyer_data()
driver.close()

items = parse_json_as_items(flyer_json)

for i in items:
    print(f'{i.price!r:7}  {i.name}')
