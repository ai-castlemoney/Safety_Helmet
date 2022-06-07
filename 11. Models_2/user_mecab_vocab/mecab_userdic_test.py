from konlpy.tag import Mecab

befor_mecab = Mecab(dicpath=r"C:/Users/김민주/mecab/mecab-ko-dic")
before = befor_mecab.nouns("데크플레이트, 아웃트리거")
print('사용자 정의 단어사전 적용 전 :', before)

after_mecab = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
after = after_mecab.nouns("데크플레이트, 아웃트리거")
print('사용자 정의 단어사전 적용 전 :', after)