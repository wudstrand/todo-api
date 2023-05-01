import logging
from src.main.common.connection import Connection

logger = logging.getLogger(__name__)


def _execute_transaction(statement, *, returns_data=True, commit=False):
    connection = Connection()
    session = connection.get_session()
    try:
        row = session.execute(statement)
        if commit:
            session.commit()
        keys = row.keys()
        data = row.all() if returns_data else []
        results = [dict(zip(keys, res)) for res in data]
    except Exception as e:
        session.rollback()
        session.close()
        raise e
    session.close()
    return results
