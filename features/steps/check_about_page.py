from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("user clicks on link with text '{text}'")
def user_clicks_on_link_with_text(context, text):
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[contains(text(), "%s")]' % text))
    )

    element = context.browser.find_element_by_xpath(
        '//a[contains(text(), "%s")]' % text)

    element.click()


@then("user see a text '{text}'")
def page_include_text(context, text):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath(
        '//*[contains(text(), "%s")]' % text)

