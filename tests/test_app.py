# tests/test_app.py
import sys
from pathlib import Path

# 动态添加项目根目录到 Python 路径
sys.path.append(str(Path(__file__).parent.parent))

# 现在可以直接导入（无需 src 前缀）
from app import GreetingService  # 注意这里不需要 src


def test_greeting():
    service = GreetingService()
    assert service.greet() != "Hello! Secret Key: ..."
