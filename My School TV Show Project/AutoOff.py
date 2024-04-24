import os, cv2, glob
import schedule, time
import psutil

def AutoOff():
    cv2.namedWindow('GIF', cv2.WINDOW_NORMAL) # 전체 화면으로 'image' 창 생성
    cv2.setWindowProperty('GIF', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # cv2. WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN을 이용하여 전체화면 속성으로 변경

    # GIF 파일을 엽니다.
    gif = cv2.VideoCapture('AutoOff.gif')

    # GIF 파일의 모든 프레임을 읽어들입니다.
    frames = []
    while True:
        ret, frame = gif.read()
        if not ret:
            break
        frames.append(frame)

    # 모든 프레임을 화면에 출력합니다.
    for frame in frames:
        cv2.imshow('GIF', frame)
        cv2.waitKey(50) 

    os.system('shutdown -s -t 0') #컴퓨터 끄기

# 매일 13시 30분에 함수 실행
schedule.every().day.at("16:40").do(AutoOff)

while True:
    schedule.run_pending()
    time.sleep(1)