# coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

#image = Image.open("D:/testpng/test1.png")
#text = pytesseract.image_to_string(image,lang='chi_sim')
#with open("output.txt", "w") as f:
#    print(text)
#    f.write(str(text))

r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"D:/testpng/test1.png") #文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
print(text) # 返回信息
