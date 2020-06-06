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
        data_list = []
        with open("./data" + os.sep + name, "r", encoding="utf-8") as f:
            # 解析数据
            data = yaml.safe_load(f)
            for i in data.values():
                data_list.append(list(i.values()))
            print(data_list)
            return data_list
