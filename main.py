from datetime import datetime

from data import users_data, support_data
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model import UserResponse, UserData, UserCreateResponse, UserCreateData, UserUpdatedResponse

app = FastAPI()


@app.get("/api/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    try:
        user_data = users_data[user_id]
    except KeyError:
        return JSONResponse(status_code=404, content={})
    return UserResponse(data=user_data, support=support_data)


@app.post("/api/users/", response_model=UserCreateResponse)
async def create_user(user: UserCreateData):
    current_id = max(users_data.keys()) + 1
    formatted_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    users_data[current_id] = UserData(id=current_id, email='', first_name=user.name, last_name='', avatar='',
                                      job=user.job)
    return UserCreateResponse(name=user.name, job=user.job, id=str(current_id), createdAt=formatted_date)


@app.put("/api/users/{user_id}", response_model=UserUpdatedResponse)
async def update_user(user_id: int, user: UserCreateData):
    try:
        exist_user = users_data[user_id]
    except KeyError:
        return JSONResponse(status_code=404, content={})
    users_data[user_id] = UserData(id=exist_user.id,
                                   email=exist_user.email,
                                   first_name=user.name,
                                   last_name=exist_user.last_name,
                                   avatar=exist_user.avatar,
                                   job=user.job)
    formatted_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return UserUpdatedResponse(name=user.name, job=user.job, updatedAt=formatted_date)


@app.delete("/api/users/{user_id}")
async def delete_user(user_id: int):
    try:
        del users_data[user_id]
    except KeyError:
        return JSONResponse(status_code=404, content={})
    return JSONResponse(status_code=204, content=None)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
