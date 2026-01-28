# testfaker.py

# 에러 ModuleNotFoundError: No module named 'qrcode'
# C:\dongaAI\day0123> pip install qrcode

# 에러 ModuleNotFoundError: No module named 'cv2'
# 에러 C:\dongaAI\day0123> pip install cv2
# 정답 C:\dongaAI\day0123> pip install opencv-python

# 에러 ModuleNotFoundError: No module named 'faker'
# C:\dongaAI\day0123> pip install faker 



import qrcode
import cv2
from faker import Faker   # 대문자는 클래스 중 하나

my = Faker()
for k in range(10):
    print(my.name())

print()
for k in range(10):
    print(my.ipv4_private())        # ip주소

print()
data = Faker('ko_KR')
for k in range(10):
    print(data.name())

print()
for k in range(10):
    print(data.address())

# 에러 ModuleNotFoundError: No module named 'faker'
# C:\dongaAI\day0123> pip install faker     

# 에러 ModuleNotFoundError: No module named 'qrcode'
# C:\dongaAI\day0123> pip install qrcode

# 에러 ModuleNotFoundError: No module named 'cv2'
# 에러 C:\dongaAI\day0123> pip install cv2
# 정답 C:\dongaAI\day0123> pip install opencv-python

