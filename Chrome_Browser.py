import os
from selenium import webdriver
class Chrome_Browser(webdriver.Chrome):
  def __init__(self,executable_path=None,binary_location=None,headless=False,*args,**kwargs):
    if executable_path == None:
      print("Only full paths are supported for the chromedriver")
      os.system("wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_mac64.zip")
      os.system("unzip -a chromedriver_mac64.zip")
      os.system("mv chromedriver ChromeDriver && rm -rf chromedriver_mac64.zip")
      executable_path = os.path.join(os.getcwd(),"ChromeDriver")
    if binary_location == None:
      print("Only full paths are supported for the binary location")
      os.system("wget https://www.slimjet.com/chrome/download-chrome.php?file=files%2F70.0.3538.77%2Fgooglechrome.dmg")
      os.system("""hdiutil attach "download-chrome.php?file=files%2F70.0.3538.77%2Fgooglechrome.dmg" """)
      os.system("sudo cp -r /Volumes/Google\ Chrome/Google\ Chrome.app /Applications/Google\ Chrome\ 70.app")
      os.system("diskutil unmount /Volumes/Google\ Chrome")
      os.remove("download-chrome.php?file=files%2F70.0.3538.77%2Fgooglechrome.dmg")
      binary_location = "/Applications/Google Chrome 70.app/Contents/MacOS/Google Chrome"
    if not os.path.exists("/Applications/Google Chrome 70.app"):
      print("Only full paths are supported for the binary location")
      os.system("wget https://www.slimjet.com/chrome/download-chrome.php?file=files%2F70.0.3538.77%2Fgooglechrome.dmg")
      os.system("""hdiutil attach "download-chrome.php?file=files%2F70.0.3538.77%2Fgooglechrome.dmg" """)
      os.system("sudo cp -r /Volumes/Google\ Chrome/Google\ Chrome.app /Applications/Google\ Chrome\ 70.app")
      os.system("diskutil unmount /Volumes/Google\ Chrome")
      os.remove("download-chrome.php?file=files%2F70.0.3538.77%2Fgooglechrome.dmg")
      binary_location = "/Applications/Google Chrome 70.app/Contents/MacOS/Google Chrome"
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--user-data-dir=~/Library/Application Support/Google/Chrome/Profile Chrome Browser")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-infobars")
    options.binary_location = binary_location
    options.add_argument("--disable-dev-shm-usage")
    if headless:
      options.add_argument('--headless')

    super().__init__(executable_path=executable_path,chrome_options=options,*args,**kwargs)
