"""
测试用例文件
"""
import pytest

from base.driver import Driver
from base.get_data import AnalysisData
from base.page import Page

# 通过调用
# def get_data():
#     # 存储测试数据
#     data_list = []
#     # 获取yaml文件数据
#     data = AnalysisData.get_yaml_data("search.yaml")
#     for i in data.values():
#         data_list.append((i.get("input"), i.get("exp")))
#     return data_list


class TestSearch:
    # 调用关闭驱动对象的方法
    def teardown_class(self):
        Driver.quit_app_driver()

    # 设置只执行一次点击搜索的按钮
    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        Page.get_search_page().click_search_btn()

    # 定义测试在搜索框中输入内容并且断言，数据是将base目录下的get_data文件进行调用读书yaml文件的方法，这样就可以实现数据代码分离
    @pytest.mark.parametrize("value,result", AnalysisData().get_yaml_data("search.yaml"))
    def test_input(self, value, result):
        Page.get_input_page().send_search_text(value)
        assert result in Page.get_input_page().get_search_result()
