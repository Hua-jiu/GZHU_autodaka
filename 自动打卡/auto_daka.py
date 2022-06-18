from time import sleep
from selenium import webdriver


def auto_daka(name, key, test_flag, long_sleep):
    if test_flag:
        driver = webdriver.Chrome()
    else:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 设置option
        driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器
        # 如需在服务器中运行,配置完环境后请使用如下option参数
        # option = webdriver.ChromeOptions()  # 以无头模式运行
        # option.add_argument('headless')
        # option.add_argument('no-sandbox')
        # option.add_argument('disable-dev-shm-usage')
        # option.add_experimental_option('useAutomationExtension', False)
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # driver = webdriver.Chrome(options=option)
    # 将健康表的地址copy过来就行
    driver.get('https://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start')
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div[1]/div['
                                 '2]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div[1]/div['
                                 '2]/input').send_keys(name)
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div[2]/div['
                                 '2]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div[2]/div['
                                 '2]/input').send_keys(key)
    sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]'
                                 '/form/div[2]/div[2]/div[1]/div[3]/a').click()
    sleep(3)
    print('教务系统登录完成')
    driver.find_element_by_xpath(
        '/html/body/div[4]/form/div/div/div/div/div[1]/div[4]/span/a').click()
    print('开始填报')
    sleep(long_sleep)

    #  test append
    driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr['
                                 '2]/td/div/table/tbody/tr[9]/td[2]/div/input[1]').click()

    driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr['
                                 '2]/td/div/table/tbody/tr[10]/td[1]/div/div/span/span[1]/span/span[2]').click()
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('广东省')
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('\n')

    driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr['
                                 '2]/td/div/table/tbody/tr[10]/td[2]/div/div/span/span[1]/span/span[2]').click()
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('广州市')
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('\n')

    driver.find_element_by_xpath('/html/body/div[4]/form/div/div[2]/div[3]/div/div[1]/div[1]/table/tbody/tr['
                                 '2]/td/div/table/tbody/tr[10]/td[3]/div/div/span/span[1]/span/span[2]').click()
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('番禺区')
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('\n')
    driver.find_element_by_xpath('//*[@id="V1_CTRL122"]').send_keys('广州大学')
    #  test append

    driver.find_element_by_xpath('//*[@id="V1_CTRL238"]').click()
    driver.find_element_by_xpath('//*[@id="V1_CTRL243"]').click()
    driver.find_element_by_xpath('//*[@id="V1_CTRL46"]').click()
    sleep(0.1)
    driver.find_element_by_xpath('//*[@id="V1_CTRL262"]').click()
    sleep(0.1)
    driver.find_element_by_xpath('//*[@id="V1_CTRL37"]').click()
    sleep(0.1)
    driver.find_element_by_xpath('//*[@id="V1_CTRL82"]').click()
    sleep(0.1)
    driver.find_element_by_xpath(
        '/html/body/div[4]/form/div/div[1]/div[2]/ul/li[1]/a').click()  # 提交表单
    sleep(0.1)
    sleep(4)
    driver.quit()
    return True
