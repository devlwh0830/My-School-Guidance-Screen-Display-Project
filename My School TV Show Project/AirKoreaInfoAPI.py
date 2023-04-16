import requests, os,sys
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
import schedule, time

print("경기도 성남시 대기질 정보 불러오기를 시작 합니다. (10분 마다 수행)")

def airKorea():
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"
    key = "API KEY"

    params = {
        "returnType" : "json",
        "stationName" : "성남대로(모란역)",
        "dataTerm" : "DAILY",
        "serviceKey" : key,
        'ver' : '1.0'
    }
    result = requests.get(url=url,params=params).json()
    a = result["response"]
    b = a["body"]
    c = b["items"]
    for i in c:
        pm10 = i["pm10Value"] # 미세먼지 ug/m3
        pm25 = i["pm25Value"] # 초미세먼지 ug/m3
        o3 = i["o3Value"] # 오존 ppm
        time = i["dataTime"]
        break

    target_image = Image.open('/slide show/images/baseimages/test.png')  
    fontsFolder = './baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'    #글자로 쓸 폰트 경로
    selectedFont =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'),120)
    selectedFont1 =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'),90) #폰트경로과 사이즈를 설정해줍니다.
    selectedFont2 =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'),50) #폰트경로과 사이즈를 설정해줍니다.
    draw =ImageDraw.Draw(target_image)

    #==========================================================================================

    if (float(pm10) <= 15.0):
        add_image1 = Image.open('/slide show/images/baseimages/good.png')
        pm10result = str(pm10) + "\n\n좋음"
        draw.text((215,348),f"{pm10result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm10) <= 35.0):
        add_image1 = Image.open('/slide show/images/baseimages/middle.png')
        pm10result = str(pm10) + "\n\n보통"
        draw.text((215,348),f"{pm10result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm10) <= 75.0):
        add_image1 = Image.open('/slide show/images/baseimages/bad.png')
        pm10result = str(pm10) + "\n\n나쁨"
        draw.text((215,348),f"{pm10result}",fill="black",font=selectedFont,align='center') 
    else:
        add_image1 = Image.open('/slide show/images/baseimages/verybad.png')
        pm10result = str(pm10)
        draw.text((260,348),f"{pm10result}",fill="black",font=selectedFont,align='center') 
        draw.text((180,548),f"매우나쁨",fill="black",font=selectedFont1,align='center') 
    
    #==========================================================================================
    
    if (float(pm25) <= 15.0):
        add_image2 = Image.open('/slide show/images/baseimages/good.png')
        pm25result = str(pm25) + "\n\n좋음"
        draw.text((850,348),f"{pm25result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm25) <= 35.0):
        add_image2 = Image.open('/slide show/images/baseimages/middle.png')
        pm25result = str(pm25) + "\n\n보통"
        draw.text((850,348),f"{pm25result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm25) <= 75.0):
        add_image2 = Image.open('/slide show/images/baseimages/bad.png')
        pm25result = str(pm25) + "\n\n나쁨"
        draw.text((850,348),f"{pm25result}",fill="black",font=selectedFont,align='center') 
    else:
        add_image2 = Image.open('/slide show/images/baseimages/verybad.png')
        pm25result = str(pm25)
        draw.text((880,348),f"{pm25result}",fill="black",font=selectedFont,align='center') 
        draw.text((800,548),f"매우나쁨",fill="black",font=selectedFont1,align='center') 

    #==========================================================================================

    if (float(o3) <= 0.030):
        add_image3 = Image.open('/slide show/images/baseimages/ozon.png')
        o3result = str(o3) + "\n\n좋음"
        draw.text((1425,348),f"{o3result}",fill="black",font=selectedFont,align='center') 
    elif (float(o3) <= 0.090):
        add_image3 = Image.open('/slide show/images/baseimages/middle.png')
        o3result = str(o3) + "\n\n보통"
        draw.text((1425,348),f"{o3result}",fill="black",font=selectedFont,align='center') 
    elif (float(o3) <= 0.150):
        add_image3 = Image.open('/slide show/images/baseimages/bad.png')
        o3result = str(o3) + "\n\n나쁨"
        draw.text((1425,348),f"{o3result}",fill="black",font=selectedFont,align='center') 
    else:
        add_image3 = Image.open('/slide show/images/baseimages/verybad.png')
        o3result = str(o3)
        draw.text((1425,348),f"{o3result}",fill="black",font=selectedFont,align='center') 
        draw.text((1425,548),f"매우나쁨",fill="black",font=selectedFont1,align='center') 

    #==========================================================================================

    target_image.paste(add_image1,(85,250),add_image1)
    target_image.paste(add_image2,(705,250),add_image2)
    target_image.paste(add_image3,(1330,250),add_image3)

    draw.text((30,950),f"{time}",fill="black",font=selectedFont2,align='center')

    target_image.save("/slide show/images/sky.png")
    target_image.close()

    print(f"[{datetime.now()}] 미세먼지 정보 업데이트 완료")

airKorea()
schedule.every(600).seconds.do(airKorea) # 600초에 한번 실행

while True:
    schedule.run_pending()
    time.sleep(1)
