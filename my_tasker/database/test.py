import asyncio

from database import db

db = db(myUrl="", database="")

async def main():
    try: 
        await db.ping()
        print("CORRECT!")
    except Exception as e:
        print("Error with db - " + e)

if __name__ == "__main__":
    asyncio.run(main())