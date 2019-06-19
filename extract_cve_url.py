# -*- coding: utf-8 -*-
import json
import os
#提取cve中的所有的url


path1=''
path2 = ''
files = os.listdir(path1)

for fil in files:
    all_data = []
    file_path =path1+"\\"+fil
    print(file_path)
    file_source = open(file_path, 'r',encoding='UTF-8')
    data_source = json.load(file_source)
    for dat1 in data_source['CVE_Items']:#取列表中的每个字典
        cwe = []
        cweDate = {}
        cve_id = dat1['cve']["CVE_data_meta"]['ID']
        cweDate['CVE_id']=cve_id
        for dat2 in dat1['cve']['references']['reference_data']:
            cwe.append(dat2)
        cweDate["CVE_url"]=cwe
        all_data.append(cweDate)
    file2 = open(path2+fil, 'w', encoding='UTF-8')  # 读文件的时候必须加编码格式，要不会出现错误
    json.dump(all_data, file2, indent=1)
    file2.close()