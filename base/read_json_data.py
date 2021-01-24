import yaml, os,json
#读取json的数据
def read_json_data(catalog,file_name):
    with open("./data/" + catalog + os.sep + file_name, "r",encoding="utf-8") as f:
        return json.load(f)
