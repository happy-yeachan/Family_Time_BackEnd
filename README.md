# 👨‍👩‍👧‍👦패밀리 타임

<div align="center">
  <img width="auto" alt="image" src="https://github.com/user-attachments/assets/93c8623d-8130-42d3-b66f-01e433001b9e">
</div>

</br>
<div align="center"><h3>👨‍👩‍👧‍👦 패밀리 타임</h3></div>

- **팀 명 :** sparcs_26
- **프로젝트 명 :** 패밀리 타임
- **프로젝트 기간 :** 2024.07.29 - 2024.08.01
- **한줄 소개 :** 하루에 한 번 패밀리 타임!
- **배포 링크 :** 링크

## <img width="18px" height="18px" src="https://github.com/codestates-seb/seb44_main_017/assets/120166543/9317d682-e804-4a3b-b6e0-57fd9aa0921b"> Team

| 기획 이동건  | 디자인 [정성희](https://tulip-turtle-82d.notion.site/PORTFOLIO-40624478eab140b59055aa505b6207e6?pvs=4)  | FE [이정우](https://github.com/MiRoro2)  | BE [오예찬](https://github.com/happy-yeachan)  |
|---|---|---|---|
| <img width="200" alt="image" src="https://github.com/user-attachments/assets/1f8808bb-88df-4675-8633-8e267ef4acd0">| <img width="200" alt="image" src="https://github.com/user-attachments/assets/eda2f4b9-a66e-48c8-8117-2e1c5e0e477d">|<img width="200" alt="image" src="https://github.com/user-attachments/assets/a298a39b-a0cc-444e-b790-5e1595533521">|<img width="200" alt="image" src="https://github.com/user-attachments/assets/27ae5167-e15d-4e05-9bb6-95f4353b5064">                                                                             

<div markdown="1">


## 🔨 Skills

<div align="center">
<img width="888" alt="image" src="https://github.com/user-attachments/assets/a278d9db-1e5c-4fb2-b227-d31e0e771626">



</div>

## 💫 Pages & Features
<div align="center">
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/dee5db96-1440-448f-b34f-1ecf0e2db82d" alt="image1" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/ee736c53-741a-4d0c-a7ee-9d25b596621f" alt="image2" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/f6a2fe19-6d37-4661-9103-c95f561c57b6" alt="image3" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/92857c8e-172a-492b-a348-1ada605dc4da" alt="image4" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/93c80410-1a7b-4faa-9b63-48551b9c025d" alt="image5" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/b49d7cd6-81dd-42ff-b6e5-b5ae16bd67a5" alt="image6" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/79386a68-7bee-4523-9889-2bcab5c870fe" alt="image7" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/b6b386d0-af11-47af-9fd9-ea6165427749" alt="image8" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/19e311e2-08fe-4fb3-ba16-7344b2df16b6" alt="image9" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/282ea1cf-4503-4680-a788-4fe12ed70ab4" alt="image10" width="400"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/bd2d8c24-f8f9-40c1-94cf-9540e526141c" alt="image11" width="400"/></td>
    <td><img src="https://github.com/user-attachments/assets/8946fb04-d4b9-4a38-b1c8-f0f0e5dad312" alt="image12" width="400"/></td>
  </tr>
</table>
</div>


# API 문서

이 API는 사용자 계정 관리, 가족 그룹, 사진, 댓글 및 챗봇 상호작용을 관리하는 다양한 엔드포인트를 제공합니다.

## 기본 URL
모든 엔드포인트는 다음 기본 URL을 기준으로 합니다:

url 비공개 상태입니다.

## 엔드포인트

### 사용자 인증

#### 1. 로그인
- **URL:** `/user/login`
- **Method:** `POST`
- **설명:** 사용자 로그인
- **Body:**
  ```json
  {
    "username": "01024264799",
    "password": "a123456789"
  }
  ```

#### 2. 회원가입
- **URL:** `/user/signup`
- **Method:** `POST`
- **설명:** 사용자 회원가입
- **Body:**
  ```json
  {
    "name": "아빠",
    "phone": "01024264798",
    "birth": "001228",
    "password": "a123456789".
    "sex": "남성"
  }
  ```

#### 3. 로그아웃
- **URL:** `/user/logout`
- **Method:** `GET`
- **설명:** 사용자 로그아웃

#### 4. 데이터 호출
- **URL:** `/user/me`
- **Method:** `GET`
- **설명:** 사용자 데이터 호출
- **Headers:**
  - `access_token: {{token}}`

### 가족 관리

#### 5. 가족 생성
- **URL:** `/family/create`
- **Method:** `POST`
- **설명:** 새로운 가족 그룹 생성
- **Headers:**
  - `access_token: {{token}}`

#### 6. 가족 입장
- **URL:** `/family/join?id=q5vlg`
- **Method:** `GET`
- **설명:** 기존 가족 그룹에 입장
- **Headers:**
  - `access_token: {{token}}`

#### 7. 가족 구성원 수 호출
- **URL:** `/family/`
- **Method:** `GET`
- **설명:** 가족 구성원 수 호출
- **Headers:**
  - `access_token: {{token}}`

### 사진 관리

#### 8. 사진 업로드
- **URL:** `/photo/upload`
- **Method:** `POST`
- **설명:** 댓글과 함께 사진 업로드
- **Body:**
  ```json
  {
    "comment": "아 허리아파",
  }
  ```
- **Headers:**
  - `access_token: {{token}}`

#### 9. 개별 사진 호출
- **URL:** `/photo/indi`
- **Method:** `GET`
- **설명:** 사용자 이름으로 개별 사진 호출
- **Body:**
  ```json
  {
    "user_name": "아빠",
  }
  ```
- **Headers:**
  - `access_token: {{token}}`

### 댓글

#### 10. 댓글 추가
- **URL:** `/photo/comments`
- **Method:** `POST`
- **설명:** 사진에 댓글 추가
- **Body:**
  ```json
  {
    "photo_no": "1",
    "comment": "멋지군"
  }
  ```
- **Headers:**
  - `access_token: {{token}}`

#### 11. 댓글 호출
- **URL:** `/photo/comments/1`
- **Method:** `GET`
- **설명:** 사진에 대한 댓글 호출
- **Headers:**
  - `access_token: {{token}}`

### 챗봇

#### 12. 질문답 관리
- **URL:** `/chatbot/ask`
- **Method:** `POST`
- **설명:** 챗봇을 위한 질문과 답변 관리
- **Body:**
  ```json
  {
    "question": "가장 좋아하는 음식은?",
    "answer": "토스트"
  }
  ```
- **Headers:**
  - `access_token: {{token}}`

#### 13. 채팅 관리
- **URL:** `/chatbot/chat`
- **Method:** `POST`
- **설명:** 채팅 내용 관리
- **Body:**
  ```json
  {
    "content": "아빠랑 내일 먹을 음식 추천좀",
  }
  ```
- **Headers:**
  - `access_token: {{token}}`

## 인증

대부분의 엔드포인트는 요청 헤더에 `access_token`을 필요로 합니다. 로그인 후 이 토큰을 얻어 다음과 같은 형식으로 사용하시면 됩니다.
```
access_token: {{token}}
```

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다.
```

여기서 `{{token}}`은 로그인 후 얻은 실제 토큰 값으로 대체해야 합니다. 보호된 엔드포인트에 요청할 때 이 토큰을 사용하시면 됩니다.
