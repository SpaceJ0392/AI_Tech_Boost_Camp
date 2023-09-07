# 최 상단의 __init__에는 하위의 모듈들의 이름을 적어준다.
__all__ = ["image", "sound", "stage"]

# 사용할 모듈 import
from . import image
from . import stage
from . import sound
