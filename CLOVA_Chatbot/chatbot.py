import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()
HOST = os.getenv("HOST")
Api_key = os.getenv("Api_key")
Api_key_primary_val = os.getenv("Api_key_primary_val")
Request_id = os.getenv("Request_id")


headers = {
        'X-NCP-CLOVASTUDIO-API-KEY': Api_key,
        'X-NCP-APIGW-API-KEY': Api_key_primary_val,
        'X-NCP-CLOVASTUDIO-REQUEST-ID': Request_id,
        'Content-Type': 'application/json; charset=utf-8',
    }


def call_clova(preset_text):
    sys_data = [{'role':'system',
            'content':'''
            - 가족 구성원들의 유저 데이터를 기반으로 정보를 제공한다
            - 유저 데이터는 채팅 기록도 포함한다.
            - 아래 질문과 답변 기록 기반하여 앞으로의 질문에 대답한다.
            - 네이버 지도를 통해 추천해줄 만한 장소도 알려주기도 한다.
            - 혹은 직접 솔루션을 제안하거나 상품을 추천해 주기도 한다.
            '''}]
    sys_data.extend(preset_text)

    data = {
        'messages': sys_data,
        'topP': 0.6,
        'topK': 0,
        'maxTokens': 100,
        'temperature': 0.1,
        'repeatPenalty': 2.0,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 0
    }
    try:
        # POST 요청 보내기
        response = requests.post(HOST, json=data, headers=headers)

        # 응답 상태 코드 확인
        response.raise_for_status()  # 상태 코드가 200이 아닐 경우 예외 발생

        data = json.loads(response.text)
        content = data['result']['message']['content']
        # JSON 응답 반환
        return content

    except requests.exceptions.HTTPError as http_err:
        return {"error": "HTTP error occurred", "details": str(http_err)}
    except Exception as err:
        return {"error": "An error occurred", "details": str(err)}
