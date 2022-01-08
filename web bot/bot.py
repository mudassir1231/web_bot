from selenium import webdriver

drive = webdriver.Chrome(executable_path="C:\\python\\web bot\\chromedriver.exe")


drive.get('https://www.google.com')
drive.implicitly_wait(4)
searchbox = drive.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
searchbox.send_keys("xhamster")
searchbox.submit()

# searchclick = drive.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchclick.click()
