import asyncio

from my_tasker.database import client


async def main():
    try:
        result = await client.ping()
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
