# 使用官方的 Python 基础镜像
FROM python:3.8-slim

# 设置代理环境变量
ARG http_proxy
ARG https_proxy
ENV http_proxy=${http_proxy}
ENV https_proxy=${https_proxy}

RUN echo $http_proxy && echo $https_proxy

# 设置工作目录
WORKDIR /opt/ai-app-laboratory

# 安装必要的系统工具，包括 procps 包以获得 pkill
RUN apt-get update && \
    apt-get install -y wget git inotify-tools procps

# 复制 requirements.txt 并安装 Python 包依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 复制 .env 文件
COPY .env .

# 设置启动命令
CMD ["bash", "-c", "chmod +x /opt/ai-app-laboratory/watch.sh && /opt/ai-app-laboratory/watch.sh"]