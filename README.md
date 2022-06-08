# Aiffelthon
## Team : Safety_Helmet(요주의 안전모)
### Members
> 허남철 - 팀장, Python Coding, 라벨링 알고리즘 개발, 데이터 전처리, 각 파트 지원 등
>
> 김민주 - 학습 단어장, 모델 구축/학습 등
>
> 송아람 - 웹 스크래핑, 데이터 수집, 정제, 전처리 데이터 검수 등
>
> 정진현 - Front/Backend Webservice 구현 등
>
> 박성돈 - Git/Github 사용/관리, MLOps 자동화 구축, GCP 활용 등

### 1. 개요   
- 프로젝트명 : 안전지침 사고사례 제공 서비스
- 모델 : 산업안전지침(KOSHA Guide) 요약 및 건설사고사례(CSI) 추천 모델   
- 서비스 : 사용자(안전관리자, 현장작업자)가 특정한 작업(키워드) 전 관련 안전지침 요약과 사고사례 추천을 제공받는 웹 서비스   
    - KOSHA : 산업안전보건공단
    - CSI : 건설공사 안전관리 종합정보망   

### 2. 개발배경   
- 중대재해처벌법의 시행에도 불구하고 안전사고는 지속적으로 발생
- 방대한 양의 산업안전지침과 사고사례 습득 및 관리가 어려움
- 규정 요약 및 사고사례 추천 서비스 필요(산업안전사고 예방 효과)

### 3. 독창성   
- 기존에 없던 서비스를 개발하는 것에 그 차별성과 의의가 있다.
- 작업허가서(작업 및 작업장의 특징 등) 입력시 키워드와 관련있는 규제 요약 및 사고사례를 추천함으로써
- 작업과 작업장 중심의 산업안전지침 규정와 사고사례 정보를 쉽게 제공받을 수 있다.
- 특정 도메인의 데이터 셋, 사용자 정의 단어장을 작성하는 것만으로도 의의가 있다.
___

<style>
H2{color:skyblue !important;}
H3{color:DarkOrange !important;}
p{color:black !important;}
</style>

## 프로젝트 진행사항   
## Process   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/Safety_Helmet.png" width="900px" title="Process" alt="Safety_Helmet"></img><br/>   

## 1. 데이터 파트   
### 데이터 수집 [안전지침 및 사고사례]   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/03-1.png" width="900px" title="데이터 수집 [안전지침 및 사고사례]" alt="03-1"></img><br/>   

### 데이터 정제 [안전 지침(KOSHA Guide)]   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/03-2.png" width="900px" title="데이터 정제 [안전 지침(KOSHA Guide)]" alt="03-2"></img><br/>   

### 데이터 정제 [사고사례(KOSHA / CSI)]      
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/03-3.png" width="900px" title="데이터 정제 [사고사례(KOSHA / CSI)]" alt="03-3"></img><br/>   

### 안전 지침 DB & 사고 사례 DB 구축   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/03-4.png" width="900px" title="안전 지침 DB & 사고 사례 DB 구축" alt="03-4"></img><br/>   

### 사고 사례 데이터 분석 [업종 / 시설물]      
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/03-5.png" width="900px" title="사고 사례 데이터 분석 [업종 / 시설물]" alt="03-5"></img><br/>   

### 사고 사례 데이터 분석 [사고 종류]   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/03-6.png" width="900px" title="사고 사례 데이터 분석 [사고 종류]" alt="03-6"></img><br/>   

## 2. 모델 파트   
### Mecab 형태소 분석기 사용   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-1.png" width="900px" title="Mecab 형태소 분석기 사용" alt="04-1"></img><br/>   

### 사용자 정의 단어사전 구축   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-2.png" width="900px" title="사용자 정의 단어사전 구축" alt="04-2"></img><br/>   

### 사용자 정의 단어사전 추가 기준   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-3.png" width="900px" title="사용자 정의 단어사전 추가 기준" alt="04-3"></img><br/>   

### 모델 선정   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-4.png" width="900px" title="모델 선정" alt="04-4"></img><br/>   

### 파라미터 설정   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-5.png" width="900px" title="파라미터 설정" alt="04-5"></img><br/>   

### word2vec 임베딩 결과 시각화   
<img src="https://user-images.githubusercontent.com/96903618/172521746-311e97b8-62c6-4cd5-a44e-99db29e5f6b5.gif" title="word2vec 시각화"></img><br/>   

### 문장 간 유사도 측정   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-6.png" width="900px" title="문장 간 유사도 측정" alt="04-6"></img><br/>   

### 모델의 문제점 01   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-7.png" width="900px" title="모델의 문제점 01" alt="04-7"></img><br/>   

### 모델의 문제점 02   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-8.png" width="900px" title="모델의 문제점 02" alt="04-8"></img><br/>   

### 모델 문제 해결 방안   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/04-9.png" width="900px" title="모델 문제 해결 방안" alt="04-9"></img><br/>   

## 3. 웹 개발 파트
### 화면정의서 작성   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/05-1.png" width="900px" title="화면정의서 작성" alt="05-1"></img><br/>   

### 웹 개발 진행   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/05-2.png" width="900px" title="웹 개발 진행" alt="05-2"></img><br/>   

## 4. 시스템 엔지니어링 파트
### GCP / Cloud Functions   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/06-1.png" width="900px" title="GCP / Cloud Functions" alt="06-1"></img><br/>   

### Git, Github 활용   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/06-2.png" width="900px" title="Git, Github 활용" alt="06-2"></img><br/>   

### 문제 해결   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/06-3.png" width="900px" title="문제 해결" alt="06-3"></img><br/>   

## 5. 마무리
### 프로젝트 의의 & 발전 계획   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/08-1.png" width="900px" title="프로젝트 의의 & 발전 계획" alt="08-1"></img><br/>   

## 부록-1
### Troubleshooting Case  
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/07-1.png" width="900px" title="TroubleShooting 1-3" alt="07-1"></img><br/>   
<img src="https://github.com/ai-castlemoney/Safety_Helmet/blob/master/17.%20images/07-2.png" width="900px" title="TroubleShooting 4-6" alt="07-2"></img><br/>   

## 부록-2
### Reference   
- [KOSHA Guide 건설안전지침](https://www.kosha.or.kr/kosha/data/guidanceC.do)
- [KOSHA Guide 재해사례(건설업)](https://www.kosha.or.kr/kosha/data/construction.do)
- [CSI 건설사고사례](https://www.csi.go.kr/acd/acdCaseList.do)
- [웹 스크래핑](https://youtu.be/yQ20jZwDjTE)
- [한국어 형태소 분석기(POS) 분석](https://velog.io/@metterian)
- [Word2Vec](https://wikidocs.net/22660)
- [Firebase documentation](https://firebase.google.com/docs/firestore/)
- [Vuetify](https://vuetifyjs.com/en/)
- [Git](https://abled.tistory.com/category/git)
- [Google Cloud Functions 및 Firebase](https://cloud.google.com/functions/docs/concepts/functions-and-firebase?hl=ko)
- [Google Cloud 함수 작성](https://cloud.google.com/functions/docs/writing?hl=ko#functions-writing-file-structuring-python)
- [윈도우 환경 mecab 사용자 사전 추가](https://joyhong.tistory.com/128)
- [Microsoft Docs(about_Execution_Policies)](https://docs.microsoft.com/ko-kr/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2)
- [Best way to remove "\xad" in Python?](https://stackoverflow.com/questions/51976328/best-way-to-remove-xad-in-python)
- [Soft Hyphen](https://namu.wiki/w/Soft%20Hyphen)


## Aiffelthon Daily Log(22.05.03 ~ 22.06.09)
|일자|내용|링크1(Markdown)|링크2(Notion)|
|:---:|:---:|:---:|:---:|
|22.05.03|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220503.md)||
|22.05.04|멘토링 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220504.md)|[🗂](https://modulabs.notion.site/22-05-04-6a9cefa6450a4d88bf32fd38e17ecb91)|
|22.05.06|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220506.md)|[🗂](https://modulabs.notion.site/22-05-06-cc34aa84ffed46919503a4301f40b032)|
|22.05.09|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220509.md)|[🗂](https://modulabs.notion.site/22-05-09-926beb48b90e47dca7391144b41ea6e7)|
|22.05.10|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220510.md)||
|22.05.11|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220511.md)||
|22.05.12|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220512.md)||
|22.05.13|멘토링 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220513.md)|[🗂](https://modulabs.notion.site/22-05-13-90da5c10c6094b6f9b3f5bc0c93c2436)|
|22.05.16~17|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220516.md)|[🗂](https://modulabs.notion.site/22-05-16-c19c4e9e4ee541678ccbd44f0b7c2116)|
|22.05.18|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220518.md)|[🗂](https://modulabs.notion.site/22-05-18-6286eb27ea2246aca7ab33d5e8b352bd)|
|22.05.19|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220519.md)|[🔖](https://modulabs.notion.site/22-05-19-38cabdfc66724e4a925f12238fe2da2b)|
|22.05.20|멘토링 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220520.md)|[🔖](https://modulabs.notion.site/22-05-20-942453072cbe4471a06e04b328dd28f4)|
|22.05.23~27|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220523.md)|[🔖](https://modulabs.notion.site/5-4-ca5bda8e196d4439942f54e038a678c3)|
|22.05.30~06.03|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220530.md)|[🔖](https://www.notion.so/modulabs/22-06-03-395d4bdf5ccd439a85883d1bd01a60cb)|
|22.06.07~09|작업 및 논의 사항들|[📝](https://github.com/ai-castlemoney/Safety_Helmet/blob/master/16.%20daily_log/220607.md)|[🔖](https://www.notion.so/modulabs/214a1d08ac3146e886e0c90f299d3b5e) [🔖](https://www.notion.so/modulabs/22-06-06-265e966376ee477c8fc3013eaeaf0f90)|
