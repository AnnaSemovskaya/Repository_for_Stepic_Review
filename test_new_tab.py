from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button=browser.find_element_by_css_selector(".btn-primary")
    button.click()

    newwindow=browser.window_handles[1]
    browser.switch_to.window(newwindow)

    x=browser.find_element_by_id("input_value").text
    value=math.log(abs(12*math.sin(int(x))))

    answer=browser.find_element_by_id("answer")
    answer.send_keys(str(value))

    button=browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла