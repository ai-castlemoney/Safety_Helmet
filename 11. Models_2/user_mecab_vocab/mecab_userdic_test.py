from konlpy.tag import Mecab

m = Mecab(dicpath=r"C:/mecab/mecab-ko-dic")
x = m.pos("이것은 메캅 테스트입니다. 사용자 사전을 등록한 후입니다. 양중기, 인양기, 인양고리, 소음성 난청")

print(x)