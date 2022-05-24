# 1. 사고사례 raw data
- 웹 스크래핑으로 추출한 사고사례 raw data
- accident_case_rawdata 폴더에 위치

- `accident_case_all.csv` : 사고사례 raw data 중 모든 column
- `accident_case_col.csv` : 사고사례 raw data 중 사용할 column

# 2. 사고사례 EDA
- 사고사례를 바탕으로 EDA 진행
- EDA_accident_case 폴더에 위치

- `1. EDA_컬럼분할, 제거.csv`
    - 세부사항이 나누어져있는 컬럼은 분할함
    - 분할한 컬럼 중 모든 값이 동일한 컬럼들이 존재하는 것을 확인(`객체소분류`, `부위내용`) → `부위내용` 컬럼 제거

- `2. EDA_원인분석, 고유값.csv`
    - 사고원인 분석
    - 각 컬럼의 고유값 추출 (작업허가서에 사용할 카테고리)
    - 2_1. 사고원인.csv
    - 2_2. 사고원인 분류.csv
    - 2_3. 공종 리스트.csv
    - 2_4. 사고객체 리스트.csv
    - 2_5. 장소 리스트.csv
    - 2_6. 부위 리스트.csv
    - 2_7. 시설물 리스트.csv
    - 2_8. 작업프로세스 리스트.csv