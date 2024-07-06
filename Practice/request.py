import requests

# 동물등록증 조회
url = 'https://www.animal.go.kr/front/awtis/record/recordConfirmDtl.do'

owner_name = ""
registration_number = ""

data = {'sOwnerState': 'owner', 'searchOwnerKeyword': owner_name, 'sRfidState': 'drn', 'searchRfidKeyword': registration_number, }
response = requests.post(url, data=data)