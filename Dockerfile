# 使用轻量级基础镜像
FROM efreidevopschina.azurecr.io/cache/library/python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装生产依赖
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 复制应用文件
COPY src ./src
COPY tests ./tests

# 暴露端口（根据应用需求修改）
EXPOSE 8000

# 设置环境变量
ENV SECRET_KEY=dev_secret

# 启动命令
CMD ["python", "src/app.py"]
