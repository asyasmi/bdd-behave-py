from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()