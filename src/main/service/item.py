import logging
from typing import Optional, List

from src.main.model.dto.request.item_request import ItemRequest
from src.main.model.dto.response.item_response import ItemResponse
import src.main.repository.item as item_repository

logger = logging.getLogger(__name__)


def save_item(item: ItemRequest) -> ItemResponse:
    logger.info(f"Saving Item: {item}")
    results = item_repository.save_item(item)
    return ItemResponse(**results[0])


def update_item(id: str, item: ItemRequest) -> ItemResponse:
    logger.info(f"Updating Item [{id=}]: {item}")
    results = item_repository.update_item(id, item)
    return ItemResponse(**results[0])


def delete_item(id: str) -> None:
    logger.info(f"Deleting Item with {id=}")
    results = item_repository.delete_item(id)
    return None


def find_item(id: str) -> Optional[ItemResponse]:
    logger.info(f"Looking for Item with {id=}")
    results = item_repository.find_item(id)
    return ItemResponse(**results[0]) if results else None


def find_all() -> List[ItemResponse]:
    logger.info(f"Getting all Items")
    results = item_repository.find_all()
    return [ItemResponse(**result) for result in results]
