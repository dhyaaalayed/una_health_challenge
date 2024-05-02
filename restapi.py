from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from database_model import load_data, filter_by_user_id_and_start_stop_timestamps, filter_by_glucose_id


DF = load_data()


app = FastAPI()


@app.get("/api/v1/levels/")
async def get_glucose_level(user_id: str, page_size: int, sort: bool, sort_ascending:bool, limit: int, start_timestamps: Optional[datetime] = None, stop_timestamps: Optional[datetime] = None) -> dict:
    result = filter_by_user_id_and_start_stop_timestamps(DF, user_id, page_size, sort, sort_ascending, limit, start_timestamps, stop_timestamps)
    return {"message": result}


@app.get("/api/v1/levels/id/")
async def get_glucose_level(glucose_id: int) -> dict:
    result = filter_by_glucose_id(DF, glucose_id)
    return {"message": result}



if __name__ == "__main__":
    uvicorn.run("restapi:app", host="0.0.0.0", port=5000, reload=True)