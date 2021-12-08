# добавление комментария
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script('window.scrollBy(0, 600);')
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
driver.find_element_by_css_selector('.post-160 h3').click()
# 4. Нажмите на вкладку "REVIEWS"
driver.find_element_by_css_selector(".reviews_tab > a").click()
# 5. Поставьте 5 звёзд
driver.find_element_by_css_selector("span .star-1").click()
driver.find_element_by_css_selector("span .star-2").click()
driver.find_element_by_css_selector("span .star-3").click()
driver.find_element_by_css_selector("span .star-4").click()
driver.find_element_by_css_selector("span .star-5").click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
driver.find_element_by_id('comment').send_keys("Nice book!")
# 7. Заполните поле "Name"
driver.find_element_by_id("author").send_keys('Ivan Petrov')
# 8. Заполните "Email"
driver.find_element_by_id("email").send_keys('ivapet70@gmail.com')
# 9. Нажмите на кнопку "SUBMIT"
driver.find_element_by_id("submit").click()

driver.quit()