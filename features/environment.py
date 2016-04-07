from selenium import webdriver


def before_feature(context, feature):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()


def after_step(context, step):
    if step.status == "failed":
        screenshot = context.scenario.name + " - " + step.name + ".png"
        context.browser.save_screenshot(screenshot)
        print("Screenshot saved to file: %s" % screenshot)


def after_feature(context, feature):
    context.browser.quit()
