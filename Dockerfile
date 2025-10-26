# 使用轻量级 Python 基础镜像
FROM efreidevopschina.azurecr.io/cache/library/python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY src ./src
COPY tests ./tests

# 暴露端口
EXPOSE 8000

# 启动命令（使用 Flask 绝对路径）
CMD ["/usr/local/bin/flask", "run", "--host=0.0.0.0", "--port=8000"]
