FROM python:3.12-alpine

WORKDIR /app

# 设置 pip 镜像源为阿里云镜像
ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
ENV PIP_TRUSTED_HOST=mirrors.aliyun.com

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=src/app.py

# TODO: change to your own API key
ENV API_KEY="api-key"


EXPOSE 5000

# # 使用 gunicorn 启动，4个工作进程，日志写入文件
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--access-logfile", "/app/data/access.log", "--error-logfile", "/app/data/error.log", "src.app:app"]

# 使用 gunicorn 启动，2个工作进程，日志输出到标准输出
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-", "src.app:app"]