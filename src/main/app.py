import logging
from fastapi import FastAPI
from src.main.controller.item import item_router


logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(item_router)
