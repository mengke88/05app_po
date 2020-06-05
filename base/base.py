from selenium.webdriver.support.wait import WebDriverWait

from base.driver import Driver


class Base:

    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        #
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象列表
        """
        #
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入内容
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param text: 输入的文本内容
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        # 定位输入框元素
        inp = self.search_ele(loc, timeout, poll_frequency)
        # 清空输入框
        inp.clear()
        # 输入信息
        inp.send_keys(text)
