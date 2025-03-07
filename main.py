import asyncio

from my_tasker import start_bot

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("Exit")
