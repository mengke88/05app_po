"""
元素定位
"""
from Page.element import ElementLocation
from base.base import Base


class SearchPage(Base):
    def __init__(self):
        # 初始化父类的init方法
        super().__init__()

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(ElementLocation.search_btn)

