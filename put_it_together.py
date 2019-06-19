# -*- coding: utf-8 -*-
import json
import os
import re
#把所有github commit的项目放在一起，并且去重
#只需要修改path1和file2就可以完成多个合并
path1=''
path2 = ''
files = os.listdir(path1)
all_data = []
for fil in files:
    file_path =path1+"\\"+fil
    print(file_path)
    file_source = open(file_path, 'r',encoding='UTF-8')
    data_source = json.load(file_source)
    for dat1 in data_source:#取列表中的每个字典
        for dat2 in dat1['CVE_url']:
            all_data.append(dat2)
all_data=list(set(all_data))
file2 = open(path2 + "github_project.json", 'w', encoding='UTF-8')  # 读文件的时候必须加编码格式，要不会出现错误
print(path2 + "github_project.json")
json.dump(all_data, file2, indent=1)
file2.close()