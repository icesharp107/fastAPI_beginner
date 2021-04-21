from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000/phone/12345
@app.get("/phone/{phone}")
async def get_phone(phone:int):
    return {"phone":phone}

# http://127.0.0.1:8000/user?user_id=136678
@app.get("/user")
async def get_user(user_id:int):
    return {"user_id":user_id}

# http://127.0.0.1:8000/user/12?mod=12
@app.get("/user/{user_id}")
async def user_mod(user_id:int,mod:int):
    return {
        "user_id":user_id,
        "mod":mod
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8000)