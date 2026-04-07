from flask import Blueprint, render_template, jsonify

# 主路由蓝图
main_bp = Blueprint('main', __name__)

# API路由蓝图
api_bp = Blueprint('api', __name__)


@main_bp.route('/')
def index():
    """首页"""
    return render_template('index.html')


@main_bp.route('/about')
def about():
    """关于页面"""
    return render_template('about.html')


@api_bp.route('/hello')
def api_hello():
    """API示例"""
    return jsonify({
        'message': 'Hello from API',
        'status': 'success'
    })


@api_bp.route('/data', methods=['GET'])
def api_get_data():
    """获取数据API"""
    return jsonify({
        'data': [1, 2, 3, 4, 5],
        'count': 5
    })
