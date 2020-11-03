from RPA.Browser import Browser
import time

browser = Browser()

# in the format of url, name, screenshot_element, screenshot_filename
screenshotURLs = [
    ["https://github.com/Theraghav", "github",
        "//div[@class='js-yearly-contributions']"],
    ["https://forum.uipath.com/u/TheRaga/summary", "uipath-forum",
     "//div[@id='main-outlet']"]
]


def open_the_website(url: str):
    browser.open_available_browser(url)


def store_screenshot(locator: str, filename: str):
    browser.screenshot(locator=locator, filename=filename)

# Define a main() function that calls the other functions in order:


def main():
    for urlInfo in screenshotURLs:
        print(urlInfo)
        try:
            url = urlInfo[0]  # "https://github.com/Theraghav"
            name = urlInfo[1]  # "github"
            # "//div[@class='js-yearly-contributions']"
            screenshot_element = urlInfo[2]
            screenshot_filename = "output/"+name+"-screenshot.png"
            open_the_website(url)
            time.sleep(2) # allow the page to load fully
            store_screenshot(screenshot_element, screenshot_filename)
        finally:
            browser.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
