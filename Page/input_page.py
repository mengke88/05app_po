from Page.element import ElementLocation
from base.base import Base


class InputPage(Base):
    def __init__(self):
        # 初始化父类的init方法
        super().__init__()

    def send_search_text(self, text):
        """
        输入搜索内容
        :param text: 需要输入的搜索内容
        :return:
        """
        self.send_ele(ElementLocation.search_input, text)

    def get_search_result(self):
        """获取搜索结果"""
        # 返回定位对象列表目的？？[对象1, 对象2.....] -> [对象1文本，对象2文本....]
        results = self.search_eles(ElementLocation.search_result)
        return [i.text for i in results]
