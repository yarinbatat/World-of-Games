from selenium import webdriver

def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.get(url)
    score_element = driver.find_element_by_id('score')
    score = int(score_element.text)
    driver.quit()
    return 1 <= score <= 1000

def main_function(url):
    if not test_scores_service(url):
        return -1
    return 0



