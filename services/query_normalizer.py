from models.query import Query
from config import ONE_INDEXED

def from_ui_indexed(query: Query) -> Query:
    if ONE_INDEXED:
        return Query(
            op=query.op,
            target=query.target - 1,
            factor=query.factor,
            other=query.other - 1 if query.other is not None else None
        )
    return query

def to_ui_indexed(query: Query) -> Query:
    if ONE_INDEXED:
        return Query(
            op=query.op,
            target=query.target + 1,
            factor=query.factor,
            other=query.other + 1 if query.other is not None else None
        )
    return query
