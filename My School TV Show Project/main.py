import os
import glob
import cv2
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
print("화면 정보 제공을 시작합니다. (8초 마다 변경)")
idx = 0
while True:

    img_files = glob.glob('.\\images\\*.png') # 이미지 파일을 모두 img_files 리스트에 추가
    cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 전체 화면으로 'image' 창 생성
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # cv2. WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN을 이용하여 전체화면 속성으로 변경
    cnt = len(img_files)

    img = cv2.imread(img_files[idx])

    if img is None: # 이미지가 없는 경우
        continue

    cv2.imshow('image', img)
    if cv2.waitKey(8000) >= 0: # 1초 동안 사진보여주는데 만약에 키보드 입력이 있으면 종료
        break
    
    target_image = Image.open('/slide show/images/baseimages/times.png')  #일단 기본배경폼 이미지를 open 합니다.
    fontsFolder = './baseimages/경기천년체/TTF/경기천년제목_Medium.ttf'    #글자로 쓸 폰트 경로
    selectedFont =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체\TTF/경기천년제목_Medium.ttf'),140)
    selectedFont2 =ImageFont.truetype(os.path.join(fontsFolder,'/slide show/images/baseimages/경기천년체\TTF/경기천년제목_Medium.ttf'),250) #폰트경로과 사이즈를 설정해줍니다.
    draw =ImageDraw.Draw(target_image)

    draw.text((830,80),f"{datetime.now().year}년 {datetime.now().month}월 {datetime.now().day}일",fill="black",font=selectedFont,align='left') 
    draw.text((100,550),f"{datetime.now().hour}시 {datetime.now().minute}분",fill="black",font=selectedFont2,align='left') 

    target_image.save("/slide show/images/time.png") #편집된 이미지를 저장합니다.
    target_image.close()

    idx += 1
    if idx >= cnt:
        idx = 0

    print(f"[{datetime.now()}] 화면 제공 정보 업데이트 완료")

cv2.destroyAllWindows()