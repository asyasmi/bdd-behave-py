import os
import logging
from selenium import webdriver
from behave.log_capture import capture

RUNTIME_DIR = os.path.join(
    os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'runtime')))
SCR_EXT = '.png'


def before_all(context):
    # context.browser = webdriver.Firefox()
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['version'] = 'latest'
    desired_capabilities['platform'] = 'LINUX'
    desired_capabilities['name'] = 'Testing Selenium with Behave'

    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://localhost:4444/wd/hub"
    )
    context.browser.maximize_window()


@capture
def after_step(context, step):
    if step.status == "failed":
        if not os.path.exists(RUNTIME_DIR):
            os.mkdir(RUNTIME_DIR)
        screenshot = os.path.join(
            RUNTIME_DIR, context.scenario.name + " - " + step.name + SCR_EXT)
        context.browser.save_screenshot(screenshot)
        logging.error("Screenshot saved to file: %s" % screenshot)


def after_feature(context, feature):
    context.browser.quit()
