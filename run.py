from selenium import webdriver
import time
from log_info import username, password

browser = webdriver.Firefox()

url = "https://twitter.com/"

browser.get(url)

hashtag = input("Search Hashtag: ")

login_btn = browser.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span")
login_btn.click()

name_input = browser.find_element_by_name("session[username_or_email]")
pass_input = browser.find_element_by_name("session[password]")
log_in = browser.find_element_by_css_selector(".r-jwli3a")

name_input.send_keys(username)
pass_input.send_keys(password)
time.sleep(2)
log_in.click()

src_btn = browser.find_element_by_css_selector(".r-30o5oe")
src_btn.send_keys(hashtag)
src_btn.submit()

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(3)

like_btn = browser.find_elements_by_css_selector(".r-4qtqp9 .r-yyyyoo .r-1xvli5t .r-dnmrzs .r-bnwqim .r-1plcrui .r-lrvibr .r-1hdv0qi")
for like in like_btn:
    try:
        like.click()
    except Exception:
        "Button is not available"

browser.close()
