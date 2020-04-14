from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message":"HelloWorld,FastAPI"}

# 运行uvicorn服务器， 地址，端口
if __name__ =='__main__':
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)

# uvicorn 1helloWorld.py:app --reload
""" 路由方法有:get、post、pathch、head、trace、delete
@app.post("/")
@app.put("/")
@app.options("/") """