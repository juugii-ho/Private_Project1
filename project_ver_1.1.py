
# ---------------------------------------------------------------------------------------------

# 모듈 설정 ---------------------------------------------------------------------------------------------
import random
import time
import csv

# ---------------------------------------------------------------------------------------------
# read.csv(플레이리스트)--------------------------------------------------------------------------
with open('prePlly.csv', mode='r', encoding='utf8') as pP:
    melCode, songKor, artistKor = pP.readline().split(',')

    pPL = {}
    code = 'gg'
    code1 = []
    # print(melCode)
    while True:
        code1 = pP.readline().split(',')
        if code1[0] == "":              #
            break
        pPL[code1[0]]= {'songKor': code1[1], 'artistKor': code1[2]}
        if code1[0] == "":              #11번줄에서 탈출구문 작성법 물어보기
            break
print(pPL)
# pPL = list(pPL.values())
ApPLV = []
ApPLV2 = []
for i in pPL:
    pPLV = [v for v in pPL.values()]
    # ApPLV.append(pPLV)
    print(f' pPLV => {pPLV}')

    for v in pPLV:
        for i in (v.values()):
            print(f'ApPLV2 => {i}')
        # print
        # print(ApPLV2.values())
        # for l in ApPLV2:
        #     BpPLV2 = {ApPLV2[0] : ApPLV2[1]}
        #
        #     print(f'BpPLV2 => {BpPLV2}')
# for i in ApPLV2:


# PPT 꼭 다 따라해보기


print(prePlly)
# prePlly = pPL.values()[0]
# print(pPL)
# print(prePlly)

# kpopPlly =
# ostPlly =
# balPlly =
# dancdPlly =
# indiePlly =
#
# inkiChartPlly =

# findPlly =

# 함수 설정 -------------------------------------------------------------------------------------
# 메인 메뉴 함수 ---------------------------------------------------------------------------------
def mainMenu():                                     # 메인 메뉴 함수 - 메인 메뉴
    print('''
    1) 현재 재생 중인 플레이리스트
    2) 장르별 듣기
    3) 라디오
    4) 랜덤 플레이리스트
    5) 인기 차트
    6) 가수로 찾기
    ''')

# PyPod 오프닝 함수 -----------------------------------------------------------------------------

def opening():                                     # 오프닝 인트로 함수
    for i in range(13):
        print(f'{"="*i:>13}'+"PyPod"+f'{"="*i:<13}')
        time.sleep(0.3)
    print()


# 현재 재생 중인 플레이 함수 -----------------------------------------------------------------------
now = 0
def play():
    while True:                                     # 재생 중 화면 함수 - 재생 중입니다  ♫ + (메뉴/다른 곡 재생) 선택
        for i in range(1):
            print("재생 중입니다  ♫")
            time.sleep(1)
            print("재생 중입니다      ♫")
            time.sleep(1)
            print("재생 중입니다          ♫")
            time.sleep(1)
        print()
        stop = int(input(f"메뉴 : 0번, 다른 곡 듣기 : 곡 번호 1~{len(prePlly)}번을 눌러주세요"))
        if stop == 0:                               # 메뉴 화면으로
            break
        elif 1<=stop<=len(prePlly)+1:               # 다른 곡 재생
            global now
            now = int(stop-1)
            print(f"\n" + f'현재 {prePlly[now]}이 재생 중입니다.')
        else:                                       # 현재 재생 중 함수 재시작
            play()


# 가수 찾기  함수 --------------------------------------------------------------------------------

def findArtist(search):                                         # 가수 찾기 함수
    a = 0
    count = 0
    artistList = []
    for arti in findPlly:                                        # 곡명, 가수명 반복 검색
        if search in list(arti.values())[0]:                             # 가수명 일치하면 반환
            count += 1
            artistList.append(arti)
            print(f'{count}번 : {arti}')
            # print(arti.values())
            # print(count)
        else:                                                   # 일치하지 않으면 계속 찾기
            a += 1
    print(f"\n" + f"현재 {prePlly[now]}이 재생 중입니다. 해당 곡들을 추가할까요?" + "\n")
    search2 = input("""전체 추가 : '0', 한 곡 추가 : '해당 곡 번호', 메인 메뉴 : 아무 키나 눌러주세요""")
    if search2.isdecimal():
        search2 = int(search2)
        if search2 == 0:
            for k in artistList:
                prePlly.append(k)
            print("\n플레이리스트에 '가수 찾기 목록'이 추가되었습니다.\n")
        elif 1 <= search2 <= (len(findPlly)):
            prePlly.append(artistList[count-1])
            print(f"\n플레이리스트에 '가수 찾기 목록'의 {artistList[count-1]}이/가 추가되었습니다.\n")
        else:
            print("올바른 곡 번호를 입력해주세요.")
        play()
    else:
        play()
    pass


# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------


# 실행
# opening()                                               # 오프닝 인트로



#
# 기능
# 1. 메인 메뉴
while True:
    print(f"=============PyPod=============")
    mainMenu()                                          # 메인 메뉴
    choice = input("원하는 메뉴를 선택해주세요.")
    if choice == "1":                                   # 메인 메뉴 1 - 현재 재생 중인 플레이리스트
        print(f"\n" +"=============현재 재생 중인 플레이리스트=============" + "\n")
        count = 0
        for p in prePlly:
            count += 1
            print(f'{count:0>2}번 곡 - {p}')
        print(f"\n" + f'현재 {prePlly[now]}이 재생 중입니다.')
        play()
    elif choice == "2":                                   # 메인 메뉴 2 - 장르별 듣기
        print(f"\n" +"=============장르 별 플레이리스트=============" + "\n")
        print(f'''    1) K-POP
    2) OST
    3) BALLAD
    4) DANCE
    5) INDIE
''')
        cho2 = input("원하는 메뉴를 선택해주세요.")
        if cho2 == "1" :                                  # 메인 메뉴 2-1 장르:K-POP
            print(f"\n" + "============= K-POP =============" + "\n")
            count = 0
            for p in kpopPlly:
                count += 1
                print(f'{count:0>2}번 곡 - {p}')
            print(f"\n" + f'현재 {prePlly[now]}이 재생 중입니다. "K-POP"플레이리스트를 추가할까요?' + "\n")
            cho2_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요.")
            if cho2_2.isdecimal():
                cho2_2 = int(cho2_2)
                if cho2_2 == 0:
                    for k in kpopPlly:
                        prePlly.append(k)
                    print("\n플레이리스트에 'K-POP 플레이리스트'가 추가되었습니다.\n")
                elif 1<=cho2_2<=(len(kpopPlly)):
                    prePlly.append(kpopPlly[cho2_2-1])
                    print(f"\n플레이리스트에 'K-POP 플레이리스트'의 {kpopPlly[cho2_2-1]}이/가 추가되었습니다.\n")
                else:
                    print("올바른 곡 번호를 입력해주세요.")
                play()
            else:
                print("올바른 입력이 아닙니다.")

        elif cho2 =="2" :                                  # 메인 메뉴 2-2 장르:OST
            print(f"\n" + "============= OST =============" + "\n")
            count = 0
            for p in ostPlly:
                count += 1
                print(f'{count:0>2}번 곡 - {p}')
            print(f"\n" + f"현재 {prePlly[now]}이 재생 중입니다. 'OST 플레이리스트'를 추가할까요?" + "\n")
            cho2_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요.")
            if cho2_2.isdecimal():
                cho2_2 = int(cho2_2)
                if cho2_2 == 0:
                    for k in ostPlly:
                        prePlly.append(k)
                    print("\n플레이리스트에 'OST 플레이리스트'가 추가되었습니다.\n")
                elif 1 <= cho2_2 <= (len(ostPlly)):
                    prePlly.append(ostPlly[cho2_2 - 1])
                    print(f"\n플레이리스트에 'OST 플레이리스트'의 {ostPlly[cho2_2 - 1]}이/가 추가되었습니다.\n")
                else:
                    print("올바른 곡 번호를 입력해주세요.")
                play()
            else:
                print("올바른 입력이 아닙니다.")


        elif cho2 =="3" :                                  # 메인 메뉴 2-3 장르:BALLAD
            print(f"\n" + "============= BALLAD =============" + "\n")
            count = 0
            for p in balPlly:
                count += 1
                print(f'{count:0>2}번 곡 - {p}')
            print(f"\n" + f"현재 {prePlly[now]}이 재생 중입니다. 'BALLAD 플레이리스트'를 추가할까요?" + "\n")
            cho2_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요.")
            if cho2_2.isdecimal():
                cho2_2 = int(cho2_2)
                if cho2_2 == 0:
                    for k in balPlly:
                        prePlly.append(k)
                    print("\n플레이리스트에 'BALLAD 플레이리스트'가 추가되었습니다.\n")
                elif 1 <= cho2_2 <= (len(balPlly)):
                    prePlly.append(balPlly[cho2_2 - 1])
                    print(f"\n플레이리스트에 'BALLAD 플레이리스트'에 {balPlly[cho2_2 - 1]}이/가 추가되었습니다.\n")
                else:
                    print("올바른 곡 번호를 입력해주세요.")
                play()
            else:
                print("올바른 입력이 아닙니다.")

        elif cho2 =="4" :                                  # 메인 메뉴 2-4 장르:DANCE
            print(f"\n" + "============= DANCE =============" + "\n")
            count = 0
            for p in dancePlly:
                count += 1
                print(f'{count:0>2}번 곡 - {p}')
            print(f"\n" + f"현재 {prePlly[now]}이 재생 중입니다. 'DANCE 플레이리스트'를 추가할까요?" + "\n")
            cho2_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요.")
            if cho2_2.isdecimal():
                cho2_2 = int(cho2_2)
                if cho2_2 == 0:
                    for k in dancePlly:
                        prePlly.append(k)
                    print("\n플레이리스트에 'DANCE 플레이리스트'가 추가되었습니다.\n")
                elif 1 <= cho2_2 <= (len(dancePlly)):
                    prePlly.append(dancePlly[cho2_2 - 1])
                    print(f"\n플레이리스트에 'DANCE 플레이리스트'에 {dancePlly[cho2_2 - 1]}이/가 추가되었습니다.\n")
                else:
                    print("올바른 곡 번호를 입력해주세요.")
                play()
            else:
                print("올바른 입력이 아닙니다.")

            pass

        elif cho2 =="5" :                                  # 메인 메뉴 2-5 장르:INDIE
            print(f"\n" + "============= INDIE =============" + "\n")
            count = 0
            for p in indiePlly:
                count += 1
                print(f'{count:0>2}번 곡 - {p}')
            print(f"\n" + f"현재 {prePlly[now]}이 재생 중입니다. 'INDIE 플레이리스트'를 추가할까요?" + "\n")
            cho2_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요.")
            if cho2_2.isdecimal():
                cho2_2 = int(cho2_2)
                if cho2_2 == 0:
                    for k in indiePlly:
                        prePlly.append(k)
                    print("\n플레이리스트에 'INDIE 플레이리스트'가 추가되었습니다.\n")
                elif 1 <= cho2_2 <= (len(indiePlly)):
                    prePlly.append(indiePlly[cho2_2 - 1])
                    print(f"\n플레이리스트에 'INDIE 플레이리스트'에 {indiePlly[cho2_2 - 1]}이/가 추가되었습니다.\n")
                else:
                    print("올바른 곡 번호를 입력해주세요.")
                play()
            else:
                print("올바른 입력이 아닙니다.")
            pass
        elif cho2 =="6" :
            print(f"\n" + "============= POP =============" + "\n")
            pass
        else:
            print("올바른 입력이 아닙니다.")
            pass
    elif choice == "3":                                  # 메인 메뉴 3 - 라디오
        script = "\n안녕하세요, 여러분. 오늘은 화요일, 9일입니다. 오늘부터 시작해서 전국적으로 눈이 내릴 예정입니다. 기상청에 따르면..."
        for i in script:
            print(i, end='', flush=True)
            time.sleep(0.1)
        radio = input("\n\n라디오를 계속 재생할까요? 메인 메뉴는 0번, 계속 재생은 아무 버튼이나 눌러주세요.")
        if radio == "0":
            play()
        else:
            script2 = """
라디오 주파수 조정 시간입니다.
치직 치직 치지직
삐---------------------\n"""

            for s in script2:
                print(s, end='', flush=True)
                time.sleep(0.1)
            time.sleep(3)
            print()
            play()

    elif choice == "4":                                  # 메인 메뉴 4 - 랜덤 플레이리스트
        print(f"\n" + "============= 랜덤 플레이리스트 =============" + "\n")
        count = 0
        randomplly = []
        for i in range(1,11):
            randomplly.append(findPlly[random.randint(1,len(findPlly))])
            print(f'{i}번 : {randomplly[i-1]}')
            count += 1
        print(f"\n" + f"현재 {prePlly[now]}이 재생 중입니다. '랜덤 플레이리스트'를 추가할까요?" + "\n")
        cho2_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요.")
        if cho2_2.isdecimal():
            cho2_2 = int(cho2_2)
            if cho2_2 == 0:
                for k in randomplly:
                    prePlly.append(k)
                print("\n플레이리스트에 '랜덤 플레이리스트'가 추가되었습니다.\n")
            elif 1 <= cho2_2 <= 10:
                prePlly.append(randomplly[cho2_2-1])
                print(f"\n플레이리스트에 '랜덤 플레이리스트'에 {randomplly[cho2_2-1]}이/가 추가되었습니다.\n")
            else:
                print("올바른 곡 번호를 입력해주세요.")
            play()
        else:
            print("올바른 입력이 아닙니다.")



    elif choice == "5":                                  # 메인 메뉴 5 - 인기 차트
        print(f"\n" + "============= 오늘의 인기 차트 =============" + "\n")
        count = 0
        for p in inkiChart:
            count += 1
            print(f'{count:0>3}위 - {p}')
        print(f"\n" + f'현재 {prePlly[now]}이 재생 중입니다.\n\n"오늘의 인기 차트"를 플레이리스트에 추가할까요?')
        cho5_2 = input("전체 추가를 원하시면 0, 한곡 추가를 원하시면 해당곡 번호를 입력해주세요. 메인 메뉴는 아무 버튼이나 눌러주세요.")
        if cho5_2.isdecimal():
            cho5_2 = int(cho5_2)
            if cho5_2 == 0:
                for k in inkiChart:
                    prePlly.append(k)
                print("\n플레이리스트에 'K-POP 플레이리스트'가 추가되었습니다.\n")
            elif 1 <= cho5_2 <= (len(inkiChart)):
                prePlly.append(inkiChart[cho5_2 - 1])
                print(f"\n플레이리스트에 'K-POP 플레이리스트'에 {inkiChart[cho5_2 - 1]}이/가 추가되었습니다.\n")
            else:
                print("올바른 곡 번호를 입력해주세요.")
            play()
        else:
            print("올바른 입력이 아닙니다.")
    elif choice == "6":                                  # 메인 메뉴 6 - 가수로 노래 찾기
        search = input("가수명을 입력하세요 : ")
        findArtist(search)
    else:
        print("올바른 입력이 아닙니다.")

