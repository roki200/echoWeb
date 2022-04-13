from databases import Database
from config import DB_URL


CREATE TABLE messages (
id SERIAL PRIMARY KEY,
telegram_id INTEGER NOT NULL,
text text NOT NULL
);


async def read(user_id):
    results = await database.fetch_all('SELECT text '
                                       'FROM messages '
                                       'WHERE telegram_id = :telegram_id ',
                                       values={'telegram_id': user_id})
    return [next(result.values()) for result in results]
  
database = Database(DB_URL)
