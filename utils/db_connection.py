from prisma import Prisma

async def prismaDB():
  db = Prisma()
  await db.connect()
  try:
    yield db
  finally:
    await db.disconnect()