import yaml
f =open('../config/data.yaml',encoding='utf8')
data=yaml.safe_load(f)
print(data)
print(data["hero"])
print(data["heros_name"])
print(data["heros_name2"])
print(data["heros_list"])