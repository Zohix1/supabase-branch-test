# Flask 标准框架

一个标准的Flask应用程序框架，包含最佳实践和常用功能。

## 功能特性

- 应用工厂模式
- Blueprint 路由组织
- SQLAlchemy ORM
- Flask-Migrate 数据库迁移
- 环境配置管理
- RESTful API 支持

## 安装

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

## 配置

```bash
# 复制环境变量配置
cp .env.example .env

# 编辑 .env 文件，设置你的配置
```

## 运行

```bash
# 初始化数据库
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 运行应用
flask run
# 或
python app.py
```

## 项目结构

```
.
├── app.py              # 应用入口
├── config.py           # 配置文件
├── extensions.py       # 扩展初始化
├── routes.py           # 路由定义
├── models.py           # 数据模型
├── requirements.txt    # 依赖列表
├── .env.example        # 环境变量示例
└── README.md           # 项目说明
```

## 开发

- 添加新的路由到 `routes.py`
- 添加新的模型到 `models.py`
- 运行 `flask db migrate -m "description"` 创建迁移
- 运行 `flask db upgrade` 应用迁移
