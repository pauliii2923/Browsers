import os
from selenium import webdriver
class PhantomJS_Browser(webdriver.PhantomJS):
  def __init__(self,executable_path=None,service_log_path=None,*args,**kwargs):
    if executable_path == None:
      print("Only full paths are supported for the phantomjsdriver")
      os.system("wget 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip'")
      os.system("unzip -a phantomjs-2.1.1-macosx.zip")
      os.system("mv phantomjs-2.1.1-macosx/bin/phantomjs PhantomJS_Driver && rm -rf phantomjs-2.1.1-macosx")
      executable_path = os.path.join(os.getcwd(),"PhantomJS_Driver")
    if not service_log_path:
      service_log_path = os.path.join(os.getcwd(),"PhantomJS_Driver_Log.log")

    super().__init__(executable_path=executable_path,service_log_path=service_log_path,*args,**kwargs)
