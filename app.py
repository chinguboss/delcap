from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 설정

# 스킬 서버 엔드포인트
@app.route('/menu', methods=['POST'])
def handle_menu():
    # 카카오톡 챗봇에서 받은 요청 데이터를 처리
    data = request.json
    menu = data['userRequest']['utterance']  # 사용자가 선택한 메뉴 가져오기

    # 사용자가 선택한 메뉴에 따라 응답
    response_text = f"{menu}을(를) 선택하셨습니다. 몇 개 주문하시겠습니까?"

    # 카카오 i 오픈빌더에 보낼 응답 형식
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": response_text
                    }
                }
            ]
        }
    }

    return jsonify(response)  # JSON 응답 반환


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 로컬 서버 실행
