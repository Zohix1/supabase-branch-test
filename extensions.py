from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 初始化扩展，但不绑定到app
db = SQLAlchemy()
migrate = Migrate()
