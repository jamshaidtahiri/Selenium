#generate list from file with links
def get_list(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By

profile = webdriver.FirefoxProfile(
    '/home/mjt/.mozilla/firefox/9jel9qq6.default-release-1659994392619')

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)





list_file = "channel_list.txt"   #file name in current location
link_list=get_list(list_file)
for link in link_list:
    driver.get(link)
    driver.implicitly_wait(30)
    try:
       login = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string")

       login.click()
    except NoSuchElementException:
        pass

#driver.quit()

