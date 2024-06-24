import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# 全局变量配置

# 其他配置项...