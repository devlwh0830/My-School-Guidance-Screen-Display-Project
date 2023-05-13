import requests, os,sys
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
import schedule, time

print("경기도 성남시 대기질 정보 불러오기를 시작 합니다. (10분 마다 수행)")

def airKorea():
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty" # API URL
    key = "개인키" # API 접근 보안 키

    params = {
        "returnType" : "json", # JSON 형식
        "stationName" : "성남대로(모란역)", # 측정소명
        "dataTerm" : "DAILY", # 측정일
        "serviceKey" : key, # URL KEY 입력
        'ver' : '1.0' # API 버전
    }
    result = requests.get(url=url,params=params).json() # API 요청 값 리턴
    a = result["response"] # JSON 데이터 필터링
    b = a["body"] # JSON 데이터 필터링
    c = b["items"] # JSON 데이터 필터링
    for i in c: # 리턴 값 반복문으로 또 필터링
        pm10 = i["pm10Value"] # 미세먼지 ug/m3 변수 저장
        pm25 = i["pm25Value"] # 초미세먼지 ug/m3 변수 저장
        o3 = i["o3Value"] # 오존 ppm 변수 저장
        times = i["dataTime"] # 측정 시각변수 저장
        break

    target_image = Image.open(.\\images\\baseimages\\test.png') # 대기질 베이스 이미지 불러오기
    fontsFolder = '.\\images\\baseimages\\경기천년체\\TTF\\경기천년제목_Medium.ttf' #글자로 쓸 폰트 경로
    selectedFont =ImageFont.truetype(os.path.join(fontsFolder,fontsFolder),120) #폰트경로과 사이즈를 설정해줍니다.
    selectedFont1 =ImageFont.truetype(os.path.join(fontsFolder,fontsFolder),90) #폰트경로과 사이즈를 설정해줍니다.
    selectedFont2 =ImageFont.truetype(os.path.join(fontsFolder,fontsFolder),55) #폰트경로과 사이즈를 설정해줍니다.
    draw =ImageDraw.Draw(target_image)

    #========================================================================================== 미세먼지 측정 값에 따른 분류

    if (float(pm10) <= 30.0):
        add_image1 = Image.open('.\\images\\baseimages\\good.png')
        pm10result = str(pm10) + "\n\n좋음"
        draw.text((230,375),f"{pm10result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm10) <= 80.0):
        add_image1 = Image.open('.\\images\\baseimages\\middle.png')
        pm10result = str(pm10) + "\n\n보통"
        draw.text((230,375),f"{pm10result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm10) <= 150.0):
        add_image1 = Image.open('.\\images\\baseimages\\bad.png')
        pm10result = str(pm10) + "\n\n나쁨"
        draw.text((230,375),f"{pm10result}",fill="black",font=selectedFont,align='center') 
    else:
        add_image1 = Image.open('.\\images\\baseimages\\verybad.png')
        pm10result = str(pm10)
        draw.text((230,375),f"{pm10result}",fill="black",font=selectedFont,align='center') 
        draw.text((180,575),f"매우나쁨",fill="black",font=selectedFont1,align='center') 

    #========================================================================================== 초미세먼지 측정 값에 따른 분류

    if (float(pm25) <= 15.0):
        add_image2 = Image.open('.\\images\\baseimages\\good.png')
        pm25result = str(pm25) + "\n\n좋음"
        draw.text((850,375),f"{pm25result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm25) <= 35.0):
        add_image2 = Image.open('.\\images\\baseimages\\middle.png')
        pm25result = str(pm25) + "\n\n보통"
        draw.text((850,375),f"{pm25result}",fill="black",font=selectedFont,align='center') 
    elif (float(pm25) <= 75.0):
        add_image2 = Image.open('.\\images\\baseimages\\bad.png')
        pm25result = str(pm25) + "\n\n나쁨"
        draw.text((850,375),f"{pm25result}",fill="black",font=selectedFont,align='center') 
    else:
        add_image2 = Image.open('.\\images\\baseimages\\verybad.png')
        pm25result = str(pm25)
        if len(pm25result) >= 3:
            draw.text((845,375),f"{pm25result}",fill="black",font=selectedFont,align='center') 
        else:
            draw.text((880,375),f"{pm25result}",fill="black",font=selectedFont,align='center') 
        draw.text((800,575),f"매우나쁨",fill="black",font=selectedFont1,align='center') 

    #========================================================================================== 오존 측정 값에 따른 분류

    if (float(o3) <= 0.030):
        add_image3 = Image.open('.\\images\\baseimages\\ozon.png')
        o3result = str(o3) + "\n\n좋음"
        draw.text((1425,375),f"{o3result}",fill="black",font=selectedFont,align='center') 
    elif (float(o3) <= 0.090):
        add_image3 = Image.open('.\\images\\baseimages\\middle.png')
        o3result = str(o3) + "\n\n보통"
        draw.text((1425,375),f"{o3result}",fill="black",font=selectedFont,align='center') 
    elif (float(o3) <= 0.150):
        add_image3 = Image.open('.\\images\\baseimages\\bad.png')
        o3result = str(o3) + "\n\n나쁨"
        draw.text((1425,375),f"{o3result}",fill="black",font=selectedFont,align='center') 
    else:
        add_image3 = Image.open('.\\images\\baseimages\\verybad.png')
        o3result = str(o3)
        draw.text((1425,375),f"{o3result}",fill="black",font=selectedFont,align='center') 
        draw.text((1425,575),f"매우나쁨",fill="black",font=selectedFont1,align='center') 

    #========================================================================================== 최종 이미지 생성 처리

    target_image.paste(add_image1,(85,270),add_image1)
    target_image.paste(add_image2,(705,270),add_image2)
    target_image.paste(add_image3,(1330,270),add_image3)

    draw.text((50,1020),f"{times}",fill="white",font=selectedFont2,align='left')

    target_image.save(".\\images\\sky.png")
    target_image.close()

    print(f"[{datetime.now()}] 미세먼지 정보 업데이트 완료")

airKorea()
schedule.every(600).seconds.do(airKorea)
while True:
    schedule.run_pending()
    time.sleep(1)
