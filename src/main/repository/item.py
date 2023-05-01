import logging
from typing import List

from sqlalchemy import select, delete, update, insert

from src.main.model.dto.request.item_request import ItemRequest
from src.main.model.item import ItemTable
from src.main.repository.utils import _execute_transaction

logger = logging.getLogger(__name__)


def save_item(item: ItemRequest) -> List[dict]:
    logger.debug(f"Persisting Item: {item}")
    statement = insert(ItemTable)\
        .values(**item.dict())\
        .returning(*ItemTable.fields())
    results = _execute_transaction(statement, commit=True)
    logger.debug(f"Persistence query result: {results}")
    return results


def update_item(id: str, item: ItemRequest) -> List[dict]:
    logger.debug(f"Updating Item [{id=}]: {item}")
    statement = update(ItemTable)\
        .filter(ItemTable.id == id)\
        .values(**item.dict())\
        .returning(*ItemTable.fields())
    results = _execute_transaction(statement, commit=True)
    logger.debug(f"Update query result: {results}")
    return results


def delete_item(id: str) -> List[dict]:
    logger.debug(f"Deleting Item with {id=}")
    statement = delete(ItemTable)\
        .filter(ItemTable.id == id)
    results = _execute_transaction(statement, commit=True)
    logger.debug(f"Delete query result: {results}")
    return results


def find_item(id: str) -> List[dict]:
    logger.debug(f"Looking for Item with {id=}")
    statement = select(*ItemTable.fields())\
        .filter(ItemTable.id == id)
    results = _execute_transaction(statement)
    logger.debug(f"Find query result: {results}")
    return results


def find_all() -> List[dict]:
    statement = select(*ItemTable.fields())
    results = _execute_transaction(statement)
    logger.debug(f"Find all query result: {results}")
    return results
