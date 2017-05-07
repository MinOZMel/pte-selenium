
from splinter import Browser

b = Browser()

url="http://pearsonpte.com/book/"


b.visit(url)

b.click_link_by_text('Sign in now')



window = b.windows[0]

b.windows.current = window.next

print(b.url)

if b.status_code.is_success():
    if b.is_element_present_by_name('loginusername',10):
        b.find_by_name('loginusername').fill('minozmel')
    else:
        print('didn'' find username')
    if b.is_element_present_by_name('loginpassword',10):
        b.find_by_name('loginpassword').fill('DpG2t5L2e')
else:
    print('didn''t find password')

loginusername = b.find_by_name('loginusername')
loginpassword = b.find_by_name('loginpassword')

if(loginusername.value == 'minozmel'):
    b.find_by_name('submitlogin').click()

if b.status_code.is_success():
    if b.is_element_present_by_text('Schedule Exams',10):
        b.find_by_text('Schedule Exams').click()
        b.fi

print(b.url)
