import yaml

data = {'Search_Data': {'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
                        'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
with open("./text.yaml", "w") as f:  # 在当前⽬录下⽣成text.yaml⽂件，若⽂件存在直接更新内容
    yaml.safe_dump(data, f,encoding="utf-8",allow_unicode=True)
