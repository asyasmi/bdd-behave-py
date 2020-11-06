import os
import time
import logging
from selenium import webdriver
from behave.log_capture import capture

GRID_HUB_URL = os.environ.get('GRID_HUB_URL')
RUNTIME_DIR = os.path.join(
    os.path.abspath(
        os.path.join(
            __file__, os.pardir, os.pardir,
            'runtime', time.strftime('%d.%m.%Y - %R')
        )
    )
)
SCR_EXT = '.png'


def before_all(context):
    if GRID_HUB_URL is None:
        context.browser = webdriver.Chrome()
    else:
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        context.browser = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor=GRID_HUB_URL
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
