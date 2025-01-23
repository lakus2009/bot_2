from selenium  import webdriver
from selenium.webdriver.common.by import By


main_url = 'https://www.tazabek.kg/lenta/page:1'
# chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome()
driver.get(main_url)
elements = driver.find_elements(By.XPATH, "//div[@class='lenta-row-title']" )


urls = []
for element in elements:
    title =  element.find_element(By.XPATH, './/a').get_attribute('href')
    urls.append(title)

for url in urls:
    driver.get(url)
    title = driver.find_element(By.XPATH, "//h2[@class='title']").text
    article = driver.find_element(By.XPATH, "//div[@class='text']").text
    time = driver.find_element(By.XPATH, "//span[@class='date']").text




    with open('tazabek_3.py', 'a') as t:
        t.write(f'url: {url}\n')
        t.write(f'Time: {time}\n')
        t.write(f'title: {title}\n')
        t.write(f'article: {article}\n')
        t.write(('-'*40 + '\n'))