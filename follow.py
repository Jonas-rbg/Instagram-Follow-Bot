import time
from webbot import Browser
import pyautogui 
import win32console,win32gui

class follow():
    
    email = []
    password = []
    
    def __init__(self,filename):
        self.filename = filename

    def readFile(self):
        with open(self.filename) as fp:
            for line in fp:
                file_email,file_passwords = line.split()
                self.email.append(file_email)
                self.password.append(file_passwords)
        
    def hide(self):
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window,0)
        
    def main(self):
        for i in range(0,len(self.email)):
            web = Browser()
            self.hide()
            web.go_to('instagram.com')
            time.sleep(3)
            web.type(self.email[i] , into='Email')
            time.sleep(3)
            web.type(self.password[i], into='Password' , id='passwordFieldId')
            web.click('Log In' , tag='button') 
            time.sleep(3)
            web.go_to('instagram.com/jonas.h24/')
            time.sleep(3)
            web.click('Follow',tag='span')
            time.sleep(2)
            pyautogui.hotkey('alt','f4')

fi = follow("file.txt")
fi.readFile()
fi.main()
