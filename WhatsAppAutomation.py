from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the user or group name : ')
msg = input('Enter your message : ')
count = int(input('Enter message count : '))
input('Enter anything after scanning OR code : ')

user = driver.find_element_by_xpath['//span[@title = "{}"]'.format(name)]
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('weEq5')
    button.click()
