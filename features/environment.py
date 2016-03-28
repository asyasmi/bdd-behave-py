from selenium import webdriver

def before_feature(context, feature):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()

def after_feature(context, feature):
    context.browser.quit()
