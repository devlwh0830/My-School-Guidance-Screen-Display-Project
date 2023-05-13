import requests, json # 외부 라이브러리 가져오기

# 나이스 데이터셋
# https://open.neis.go.kr/portal/mainPage.do

# 함수를 이용하여 호출하기
def MealService(shoolCode:str, educationCode:str, date:str):

    # url 변수를 통하여 API URL을 담기
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

    # API 요청 인자를 입력하기
    params = { 
        "KEY" : "API KEY HERE", # 인증키 / 필수
        "Type":"json", # 호물 문서 / 필수
        "pIndex":1, # 페이지 위치 / 필수
        "pSize":100, # 페이지 당 신청 숫자 / 필수
        "ATPT_OFCDC_SC_CODE":educationCode, # 시도교육청 코드 / 필수
        "SD_SCHUL_CODE": shoolCode, # 학교 코드 / 필수
        "MLSV_YMD": date # 날짜 / 선택
    }

    # 서버로 부터 받은 값을 result 변수에 담아주기
    result = requests.get(url=url,params=params).json() # API 값 받기

    # 받은 JSON 값 중 필요한 부분만 meal 변수와 mealService 변수에 담기
    meal = result["mealServiceDietInfo"]
    mealService = meal[1]["row"]

    # 칼로리 정보를 calInfo 변수에 담기
    calInfo = str(mealService[0]["CAL_INFO"]) # 칼로리 정보

    # 급식 메뉴를 menu 변수에 담기
    menu = str(mealService[0]["DDISH_NM"]) # 급식 메뉴 정보

    # 급식 메뉴를 보기 좋게 바꾸기
    menu = menu.split("<br/>") # "<br/>" 을 기준으로 문자열 자르기
    lunch = "<br/>" 
    for i in menu:
        i = i.split()
        lunch = f"{lunch}<br/>" + str(i[0])
    lunch = lunch.replace("<br/>","\n\n")

    # 리스트를 만들어서 칼로리 정보와 급식메뉴를 리스트에 넣기
    returnList = [str]
    returnList.insert(0,calInfo) 
    returnList.insert(1,lunch)

    # 최종 값이 담긴 리스트를 반환하기
    return returnList
