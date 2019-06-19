# new_extract_cve_info
提取cve对应的与github相关的数据
主要包括以下五个文件：
1.extract_github_url:以2中提取的数据为基础，提取cve中与github相关的url
2.extract_cve_url：从原始数据中提取cve id 和它所对应的url
3.extract_github_project:以1中已提取的数据作为基础提取cve对应的github上的项目
4.extract_github_commit:以1中提取的数据为基础，提取cve id 和它对应的github commit
5.put it together： 以以上提取的数据为基础，把所有的数据合并到一个文件里，合并的时候去掉了cve id
