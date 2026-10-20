from fastapi import FastAPI, HTTPException
from connection import localsession
from classes import CreateUser, User, PatchUser
from sqlalchemy import select, insert, delete, update

app = FastAPI()

@app.get("/orm/users")
def get_users():
    with localsession() as db:
        result = db.scalars(select(User)).all()
    return [{
        "id": res.id,
        "name": res.name,
        "age": res.age
    }
    for res in result
    ]
        
        
@app.post("/orm/user")
def post_user(myuser: CreateUser):
    with localsession() as db:
        post_result = db.execute(insert(User).values(name=myuser.name, age= myuser.age).returning(User.id, User.name, User.age))
        res = post_result.one()
        db.commit()
    return {
        "id": res.id,
        "name": res.name,
        "age": res.age
    }

@app.delete("/orm/user/{id}")
def delete_user(id: int):
    with localsession() as db:
        result = db.execute(delete(User).where(User.id == id))
        if result.rowcount == 0:
                    raise HTTPException(status_code= 404, detail= "Not found")
        db.commit()

    return f"succsesful deleted user which id: {id}"

@app.patch("/orm/user/{id}")
def patch_user(id: int, patch_user: PatchUser):
    with localsession() as db:
        changes = patch_user.model_dump(exclude_unset=True)

        if not changes:
             raise HTTPException(status_code=400, detail = "incorect input")
        if any(value is None for value in changes.values()):
             raise HTTPException(status_code=422, detail = "values cant be None")
             
        patch_result = db.execute(update(User).where(User.id == id).values(**changes).returning(User.id, User.name, User.age))

        end_result_patch = patch_result.one_or_none()

        if  end_result_patch is None:
                    raise HTTPException(status_code= 404, detail= "Not found")

        db.commit()

    return {"id": end_result_patch.id, "name": end_result_patch.name, "age": end_result_patch.age}

@app.put("/orm/user/{id}")
def put_user(id: int, user: CreateUser):
      with localsession() as db:
                  
            result = db.execute(update(User).where(User.id == id).values(name= user.name,age= user.age).returning(User.id, User.name, User.age))

            res = result.one_or_none()

            if res is None:
                raise HTTPException(status_code=404, detail= "not found")
            
            db.commit()

            return {
                  "id": res.id,
                  "name": res.name,
                  "age": res.age
            }


        

    
    


