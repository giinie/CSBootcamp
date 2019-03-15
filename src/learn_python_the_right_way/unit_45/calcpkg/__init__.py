"""calcpkg 패키지의 독스트링"""
# 디렉토리 안에 __init__.py 파일이 있으면 해당 디렉토리는 패키지로 인식됨.
# __init__.py 파일은 내용을 비워둘 수 있음
# 파이썬 3.3 이상부터는 __init__.py 파일이 없어도 패키지로 인식되지만,
# 하위 버전에도 호환되도록 __init__.py 파일을 작성할 하도록 권장.

# 패키지 초기화. import 로 패키지를 가져오면 __init__.py 파일이 실행됨.

# from 패키지 import * -> 를 위한 기술
# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
# from .operation import add, mul
# from .geometry import triangle_area, rectangle_area

# 패키지.함수 형식으로 사용가
__all__ = ['add', 'triangle_area']  # 공개할 함수 목록
from .operation import *
from .geometry import *
