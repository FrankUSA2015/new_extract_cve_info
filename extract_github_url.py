# -*- coding: utf-8 -*-
import json
import os
import re
#根据cve_github_url文件夹提取与github相关的url

path1=''
path2 = ''
files = os.listdir(path1)

for fil in files:
    all_data = []
    file_path =path1+"\\"+fil
    print(file_path)
    file_source = open(file_path, 'r',encoding='UTF-8')
    data_source = json.load(file_source)
    for dat1 in data_source:#取列表中的每个字典
        cwe = []
        cweDate = {}
        for dat2 in dat1['CVE_url']:
            url=dat2['url']
            if len(re.findall("http://github.com",url))!=0 or len(re.findall("https://github.com",url))!=0:
                cwe.append(url)
        if len(cwe):
            cweDate['CVE_id']=dat1['CVE_id']
            cweDate['CVE_url']=cwe
            all_data.append(cweDate)
    file2 = open(path2 + fil, 'w', encoding='UTF-8')  # 读文件的时候必须加编码格式，要不会出现错误
    json.dump(all_data, file2, indent=1)
    file2.close()