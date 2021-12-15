from __future__ import annotations
from fastapi import APIRouter, File, UploadFile
from starlette.responses import FileResponse

from app.api.readPlate.main import readPlateNumber

router = APIRouter()


@router.get("/")
async def home() -> str:
    return FileResponse('./app/routes/views/index.html')


@router.post("/read-plate")
async def home(file: UploadFile = File(...)) -> str:
    return readPlateNumber(await file.read())
