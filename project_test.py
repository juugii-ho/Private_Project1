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
        # print(pPL)
        pPL[code1[0]]= {'songKor': code1[1], 'artistKor': code1[2]}
        print(code1)
        # pPL.update(code1[0] = code1[1], code1[2])
        if code1[0] == "":              #11번줄에서 탈출구문 작성법 물어보기
            break

print(pPL)
