import requests
import os
from dotenv import load_dotenv

load_dotenv()
Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")

# API 엔드포인트 URL
url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"  # 사용할 실제 URL로 변경

headers = {
    "X-NCP-APIGW-API-KEY-ID": Client_ID,
    "X-NCP-APIGW-API-KEY": Client_Secret,
    "Content-Type": "application/json"
}

def sentiment_post(content: str):
    data = {
        "content": content
    }

    try:
        # POST 요청 보내기
        response = requests.post(url, json=data, headers=headers)

        # 응답 상태 코드 확인
        response.raise_for_status()  # 상태 코드가 200이 아닐 경우 예외 발생

        # JSON 응답 반환
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        return {"error": "HTTP error occurred", "details": str(http_err)}
    except Exception as err:
        return {"error": "An error occurred", "details": str(err)}

