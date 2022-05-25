print('dd')
import pandas as pd
import urllib.request
import csv
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
vocab_file = "TF_IDF_test/accidentcase_unigram.model"
sp.load(vocab_file)

lines = [
  '철골자재(데크플레이트(슈퍼데크))를 화물차에서 지게차로 하차 적재위치에 내려놓는 중 받침대가 낮아 지게차발이 빠지지않아 받침대를 설치하는중 2단으로 되어 있던 데크자재가 작접자 쪽으로 떨어지면서 사고 발생',
  '2022년04월27일 오전07시20분경 보라동 근린생활시설 및 다세대주택 신축공사 현장 내 대기실에서 작업 착수 전 동료들과 모여 대기중 송**이 갑자기 쓰러져 119에 전화해서 구급차가 출동하여 용인 소재 세브란스 병원으로 이송하여 사망한 사'
]
print('dd')
for line in lines:
  print(line)
  print(sp.encode_as_pieces(line))
  print(sp.encode_as_ids(line))
  print()