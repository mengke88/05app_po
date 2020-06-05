# 导入yaml解析库
import yaml

# 打开文件
with open("./data.yaml", "r", encoding="utf-8") as f:
    # 读取yaml文件，返回值是字典
    data = yaml.safe_load(f)
    print("类型", type(data))
    print(data)
