import webbrowser
import json

PATH_JS = "/home/pio/Desktop/cogrob/cogrob_ws/src/web_service/src/json/pearson.js"
PATH_HTML = "file:///home/pio/Desktop/cogrob/cogrob_ws/src/web_service/src/html/index.html"

def load_url():
    

    browser= webbrowser.get('firefox')
    browser.open(PATH_HTML)
