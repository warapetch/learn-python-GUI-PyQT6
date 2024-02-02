```python
from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys


# run in console
app = QApplication(sys.argv)  

# argv: List[str] >> List Of String
# argv = argument value >> ค่าพารามิเตอร์ที่ส่งเข้ามา ทางคอนโซล

print(sys.argv) # [0] file current

# ตัวอย่าง
"""
python app1.py ["hello"] ["world"] [12345]
python app1.py "hello" "world" 12345
python app1.py hello world 12345
"""
print("sys.argv[0]=",sys.argv[0])
print("sys.argv[1]=",sys.argv[1])
print("sys.argv[2]=",sys.argv[2])

print(f"sys.argv[1]= {sys.argv[0]}")
print(f"sys.argv[2]= {sys.argv[1]}")
print(f"sys.argv[3]= {sys.argv[2]}")

```