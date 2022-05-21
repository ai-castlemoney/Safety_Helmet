# 1. 사고사례 raw data
- 웹 스크래핑으로 추출한 사고사례 raw data
- accident_case_rawdata 폴더에 위치

- `accident_case_all.csv` : 사고사례 raw data 중 모든 column
- `accident_case_col.csv` : 사고사례 raw data 중 사용할 column

# 2. 사고사례 EDA
- 사고사례를 바탕으로 EDA 진행
- EDA_accident_case 폴더에 위치

- `EDA_accidentcase.csv` : `accident_case_col.csv`와 동일 (EDA하기 위해 해당 폴더에 복사)
- `EDA_accidentcase_1.csv`
    - 세부사항이 나누어져있는 컬럼은 분할함
    - 분할한 컬럼 중 모든 값이 동일한 컬럼들이 존재하는 것을 확인(`객체종류`, `부위종류`) → `부위종류` 컬럼 제거