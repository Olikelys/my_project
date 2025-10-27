# 使用轻量级 Python 基础镜像
FROM python:3.11-slim
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码（包括 .env 文件）
COPY . .

# 设置环境变量
ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
