# DemoDict.py
device={"아이폰":5, "아이패드":10,"윈도우":20}
print(device)
print( len(device))
print(device["아이폰"])
device["맥프레"]=15
device["아이폰"]=6
print(device)
del device["아이폰"]

for item in device.items():
    print(item)

print("---key, valude---")
for k,v in device.items():
    print(k,v)