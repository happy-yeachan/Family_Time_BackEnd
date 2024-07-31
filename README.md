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
