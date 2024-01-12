import random
import time
import csv
#
# # ---------------------------------------------------------------------------------------------
# # read.csv(플레이리스트)--------------------------------------------------------------------------
# with open('prePlly.csv', mode='r', encoding='utf8') as pP:
#     melCode, songKor, artistKor = pP.readline().split(',')
#
#     pPL = {}
#     code = 'gg'
#     code1 = []
#     # print(melCode)
#     while True:
#         code1 = pP.readline().split(',')
#         if code1[0] == "":              #
#             break
#         # print(pPL)
#         pPL[code1[0]]= {'songKor': code1[1], 'artistKor': code1[2]}
#         print(code1)
#         # pPL.update(code1[0] = code1[1], code1[2])
#         if code1[0] == "":              #11번줄에서 탈출구문 작성법 물어보기
#             break
#
# print(pPL)

dataFile = 'prePlly.csv'

prePllyCsv = read_csv(dataFile)

print(prePllyCsv)

pPllySong = prePllyCsv['노래한글']
pPllyArtist = prePllyCsv['가수한글']

print(pPllySong)
print(pPllyArtist)

prePlly =[]

for i, j in enumerate(pPllySong):
    prePllyDict = {}
    prePllyDict[j]=pPllyArtist[i]
    prePlly.append(prePllyDict)

print(prePlly)



#     for i, j in enumerate(a):
#         PllyDict = {}
#         PllyDict[j] = b[i]
#         c.append(PllyDict)



# def creatPlly(a, b, c):
#     for i, j in enumerate(a):
#         PllyDict = {}
#         PllyDict[j] = b[i]
#         c.append(PllyDict)


# for i, j in enumerate(pPllySong):
#     PllyDict = {}
#     PllyDict[j]=pPllyArtist[i]
#     prePlly.append(PllyDict)

# creatPlly(pPllySong,pPllyArtist,prePlly)


# for i in range(8):
    # print(PllySong[i],PllyArtist[i],Plly[])

# print(prePlly)
