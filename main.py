from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/cb', methods=['POST','GET'])
def handle_post_request():
    # 这里可以添加你的业务逻辑代码
    data = request.get_json()  # 如果需要解析JSON数据的话
    # 处理data...
    print(data)

    response = {"status": "success", "message": "Post request received successfully"}
    
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
