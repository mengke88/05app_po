import yaml, os


class AnalysisData:

    @classmethod
    def get_yaml_data(cls, name):
        """
        返回yaml文件数据
        :param name: 读取yaml文件名字
        :return:
        """
        # 打开文件
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # 解析数据
            return yaml.safe_load(f)
