
"""
Created on Tue May 26 16:46:40 2020

@author: kgleeson

v1
Currently takes ~ 1min 15s to run

Program first logs into Virgin Pulse. 
Then, selects got it on cards to get points. 
Then, it proceeds to enter in daily health stats on healthy habits.
"""

#Automate annoying Virgin Pulse data entry to get my $400

#import Selenium and import the webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome('C:\\Users\\kgleeson\\Documents\\Python Scripts\\chromedriver')
type(browser)

#Go to virgin pulse
browser.get('https://iam.virginpulse.com')

#enter username
time.sleep(2)
user_name = browser.find_element_by_id('username')
user_name.send_keys('')

# Enter password
pword = browser.find_element_by_id('password')
pword.send_keys('')

pword.send_keys(Keys.ENTER)




time.sleep(15)

try:
    button = browser.find_element_by_class_name('next-card-btn')
    button.send_keys(Keys.ENTER)
except:
    pass



#Click got it on second card
try:
    card = browser.find_element_by_id('triggerCloseCurtain')
    card.click()
except:
    pass

#Click next again
try:
    button.click()
except:
    pass
#Click Got it
try:
    card.click()
except:
    pass
#Go to tracking


tracking = browser.find_element_by_id('core-menuitem-tracking-title')
tracking.click()

time.sleep(5)
#zoom out



#Click yes everywhere
time.sleep(5)

drink = browser.find_element_by_id('tracker-652-track-yes')
workout = browser.find_element_by_id('tracker-683-track-yes')
exercise = browser.find_element_by_id('tracker-687-track-yes')
stairs = browser.find_element_by_id('tracker-13-track-yes')
breakfast = browser.find_element_by_id('tracker-44-track-yes')

popup=browser.find_element_by_tag_name('html')

drink.send_keys(Keys.ENTER)
time.sleep(10)
popup.send_keys(Keys.ESCAPE)

time.sleep(5)
workout.send_keys(Keys.ENTER)
time.sleep(5)
popup.send_keys(Keys.ESCAPE)

exercise.send_keys(Keys.ENTER)
time.sleep(5)
popup.send_keys(Keys.ESCAPE)

stairs.send_keys(Keys.ENTER)
time.sleep(5)
popup.send_keys(Keys.ESCAPE)

breakfast.send_keys(Keys.ENTER)
time.sleep(5)
popup.send_keys(Keys.ESCAPE)


    

#Enter Weight
weight = browser.find_element_by_id('healthyhabits-weightinput')
weight.send_keys('170')

weight.send_keys(Keys.ENTER)



time.sleep(3)
#Enter Sleep
sleep = browser.find_element_by_id('sleepHours')
sleep.send_keys('8')

sleep.send_keys(Keys.ENTER)


#Select Mood
mood = browser.find_element_by_class_name('mood-icon-button5')
mood.click()




#Exit browser
browser.quit()
