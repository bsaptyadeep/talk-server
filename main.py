# uvicorn main:app
# uvicorn main:app --reload

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

from config.database import collection_name
from schemas.wait_list_schema import list_serial


app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/waitlist")
async def get_wait_list():
    wait_list = list_serial(collection_name.find())
    return wait_list

@app.post("/waitlist")
async def add_user_to_waitlist(email):
    wait_list = list_serial(collection_name.find())
    is_email_unique = True
    for user in wait_list:
        if user["emailId"] == email:
            is_email_unique = False

    if is_email_unique == False:
        return { "message": "EmailId already added to Waitlist", "response": "success"}

    result = collection_name.insert_one({
        "emailId": email
    })

    # Check if insertion was successful
    if result.inserted_id:
        return { "message": "EmailId added to Waitlist", "response": "success"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add user email")

