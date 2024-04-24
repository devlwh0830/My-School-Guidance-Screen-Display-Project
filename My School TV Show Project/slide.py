import os
import glob
import cv2
from PIL import Image,ImageDraw,ImageFont
from datetime import *
print("화면 정보 제공을 시작합니다. (5초 마다 변경)")
today = f"{datetime.now().year}년 {datetime.now().month}월 {datetime.now().day}일"
img_files = glob.glob('.\\images\\*.png') # 이미지 파일을 모두 img_files 리스트에 추가
cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 전체 화면으로 'image' 창 생성
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # cv2. WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN을 이용하여 전체화면 속성으로 변경
fontsFolder = '.\\images\\baseimages\\경기천년체\\TTF\\경기천년제목_Medium.ttf'    #글자로 쓸 폰트 경로
selectedFont =ImageFont.truetype(fontsFolder,50)
selectedFont2 =ImageFont.truetype(fontsFolder,50) #폰트경로과 사이즈를 설정해줍니다.
idx = 0
while True:

    times = 0
    while(times <= 1):
        target_image = Image.open('.\\images\\before_image\\jijinresult.png')  #일단 기본배경폼 이미지를 open 합니다.
        draw =ImageDraw.Draw(target_image)
        draw.text((165,1005),f"{today}",fill="black",font=selectedFont,align='left') 
        draw.text((715,1005),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 
        target_image.save(".\\images\\jijinresult.png") #편집된 이미지를 저장합니다.
        target_image.close()

        target_image = Image.open('.\\images\\before_image\\mealService.png')  #일단 기본배경폼 이미지를 open 합니다.
        draw =ImageDraw.Draw(target_image)
        draw.text((165,1005),f"{today}",fill="black",font=selectedFont,align='left') 
        draw.text((715,1005),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 
        target_image.save(".\\images\\mealService.png") #편집된 이미지를 저장합니다.
        target_image.close()

        target_image = Image.open('.\\images\\before_image\\sky.png')  #일단 기본배경폼 이미지를 open 합니다.
        draw =ImageDraw.Draw(target_image)
        draw.text((165,1005),f"{today}",fill="black",font=selectedFont,align='left') 
        draw.text((715,1005),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 
        target_image.save(".\\images\\sky.png") #편집된 이미지를 저장합니다.
        target_image.close()

        times += 1

    cnt = len(img_files)

    img1 = cv2.imread(img_files[idx])
    img2 = cv2.imread(img_files[(idx + 1) % cnt])

    if img1 is None or img2 is None:
        continue

    alpha = 0
    while alpha <= 1:
        # 두 이미지를 서서히 변화하도록 합성
        dst = cv2.addWeighted(img1, round(1 - alpha,2) - 0.02, img2, alpha, 0)
        cv2.imshow('image', dst)
        cv2.waitKey(10)
        alpha += 0.02

    if cv2.waitKey(4000) >= 0: # 1초 동안 사진보여주는데 만약에 키보드 입력이 있으면 종료
        break
    
    times = 0
    while(times <= 1):

        target_image = Image.open('.\\images\\before_image\\jijinresult.png')  #일단 기본배경폼 이미지를 open 합니다.
        draw =ImageDraw.Draw(target_image)
        draw.text((165,1005),f"{today}",fill="black",font=selectedFont,align='left') 
        draw.text((715,1005),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 
        target_image.save(".\\images\\jijinresult.png") #편집된 이미지를 저장합니다.
        target_image.close()

        target_image = Image.open('.\\images\\before_image\\mealService.png')  #일단 기본배경폼 이미지를 open 합니다.
        draw =ImageDraw.Draw(target_image)
        draw.text((165,1005),f"{today}",fill="black",font=selectedFont,align='left') 
        draw.text((715,1005),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 
        target_image.save(".\\images\\mealService.png") #편집된 이미지를 저장합니다.
        target_image.close()

        target_image = Image.open('.\\images\\before_image\\sky.png')  #일단 기본배경폼 이미지를 open 합니다.
        draw =ImageDraw.Draw(target_image)
        draw.text((165,1005),f"{today}",fill="black",font=selectedFont,align='left') 
        draw.text((715,1005),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 
        target_image.save(".\\images\\sky.png") #편집된 이미지를 저장합니다.
        target_image.close()

        times += 1

    idx += 1
    if idx >= cnt:
        idx = 0

    if datetime.now().hour == 16 and datetime.now().minute == 40:
        break
    
    print(f"[{datetime.now()}] 화면 제공 정보 업데이트 완료")
    

cv2.destroyAllWindows()