import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from untitled import Ui_Dialog

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)
main_ui = Ui_Dialog()


class WindowClass(QDialog):
    def __init__(self):
        super().__init__()
        main_ui.setupUi(self)
        main_ui.pushButton.clicked.connect(self.button1Function)

    def button1Function(self):
        print("start")
        url = "https://speed.nia.or.kr/index.asp"
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "speed")))
        driver.find_element(By.CLASS_NAME, "speed").click()
        print("go speed page")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "checkAgree")))
        driver.find_element(By.ID, "checkAgree").click()
        print("checkAgree")
        thread = Thread(self)
        thread.start()


class Thread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print("thread")
        wait = main_ui.lineEdit_2.text()
        print("주기" + wait)
        count = main_ui.lineEdit_3.text()
        print("횟수" + count)
        main_ui.progressBar.setMaximum(int(count))
        for i in range(int(count)):
            print("start loop")
            print("goBack")
            main_ui.progressBar.setValue(int(i))
            print(int(i) + 1)
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "goBack")))
            time.sleep(int(wait))
            driver.find_element(By.ID, "goBack").click()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
