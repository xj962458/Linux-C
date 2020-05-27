import json
stu = [
    {"name": "武新纪", "age": 20, "tele": "17605675448"},
    {"name": "付玉婷", "age": 19, "tele": "17682750129"},
]

stu1 = json.loads(stu)
print(type(stu1))
print(stu1)
# print(stu1['age'])
# print(stu1['name'])
# 反序列化

