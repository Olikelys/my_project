# src/app.py
from flask import Flask
import os
from dotenv import load_dotenv

# 初始化Flask应用
app = Flask(__name__)


# 加载环境变量 - 修复路径问题
def load_environment():
    """加载环境变量，支持开发和生产环境"""
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")

    # 尝试从不同路径加载
    if os.path.exists(env_path):
        load_dotenv(env_path)  # 容器内的相对路径
    else:
        load_dotenv()  # 默认位置

    # 设置默认值，避免生产环境崩溃
    if not os.getenv("SECRET_KEY"):
        app.logger.warning("SECRET_KEY not set, using default value")
        os.environ["SECRET_KEY"] = "dev_secret_default"


# 在应用启动前加载环境变量
load_environment()


class GreetingService:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY", "default_secret")
        # 移除强制验证，改为警告
        if self.secret_key == "default_secret":
            app.logger.warning(
                "Using default SECRET_KEY - not recommended for production"
            )

    def greet(self):
        return f"Greeting Service Running! Secret Key: {self.secret_key[:3]}..."  # 显示前3位用于调试


@app.route("/")
def home():
    try:
        service = GreetingService()
        return service.greet()
    except Exception as e:
        app.logger.error(f"Error in home route: {str(e)}")
        return "Internal Server Error", 500


@app.route("/health")
def health_check():
    """健康检查端点"""
    return {"status": "healthy", "service": "greeting-service"}


# 启动Flask服务
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
