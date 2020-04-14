
运行代码：vuicorn mian:app --reload
* 命令vuicorn mian:app指的：
    * 1、main.py文件模块
    * 2、app是FastAPI()创建的对象
    * 3、reload用于开发更改代码后重启服务器

### 步骤1：导入fastAPI、创建实例、定义路由
```python
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return{"message":"Hellow,World",}

```
细节
 > FastAPI是继承Starlette
网址：
 > https://baidu.com/items/foo
路径就是
 >/item/foo
路径的别称：路由、端点;路径能分离：问题、资源

## 步骤2：路径参数,注释类型
```python
from fastapi import FastAPI

app=FastAPI

@app.get("/item/{item_id}")
async def read_item(item_id:int):
    return{"item_id":item_id}
```
路径参数值item_id，作为参数传递给函数;运行的结构
>{"item_id":"foo"}
注释类型,item_id是整数类型
>def read_item(item_id:int):
* 会对数据进行转换和验证
>item_id="foo"是字符串，注解指明是整数，能转换就转换不能就这样会报错

### 如何抉择
当路径是固定，但又想接收参数获取其他：可添加新的路径，顺序原则
```python
from fastapi import FastAPI

app=FastAPI

@app.get("/users/me")
async def read_users_me():
    return{"user_id":"当前用户"}

@app.get("/users/{user_id}")
async def read_users(user_id:str):
    return{"user_id":"指定id用户"}
```
* 注意"user_id/{user_id}"在前，路径将理解为指定id当作me的id

### 预设定义值
接收参数的路径，可预设路径参数值
#### 创建Enum类
这里Enum是继承str和子类Enum
```python
from enum import Enum
from fastapi import FastAPI

class ModelName(str,Enum):
    alexnext="alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "深度学习 FTW!"}
    if model_name.vlaue == "lenet":
        reutn {"model_name": model_name, "message": "一些剩余值"}
```
声明路径参数，创建枚举类，并带类型注释的路径参数
>async def get_model(model_name:ModelName)
创建的枚举中枚举成员进行比较：
>if model_name == ModelName.alexnet: