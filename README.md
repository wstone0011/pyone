# pyone
使用pyinstaller打包python运行环境和依赖库，而又可以执行自定义的脚本。

# 说明
```
1. 打包方法
pyinstaller -F pyone.py --noupx

注意：
因为电脑里有upx环境，用"pyinstaller -F pyone.py"打包出来的程序会报错，不知道是不是pyinstaller的bug。但是打包完成的程序用upx加壳是可以正常运行的。

2. 使用方法
pyone run.py

3.要运行的脚本默认为run.py，但也可以是别的名字，可以是main.py，甚至可以是pyone.py

4.自定义脚本文件run.py里面依赖的库需要借助pyinstaller提前打包好

5.打包python环境依赖于pyinstaller，而执行自定义脚本的能力则在于“在顶层代码中执行exec(code)”

```

# 测试案例

## 打包flask环境
run.py
```python
from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return "Hello World."
    
app.run("0.0.0.0", 80)

```

**输出效果**
```
>pyone.exe run.py
 * Serving Flask app 'pyone'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:80
 * Running on http://192.168.67.48:80
Press CTRL+C to quit

访问http://127.0.0.1:80可以看到“Hello World.”，表明程序运行正常。
```

## 执行自定义代码，支持自定义类
main.py
```python
class A():
    a=123
    def __init__(self):
        print("I'm A.__init__")
        print(A.a)
        
    def sum(self, x, y):
        print("x="+str(x))
        print("y="+str(y))
        return x+y

def main():
    print("Hello world.")
    a=A()
    z=a.sum(1,2)
    print(z)
    
if "__main__"==__name__:
    main()
    
```
**输出效果**
```
>pyone.exe main.py
Hello world.
I'm A.__init__
123
x=1
y=2
3
```
