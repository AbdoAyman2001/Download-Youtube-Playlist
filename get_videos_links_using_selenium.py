from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')

def get_videos_links_of_playlist(link):
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    a_tags = driver.find_elements_by_css_selector("a#video-title")
    links = [a_tag.get_attribute('href') for a_tag in a_tags]
    driver.quit()
    return links