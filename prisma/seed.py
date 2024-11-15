import asyncio
from datetime import datetime
from prisma import Prisma

tasks = [
    {
        "id": "cm3f558ak0000oknda2nktdwv",
        "description": "Learn backend",
        "completed": False
    },
    {
        "id": "cm3f558b10001oknd7doffho5",
        "description": "Learn acoustic guitar",
        "completed": False
    },
    {
        "id": "cm3f558b80002oknd4uso6uvc",
        "description": "Create a starter project",
        "due": datetime(2024, 11, 12),
        "completed": True
    }
]

async def seed() -> None:
  db = Prisma()
  await db.connect()
  print("Running seed...")

  await db.task.delete_many()
  await db.task.create_many(data=tasks, skip_duplicates=True)
  

  print("Database seeded!")
  await db.disconnect()

if __name__ == "__main__":
  asyncio.run(seed())