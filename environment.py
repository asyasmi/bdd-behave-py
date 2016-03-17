from selenium import webdriver

def after_feature(context, feature):
    context.browser.quit()
