import time
x = str(input("군 복무 여부 (Y or N): "))
if x == "Y":
    print("기록 확인중...")
    time.sleep(1)
    print("해군작전사령부 본부 통번역병 608일 병장 만기전역")
    
elif x == "N":
    print("죄송합니다. 이 서비스를 이용하실 수 없습니다.")
else:
    print("대문자 Y과 N중 하나만 입력하세요.")
