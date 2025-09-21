## Co-routine withint a co-routine
import asyncio

async def process1():
    print("Execute: Step 1")
    await asyncio.sleep(5)
    result = await process2()
    print(f"Process 2 results: {result}")
    print("Execute: Step 2")

async def process2():
    print("Execute: Step 3")
    await asyncio.sleep(5)
    print("Execute: Step 4")
    return "Process 2 completed sucessfully!"

# Begin Event Loop
# use await process1() directly in Databricks notebooks, since the event loop is already running.
await process1()
