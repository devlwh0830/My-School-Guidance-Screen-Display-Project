import requests, os,sys
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
import schedule, time

print("기상청 지진 발생 정보 불러오기를 시작 합니다. (5분 마다 수행)")

def koreanJijin():
    today1 = today = datetime.today().strftime("%Y%m%d")
    today = datetime.today().strftime("%Y%m%d%H%M")

    url = "https://apihub.kma.go.kr/api/typ01/url/eqk_list.php?tm1=201211231215&tm2=201311231215&disp=0&help=1&authKey=WiUNm7KfSjilDZuynyo4TQ"
    key = "API KEY"

    params = {
        "tm1" : f"{today1}0000",
        "tm2" : f"{today}",
        "disp" : "2",
        "authKey" : key
    }
    try :
        result = requests.get(url=url,params=params).text
        a = result.split("\n")
        for i in range(19,len(a)):
            b = a[i].strip().split(",")
            if b[0] == "3":
                jijin = []
                jijin.append(a[i])

        jijin = str(jijin[-1]).strip().split(",")
    except:
        jijin = ["","","","00000000000000","0.0","","","지진 발생 정보 없음.","","지진 발생 정보 없음.","","","","",""]

    target_image = Image.open('jijin.png')
    fontsFolder = '/slide show/images/baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'    #글자로 쓸 폰트 경로
    selectedFont =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목V_Bold.ttf'),65)
    selectedFont1 =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목V_Bold.ttf'),50) #폰트경로과 사이즈를 설정해줍니다.
    selectedFont2 =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목V_Bold.ttf'),100) #폰트경로과 사이즈를 설정해줍니다.
    selectedFont3 =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'),70) #폰트경로과 사이즈를 설정해줍니다.
    draw =ImageDraw.Draw(target_image)

    time = str(jijin[3])
    draw.text((420,540),f"{time[0:4]}년 {time[4:6]}월 {time[6:8]}일 {time[8:10]}시 {time[10:12]}분 {time[12:14]}초",fill="black",font=selectedFont1,align='left') 
    draw.text((145,620),f"{jijin[7]}",fill="black",font=selectedFont,align='left') 
    draw.text((160,840),f"{jijin[4]}",fill="black",font=selectedFont2,align='left') 
    draw.text((500,840),f"{jijin[9]}",fill="black",font=selectedFont3,align='left') 

    target_image.save("/slide show/images/jijinresult.png") #편집된 이미지를 저장합니다.
    target_image.close()
    
    print(f"[{datetime.now()}] 지진 정보 업데이트 완료")

koreanJijin()
schedule.every(300).seconds.do(koreanJijin) # 300초에 한번 실행

while True:
    schedule.run_pending()
    time.sleep(1)