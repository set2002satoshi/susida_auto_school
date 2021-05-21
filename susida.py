from selenium import webdriver
import chromedriver_binary
import pyautogui as pgui 
from PIL import Image
from time import sleep
import datetime 

import pyocr
import pyocr.builders

driver = webdriver.Chrome()

driver.maximize_window()

# # OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)
 # クリックする前にロード時間待機
sleep(5)
# スタート画面
pgui.click(x=679, y=540)

sleep(3)

# １千円コース
# pgui.click(x=794, y=427)
# 5千円
# pgui.click(x=710, y=508)
# # これは１万円コース
pgui.click(x=697, y=573)


sleep(3)
tools = pyocr.get_available_tools()
tool = tools[0]
builder = pyocr.builders.TextBuilder(tesseract_layout=6)

a = []
pclle = '/Users/wed2110258/Desktop/susida/satoshi.png'

pgui.FAILSAFE = True

def screenshot_system(imgpath):
    # 3000￥コース用
    # sc = pgui.screenshot(region=(1260,1000,300,55))

    sc = pgui.screenshot(region=(1150,1000,600,55))
    sc.save(imgpath)

 

for _ in range(340):

    screenshot_system(pclle)
    image = Image.open(pclle)
    result = tool.image_to_string(image, lang="eng", builder=builder)
    print(result)


    pgui.typewrite(result)
    sleep(0.2)

print('end')


