import yaml, os
#读取yaml的数据
def read_yaml_data(catalog,file_name):
    with open("./data/" + catalog + os.sep + file_name, "r",encoding="utf-8") as f:
        return yaml.load(f)
