# src/app.py
from flask import Flask
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化Flask应用
app = Flask(__name__)


# 保留你的业务逻辑类（可选，但建议保留）
class GreetingService:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")
        if not self.secret_key:
            raise ValueError("SECRET_KEY environment variable is required")

    def greet(self):
        return f"Greeting Service Running!"  # 返回具体内容（避免暴露密钥）


# 定义路由：浏览器访问根路径时触发
@app.route("/")
def home():
    service = GreetingService()
    return service.greet()  # 返回业务结果


# 启动Flask服务（关键：绑定到0.0.0.0，让容器外部可访问）
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
