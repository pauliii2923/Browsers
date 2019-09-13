import os
from Firefox_Browser import Firefox_Browser
from Chrome_Browser import Chrome_Browser
from PhantomJS_Browser import PhantomJS_Browser



# test the firefox browser by navigating to https://google.com and getting a screenshot.
firefox_browser = Firefox_Browser(executable_path=None,firefox_binary=None,firefox_profile=None)
firefox_browser.get("https://google.com")
firefox_browser.save_screenshot("firefox_browser_screenshot.jpg")
firefox_browser.quit()
# test the chrome browser by navigating to https://google.com and getting a screenshot.
chrome_browser = Chrome_Browser(executable_path=None,binary_location=None,headless=True)
chrome_browser = Chrome_Browser(executable_path=os.path.join(os.getcwd(),"ChromeDriver"),binary_location="/Applications/Google Chrome 70.app/Contents/MacOS/Google Chrome",headless=True)
chrome_browser.get("https://google.com")
chrome_browser.save_screenshot("chrome_browser_screenshot.jpg")
chrome_browser.quit()
# test the phantomjs browser by navigating to https://google.com and getting a screenshot.
phantomjs_browser = PhantomJS_Browser(executable_path=None)
phantomjs_browser.get("https://google.com")
phantomjs_browser.save_screenshot("phantomjs_browser_screenshot.jpg")
phantomjs_browser.quit()



# if you specify None for the webdriver fields, they will download the necessary executables and binaries to these default values
firefox_browser = Firefox_Browser(executable_path=os.path.join(os.getcwd(),"Geckodriver"),firefox_binary="/Applications/Firefox 65.app/Contents/MacOS/firefox-bin",firefox_profile=None)
firefox_browser.quit()
chrome_browser = Chrome_Browser(executable_path=os.path.join(os.getcwd(),"ChromeDriver"),binary_location="/Applications/Google Chrome 70.app/Contents/MacOS/Google Chrome",headless=True)
chrome_browser.quit()
phantomjs_browser = PhantomJS_Browser(executable_path=os.path.join(os.getcwd(),"PhantomJS_Driver"))
phantomjs_browser.quit()

