from typing import List

from fastapi import APIRouter

from src.main.model.dto.request.item_request import ItemRequest
from src.main.model.dto.response.item_response import ItemResponse

import src.main.service.item as item_service

item_router = APIRouter(prefix="/item")


@item_router.get("")
async def find_all() -> List[ItemResponse]:
    return item_service.find_all()


@item_router.get("/{item_id}")
async def find_by_id(item_id: str) -> ItemResponse:
    return item_service.find_item(item_id)


@item_router.put("")
async def create(new_item: ItemRequest) -> ItemResponse:
    return item_service.save_item(new_item)


@item_router.put("/{item_id}")
async def update(item_id: str, updated_item: ItemRequest) -> ItemResponse:
    return item_service.update_item(item_id, updated_item)


@item_router.delete("/{item_id}")
async def delete(item_id: str) -> None:
    return item_service.delete_item(item_id)
