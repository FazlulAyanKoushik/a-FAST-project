import asyncio

from app.core.db import init_db, get_db


async def migrate_users():
    await init_db()
    db = get_db()
    # Example: Create an index on the user_name field for faster queries
    await db.users.create_index("user_name", unique=True)


if __name__ == "__main__":
    asyncio.run(migrate_users())
