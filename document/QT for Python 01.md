[ author: วรเพชร  เรืองพรวิสุทธิ์ 
 date: 18/01/2567 # 18/01/2024 ]

# <span style="color:blue">QT for Python</span>
### PyQT6 [ปัจจุบัน เวอร์ชั่น 6.6.1 @ 18/01/2567]

[<ลิงก์> Qt for Python](https://doc.qt.io/qtforpython-6/)

## <span style="color:red">หลักสูตรเร่งลัด Quick Start</span>

---
### <span style="color:blue">เริ่มเขียนโปรแกรมไพธอน GUI ด้วย PyQT6</span>
[<ลิงก์ เอกสาร> ](https://doc.qt.io/qtforpython-6/quickstart.html#quick-start)

สิ่งแวดล้อมที่ต้องการ
* ไพธอน 3.7 ขึ้นไป 
(ปัจจุบัน 3.12.1 และ **3.13 pre-release 01/10/2567**)
[< รายละเอียด > เวอร์ชั่นล่าสุด 3.12.1](https://www.python.org/downloads/)

* ขณะพัฒนาควรใช้ Virtual Environment (venv ,anaconda)
* แพ็คเกจที่จำเป็น PyQT6


### เริ่มกันเลย
1. ติดตั้ง VS-Code
2. ติดตั้ง Virtual Enviroment (venv / Anaconda)

---
#### 2.1 <span style="color:blue">สร้าง Venv โดยใช้ Python Venv </span>
> ติดตั้ง Python Virtual Environment (ถ้ายังไม่ได้ติดตั้ง)

#### ตรวจสอบการติดตั้ง venv ด้วยคำสั่ง 
```
pip show venv
```
> ถ้าขึ้นข้อความ WARNING: Package(s) not found: venv
> หมายความว่า ยังไม่ได้ติดตั้ง Python Virtual Environment


คำสั่งในการติดตั้ง Python Virtual Environment
```python
pip install virtualenv
```

#### เริ่มทำการสร้าง venv
1. สร้างโฟลเดอร์โปรเจค `PyQT6`
2. cd เข้า `PyQT6`
3. ทำงานที่ CMD > พิมพ์คำสั่ง 
#### สร้าง Venv ชื่อ `env`
```bash
python -m venv env
```
4. เมื่อสร้างเสร็จให้ 
### ทำการแอคติเวท Activate
ทำงานที่ CMD > พิมพ์คำสั่ง 
### Windows
```bash
env/Script/activate 
```

#### McOS/Linux
```bash
source env/Script/activate 
```

5. การปิด หรือ ออกจาก Venv
ทำงานที่ CMD > พิมพ์คำสั่ง 
#### Windows
```python
deactivate
```
#### MacOS
```python
source deactivate
```

---
![Alt text](img_anaconda.png)
## 2.2 <span style="color:blue">สร้าง Venv โดยใช้ Anaconda3</span>

[<ลิงก์> ดาวน์โหลดและติดตั้ง Anaconda3](https://www.anaconda.com/download)

#### เริ่มทำการสร้าง venv
1. สร้างโฟลเดอร์โปรเจค `PyQT6`
2. cd เข้า `PyQT6`
3. ทำงานที่ CMD > พิมพ์คำสั่ง 
#### สร้าง Venv ชื่อ `envPyQT` และ กำหนดให้ติดตั้งไพธอนเวอร์ชั่น 3.11.7

[< รายละเอียด > 3.11.7 เป็นเวอร์ชั่นท้ายสุดของ 3.11](https://docs.python.org/3.11/)


หากไม่กำหนดจะติตตั้งเวอร์ชั่นล่าสุด (3.12.1 หรือ มากกว่า)
[< รายละเอียด > เวอร์ชั่นล่าสุด](https://www.python.org/downloads/)

```bash
conda create -n envpyqt python==3.11.7
```
4. เมื่อสร้างเสร็จให้ 
### ทำการแอคติเวท Activate
ทำงานที่ CMD > พิมพ์คำสั่ง 
### Windows
```bash
conda activate envpyqt6
```

#### MacOS/Linux
```bash
source activate envpyqt6
```

> ถ้าใครติดปัญหา Anaconda แจ้งแบบนี้
```usage: conda-script.py [-h] [--no-plugins] [-V] COMMAND ...
conda-script.py: error: argument COMMAND: invalid choice: 'activate'  
(choose from 'clean', 'compare', 'config', 'create', 'info', 'init',   
'install', 'list', 'notices', 'package', 'remove', 'uninstall',   
'rename', 'run', 'search', 'update', 'upgrade', 'build',   
'content-trust', 'convert', 'debug', 'develop', 'doctor',   
'index', 'inspect', 'metapackage', 'render', 'skeleton',   
'token', 'server', 'repo', 'env', 'verify', 'pack')  

```

#### ให้แก้ไขดังนี้
> ปิด VS-Code  
> ปิด CMD (ถ้าเปิดไว้)
---
> เปิด CMD แล้วพิมพ์คำว่า
```
conda init
```

จากนั้น ปิด CMD  
แล้วเข้า VS-Code  
ลองใช้คำสั่ง Activate อีกครั้ง
```bash
conda activate envqt6
```
อีกครั้ง


5. การปิด หรือ ออกจาก Venv
ทำงานที่ CMD > พิมพ์คำสั่ง 
#### Windows
```python
deactivate
```
#### MacOS
```python
source deactivate
```

---
#### <span style="color:blue">ติดตั้งแพ็กเกจที่จำเป็น/ระบบต้องการ</span>
1. อัพเดต PIP เป็นเวอร์ชั่นล่่าสุด
```python
python -m pip install --upgrade pip
```
2. PyQT6 (เวอร์ชั่น 6.6.1)
```python
pip install PyQt6
```
3. PyQT6-Tools (เวอร์ชั่น 6.4.2.3.3)

[< PyQT6-Tools @ GitHub >](https://github.com/altendky/pyqt-tools)


```python
pip install pyqt6-tools
```
<span style="color:red">ถ้าต้องการ QT-DESIGNER เวอร์ชั่น 6.6.1
ต้องติดตั้ง PySide6 หรือ ใช้วิธีอื่น</span>


#### คำสั่งในการเรียกใช้งาน PyQT-Tools Designer
```python
Usage: pyqt6-tools designer [OPTIONS]
```

```
Options:
  -p, --widget-path DIRECTORY     Paths to be combined with PYQTDESIGNERPATH
  --example-widget-path           Include the path for the pyqt6-tools example
                                  button (c:\users\sda\testenv\lib\site-
                                  packages\pyqt6_plugins)

  --designer-help                 Pass through to get Designer's --help
  --test-exception-dialog         Raise an exception to check the exception
                                  dialog functionality.

  --qt-debug-plugins / --no-qt-debug-plugins
                                  Set QT_DEBUG_PLUGINS=1
  --help                          Show this message and exit.
  ```