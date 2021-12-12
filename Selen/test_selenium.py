from selenium import webdriver


def test_planet_for_me():
    driver = webdriver.Chrome()
    driver.get('https://planetfor.me')
    button = driver.find_element_by_xpath('//*[@id="page-507"]/div/div[4]/div/a')
    button.click()
    title = driver.find_element_by_css_selector('#__layout > div > div.pfm-container.mg-lr-auto.pd-tb-20 > '
                                                'div:nth-child(2) > '
                                                'div.pfm-card.pfm-theme_white.b-rad-20-0.pd-20-25-0 > '
                                                'div.font-semi-22.mg-top-15').text
    assert title == 'КРЫМ'
