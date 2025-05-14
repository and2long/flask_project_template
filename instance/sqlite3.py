"""instance/sqlite3.py
"""

import os

# 设置数据库文件存放在 data 目录下
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)  # 确保目录存在

# TODO: change to your own database file name
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(data_dir, "db-name.db")}'
