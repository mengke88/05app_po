"""
定义元素定位方式
"""
from selenium.webdriver.common.by import By


class ElementLocation:
    """搜索页面类"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")