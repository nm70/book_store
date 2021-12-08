import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------------------------
# отображение страницы товара
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# 2. Залогиньтесь
driver.find_element_by_css_selector("[id='menu-item-50'] >a").click()
driver.find_element_by_id('username').send_keys('wel2f@xutc.com')
driver.find_element_by_id('password').send_keys('7zxc_QWE0')
driver.find_element_by_css_selector(".button[name='login']").click()
# 3. Нажмите на вкладку "Shop"
driver.find_element_by_id('menu-item-40').click()
# 4. Откройте книгу "HTML 5 Forms"
driver.find_element_by_css_selector('.post-181').click()
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
assert(driver.find_element_by_css_selector('[id="product-181"] h1').text) == "HTML5 Forms"

driver.quit()


# ------------------------------------
# количество товаров в категории
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# 2. Залогиньтесь
driver.find_element_by_css_selector("[id='menu-item-50'] >a").click()
driver.find_element_by_id('username').send_keys('wel2f@xutc.com')
driver.find_element_by_id('password').send_keys('7zxc_QWE0')
driver.find_element_by_css_selector(".button[name='login']").click()
# 3. Нажмите на вкладку "Shop"
driver.find_element_by_id('menu-item-40').click()
# 4. Откройте категорию "HTML"
driver.find_element_by_css_selector('.cat-item-19 > a').click()
# 5. Добавьте тест, что отображается три товара
assert(len(driver.find_elements_by_css_selector('.product'))) == 3, 'отображается не три товара'

driver.quit()


# ------------------------------------
# сортировка товаров
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2. Залогиньтесь
driver.find_element_by_css_selector("[id='menu-item-50'] >a").click()
driver.find_element_by_id('username').send_keys('wel2f@xutc.com')
driver.find_element_by_id('password').send_keys('7zxc_QWE0')
driver.find_element_by_css_selector(".button[name='login']").click()
# 3. Нажмите на вкладку "Shop"
driver.find_element_by_id('menu-item-40').click()
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
assert(driver.find_element_by_css_selector('option:nth-child(1)').get_attribute('value')) == 'menu_order', 'сортировка не по умолчанию'

# 5. Отсортируйте товары от большего к меньшему
Select(driver.find_element_by_class_name('orderby')).select_by_value('price-desc')

# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
sort_key = driver.find_element_by_class_name('orderby')

# 7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
assert(driver.find_element_by_css_selector('option:nth-child(6)').get_attribute('value')) == 'price-desc'

driver.quit()


# ------------------------------
# отображение, скидка товара
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
# 2. Залогиньтесь
driver.find_element_by_css_selector("[id='menu-item-50'] > a").click()
driver.find_element_by_id('username').send_keys('wel2f@xutc.com')
driver.find_element_by_id('password').send_keys('7zxc_QWE0')
driver.find_element_by_css_selector(".button[name='login']").click()
# 3. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector('#menu-item-40').click()
# 4. Откройте книгу "Android Quick Start Guide"
driver.find_element_by_css_selector('.post-169').click()
# 5. Добавьте тест, что содержимое старой цены = "₹600.00"
assert(driver.find_element_by_css_selector('#product-169 del .amount').text) == "₹600.00"
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
assert(driver.find_element_by_css_selector('#product-169 ins .amount').text) == "₹450.00"
# 7. Добавьте явное ожидание и нажмите на обложку книги
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images a")) ).click()
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")) ).click()

driver.quit()


# ------------------------------
# проверка цены в корзине
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# 2. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector('#menu-item-40').click()
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
driver.find_element_by_css_selector('.post-182 a.button').click()

# 4. Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element([By.CSS_SELECTOR, ".cartcontents"], "1 Item"))

assert(driver.find_element_by_css_selector(".cartcontents").text) == "1 Item"
assert(driver.find_element_by_css_selector('#wpmenucartli .amount').text) == "₹180.00"

# 5. Перейдите в корзину
driver.find_element_by_css_selector('.post-182 a.added_to_cart').click()
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-subtotal span.amount')))
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-subtotal > span')))

driver.quit()


# --------------------------
# работа в корзине
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# 2. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector('#menu-item-40').click()
driver.execute_script('window.scrollBy(0, 300);')
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
driver.find_element_by_css_selector('.post-182 a.button').click()
time.sleep(5)
driver.find_element_by_css_selector('.post-180 a.button').click()

# 4. Перейдите в корзину
driver.find_element_by_id('wpmenucartli').click()

# 5. Удалите первую книгу
time.sleep(5)
driver.find_element_by_css_selector('tr:nth-child(1) a.remove').click()

# 6. Нажмите на Undo (отмена удаления)
driver.find_element_by_css_selector(' div.woocommerce-message > a').click()

# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
driver.find_element_by_css_selector('tr:nth-child(1) .input-text').clear()
driver.find_element_by_css_selector('tr:nth-child(1) .input-text').send_keys('3')

# 8. Нажмите на кнопку "UPDATE BASKET"
driver.find_element_by_css_selector('input.button:nth-child(2)').click()

# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
print(WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element_value([By.CSS_SELECTOR, "tr:nth-child(1) .input-text"], "3")) )

# 10. Нажмите на кнопку "APPLY COUPON"
time.sleep(5)
driver.find_element_by_css_selector('div.coupon input.button').click()

# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
assert(driver.find_element_by_css_selector('div.woocommerce > ul > li').text) == "Please enter a coupon code."

driver.quit()


# --------------------------
# работа в корзине
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# 2. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector('#menu-item-40').click()
driver.execute_script('window.scrollBy(0, 300);')

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
driver.find_element_by_css_selector('.post-182 a.button').click()

# 4. Перейдите в корзину
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element([By.CSS_SELECTOR, ".cartcontents"], "1 Item"))
driver.find_element_by_id('wpmenucartli').click()

# 5. Нажмите "PROCEED TO CHECKOUT"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.checkout-button')))
driver.find_element_by_css_selector('a.checkout-button').click()

# 6. Заполните все обязательные поля
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'billing_first_name')))
driver.find_element_by_id('billing_first_name').send_keys("Ivan")

driver.find_element_by_id('billing_last_name').send_keys('Petrov')
driver.find_element_by_id('billing_email').send_keys('ivapet70@gmail.com')
driver.find_element_by_id('billing_phone').send_keys('+79511237816')

driver.find_element_by_id('s2id_billing_country').click()
driver.find_element_by_id('s2id_autogen1_search').send_keys('Russia')
driver.find_element_by_css_selector("span.select2-match").click()

driver.find_element_by_id('billing_address_1').send_keys('st. Truda')
driver.find_element_by_id('billing_city').send_keys('Chebarcul')
driver.find_element_by_id('billing_state').send_keys('-')
driver.find_element_by_id('billing_postcode').send_keys('456544')

driver.execute_script('window.scrollBy(0, 600);')
time.sleep(5)
# 7. Выберите способ оплаты "Check Payments"
driver.find_element_by_id('payment_method_cheque').click()

# 8. Нажмите PLACE ORDER
driver.find_element_by_id('place_order').click()

# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element([By.CSS_SELECTOR, "div.woocommerce p:nth-child(1)"],
    "Thank you. Your order has been received."))

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element([By.CSS_SELECTOR, ".method > strong"], "Check Payments"))

driver.quit()

