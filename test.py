import requests
# from tkinter import *



# tk = Tk()listb  = Listbox()
headers = {
    "Accept":"*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Length": "441",
    "Content-Type": "application; charset=UTF-8",
    "Cookie": "td_cookie=18446744070086724730; JSESSIONID=429884F719C4A68A20B5F39392380F80; td_cookie=18446744072006821871",
    # "Host": "123.206.76.150:8086",
    # "Origin": "http://123.206.76.150:8086",
    "Pragma": "no-cache",
    "Proxy-Connection": "keep-alive",
    # "Referer: http":"//123.206.76.150:8086/earth-wms/stock/nonTransactiona/show",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest"
}
    # "X-Requested-With": "XMLHttpRequest"

payload = {
    "ntId": "",
    "items": """21192|100.0000|ZH001|2018-09-01|10.0000|16|1000.0000|160.0000|20#
                21193|100.0000|ZH001|2018-09-01|10.0000|16|1000.0000|160.0000|20#""",
    "warehouseId": "10008",
    "storeId": "46",
    "operationType": "344",
    "billStatus": "1064",
    "bizType": "346",
    "deptId": "144",
    "departmentId": "144",
    "departmentName": "北京地球港卓越商业管理有限公司",
    "remarks": ""
}

data =payload
r = requests.post("http://123.206.76.150:8086/earth-wms/stock/nonTransactiona/edit",data=payload, headers=headers)
print(r.status_code)
print(r.text)
print(r.cookies)
print(r.headers)