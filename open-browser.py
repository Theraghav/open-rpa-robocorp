from RPA.Browser import Browser
import time

browser = Browser()

# in the format of url, name, screenshot_element, screenshot_filename
screenshotURLs = [
    ["https://github.com/Theraghav", "github",
        "//div[@class='js-yearly-contributions']"],
    ["https://forum.uipath.com/u/TheRaga/summary", "uipath-forum",
     "//div[@id='main-outlet']"],
    ["https://stackoverflow.com/users/4581293/raga?tab=topactivity", "stackoverflow",
     "//div[@id='top-cards']"],
    ["https://university.mongodb.com/certified_professional_finder/certified_professionals/828741", "mongo-dev-profile",
     "//div[@class='css-i9gxme e1p474gp5']"],
    ["https://www.certmetrics.com/uipath/public/badge.aspx?i=1&t=c&d=2020-11-09&ci=UIP00133845", "uiPath-cert",
        "//div[@id='prevDivPublic']"],
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
            name = urlInfo[1]  # "github" # "//div[@class='js-yearly-contributions']"
            screenshot_element = urlInfo[2]
            screenshot_filename = "output/"+name+"-screenshot.png"
            open_the_website(url)
            time.sleep(2)  # allow the page to load fully
            store_screenshot(screenshot_element, screenshot_filename)
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst)
            print('Could not get screenshot for '+name)
        finally:
            browser.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
