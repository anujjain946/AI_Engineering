# from fastapi import FastAPI
# from schema import MongoDBSchema
# from config import collection

# app = FastAPI()


# # Create a new user
# @app.post("/mongodb_create")
# def create_user(user: MongoDBSchema):
#     dic = user.model_dump()
#     response = collection.insert_one(dic)

#     return {
#         "message": "User created successfully",
#         "id": str(response.inserted_id)
#     }
from fastapi import FastAPI
from schema import MongoDBSchema, UpdateMongoDBSchema
from config import collection

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI + MongoDB CRUD is working"}


# =========================
# CREATE
# =========================
@app.post("/mongodb_create")
def create_user(user: MongoDBSchema):
    try:
        dic = user.model_dump()
        response = collection.insert_one(dic)

        return {
            "message": "User created successfully",
            "id": str(response.inserted_id)
        }

    except Exception as e:
        return {"error": str(e)}


# =========================
# READ ALL USERS
# =========================
@app.get("/mongodb_users")
def get_users():
    try:
        users = list(collection.find())

        for user in users:
            user["_id"] = str(user["_id"])

        return users

    except Exception as e:
        return {"error": str(e)}


# =========================
# READ SINGLE USER BY user_id
# =========================
@app.get("/mongodb_user/{user_id}")
def get_single_user(user_id: int):
    try:
        user = collection.find_one({"user_id": user_id})

        if not user:
            return {"message": "User not found"}

        user["_id"] = str(user["_id"])
        return user

    except Exception as e:
        return {"error": str(e)}


# =========================
# UPDATE USER
# =========================
@app.put("/mongodb_update/{user_id}")
def update_user(user_id: int, user: UpdateMongoDBSchema):
    try:
        update_data = {k: v for k, v in user.model_dump().items() if v is not None}

        if not update_data:
            return {"message": "No data provided for update"}

        result = collection.update_one(
            {"user_id": user_id},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            return {"message": "User not found"}

        return {"message": "User updated successfully"}

    except Exception as e:
        return {"error": str(e)}


# =========================
# DELETE USER
# =========================
@app.delete("/mongodb_delete/{user_id}")
def delete_user(user_id: int):
    try:
        result = collection.delete_one({"user_id": user_id})

        if result.deleted_count == 0:
            return {"message": "User not found"}

        return {"message": "User deleted successfully"}

    except Exception as e:
        return {"error": str(e)}