# ChatBot (from chatgpt api)
## ChatGPT API 이용한 웹 챗봇서비스
> <b> 프로그래밍 시 레퍼런스 코드를 즉각적으로 찾아보기 위해 개발한 챗봇 </b>
#### 시안
![img](img/ChatBot.png)

### <b> 1. openai API + Flask </b>
1. 웹에서 구동되는 chatbot 개발: 03.13-03.15
2. chatbot 답변 파일로 저장 가능하게끔 구현: 03.17-03.19

#### 기능
1. ChatGPT API를 이용한 웹 챗봇서비스
2. 챗봇 질문 입력 시 받은 답변 txt 파일로 다운로드

#### 파일 
- Local chatbot (웹서비스 구현 전 테스트용으로 작성한 파일들)
   - local/chatgpt_local.py (코드), local/chat_local.txt (결과파일)
- Web chatbot
   - result/chat.py, result/index.html (코드), result/chat_web.txt (결과파일)



##### ❗ 해당 코드는 로컬에서만 테스트 가능하다. <br><br>

### <b> 2. openai API + PyQT5 </b>
1. pyQT로 로컬에서 구동되는 API 개발 (0427)

#### 기능
1. ChatGPT API를 이용한 로컬 챗봇서비스
2. 챗봇 질문 입력 시 받은 답변 txt 파일로 다운로드