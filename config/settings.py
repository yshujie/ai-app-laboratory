import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

class Settings(BaseSettings):
    debug: bool
    port: int
    http_proxy: str = None
    https_proxy: str = None    
    
    class Config:
        env_file = ".env"
        extra = "allow"  # 允许额外的未定义字段

settings = Settings()