import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
class Firefox_Browser(webdriver.Firefox):
  def __init__(self,executable_path=None,firefox_binary=None,firefox_profile=None,*args,**kwargs):
    if executable_path == None:
      print("Only full paths are supported for the geckodriver")
      os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-macos.tar.gz")
      os.system("tar -xvzf geckodriver-v0.24.0-macos.tar.gz && rm -rf geckodriver-v0.24.0-macos.tar.gz")
      os.system("mv geckodriver Geckodriver")
      executable_path = os.path.join(os.getcwd(),"Geckodriver")
    if firefox_binary == None:
      print("Only full paths are supported for the binary location")
      os.system("wget https://ftp.mozilla.org/pub/firefox/releases/65.0/mac/en-US/Firefox%2065.0.dmg")
      os.system("""hdiutil attach "Firefox 65.0.dmg" """)
      os.system("sudo cp -r /Volumes/Firefox/Firefox.app /Applications/Firefox\ 65.app")
      os.system("diskutil unmount /Volumes/Firefox")
      os.remove("Firefox 65.0.dmg")
      firefox_binary = "/Applications/Firefox 65.app/Contents/MacOS/firefox-bin"
      firefox_binary = FirefoxBinary(firefox_binary)
    if not os.path.exists("/Applications/Firefox 65.app"):
      print("Only full paths are supported for the binary location")
      os.system("wget https://ftp.mozilla.org/pub/firefox/releases/65.0/mac/en-US/Firefox%2065.0.dmg")
      os.system("""hdiutil attach "Firefox 65.0.dmg" """)
      os.system("sudo cp -r /Volumes/Firefox/Firefox.app /Applications/Firefox\ 65.app")
      os.system("diskutil unmount /Volumes/Firefox")
      os.remove("Firefox 65.0.dmg")
      firefox_binary = "/Applications/Firefox 65.app/Contents/MacOS/firefox-bin"
      firefox_binary = firefox_binary
    if firefox_profile == None:
      print("Only full paths are supported for the profile path")
      os.system("/Applications/Firefox\ 65.app/Contents/MacOS/firefox-bin -CreateProfile 'Profile_Firefox_Browser'")
      firefox_profile = FirefoxProfile(os.path.join(os.path.expanduser("~/Library/Application Support/Firefox/Profiles"),[i for i in os.listdir(os.path.expanduser("~/Library/Application Support/Firefox/Profiles")) if i.endswith("Profile_Firefox_Browser")][0] ))
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv; charset=utf-8')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/json; charset=utf-8')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/json')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain; charset=utf-8')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/html; charset=utf-8')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/html')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'attachment/json; charset=utf-8')
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'attachment/json')

    super().__init__(executable_path=executable_path,firefox_binary=firefox_binary,firefox_profile=firefox_profile)
