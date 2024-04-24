# 라이브러리 가져오기
from PIL import Image,ImageDraw,ImageFont
import mealService
import datetime

now = datetime.datetime.now()
now = str(now).split(" ")
now = str(now[0]).replace("-","")

# mealService 파일에서 MealService함수를 이용하여 정보 받아오기 그리고 meal변수에 담아주기
meal = mealService.MealService("7531423","J10",now)

# 베이스가 되는 이미지 가져오기
target_image = Image.open('.\\images\\baseimages\\mealService.png') #일단 기본배경폼 이미지를 open 합니다.

# 사용할 폰트 가져오기
fontsFolder = '.\\images\\baseimages\\경기천년체\\TTF\\경기천년제목_Medium.ttf' #글자로 쓸 폰트 경로
selectedFont = ImageFont.truetype(fontsFolder,40) 

# 베이스 이미지에 텍스트를 추가하기
draw =ImageDraw.Draw(target_image)

draw.text((990,220),f"{meal[0]}",fill="Black",font=selectedFont,align='left') # 칼로리 정보
draw.text((730,200),f"{meal[1]}",fill="Black",font=selectedFont,align='left') # 급식 메뉴
    
# 편집된 이미지를 저장하기
target_image.save(f".\\images\\before_image\\mealService.png") #편집된 이미지를 저장합니다.