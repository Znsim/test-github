#for 갑 in 리스트

상자 = ["사과","배","콩","두부","아이스크림"]

for 값 in 상자:
    if(값 == "사과"):
        print("냉장실")
    elif(값=="아이스크림"):
        print("냉동실")
    else:
        print("폐기처분")

#답
상자 = ["사과","배","콩","두부","아이스크림"]

for 물건 in 상자:
    if(물건 == "사과"):
        print(f"'{물건}' 냉장실에 넣기")
    elif(물건=="아이스크림"):
        print(f"'{물건}' 냉동실에 넣기")
    else:
        print(f"'{물건}'은 폐기 처분")

# f-string 
# 문자와 변수를 혼재해서 문자열로 바꾸고 싶을떄 