from pymongo.client_session import ClientSession
from pymongo.database import Collection, Database


def get_polls_collection(session: ClientSession) -> Collection:
    db: Database = session.client.get_database()
    polls: Collection = db.polls
    return polls
