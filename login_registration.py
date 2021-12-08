from selenium import webdriver

# ----------------------------------
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# регистрация аккаунта
# 2. Нажмите на вкладку "My Account Menu"
driver.find_element_by_css_selector("[id='menu-item-50'] >a").click()
# 3. В разделе "Register", введите email для регистрации
driver.find_element_by_id('reg_email').send_keys('wel2f@xutc.com')
# 4. В разделе "Register", введите пароль для регистрации
driver.find_element_by_id('reg_password').send_keys('7zxc_QWE0')
# 5. Нажмите на кнопку "Register"
driver.find_element_by_css_selector(".button[name='register']").click()

driver.quit()

# ----------------------------------
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# логин в систему
# 2. Нажмите на вкладку "My Account Menu"
driver.find_element_by_css_selector("[id='menu-item-50'] >a").click()
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
driver.find_element_by_id('username').send_keys('wel2f@xutc.com')
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
driver.find_element_by_id('password').send_keys('7zxc_QWE0')
# 5. Нажмите на кнопку "Login"
driver.find_element_by_css_selector(".button[name='login']").click()
# 6. Добавьте проверку, что на странице есть элемент "Logout"
assert(driver.find_element_by_css_selector("[class*='logout'] > a").text) == "Logout"

driver.quit()