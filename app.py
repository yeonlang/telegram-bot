from flask import Flask, request
import os
app = Flask(__name__)

token = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route(f'/{token}', methods=['POST'])
def telegram():
    #1. 구조 확인하기
    from_telegram=request.get_json() #=>telegram에 자료값 요청 결과값은 dict 으로 온다.
    print(from_telegram)
    
    #2. 그대로 돌려보내기
    chat_id = from_telegram['message']['chat']['id']
    text = from_telegram['message']['text']
    print(chat_id)
    print(text)
    
    return '', 200
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
    # {'update_id': 736079307, 
    #  'message': 
    #      {'message_id': 17, 
    #       'from': {'id': 758344425, 'is_bot': False, 'first_name': 'Daehyeon', 'last_name': 'Kang', 'language_code': 'ko'}, 
    #       'chat': {'id': 758344425, 'first_name': 'Daehyeon', 'last_name': 'Kang', 'type': 'private'}, 
    #       'date': 1545372126, 
    #       'text': '오랜만입니다'
    #      }
    # }