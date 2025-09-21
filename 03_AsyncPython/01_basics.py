import asyncio

async def process1():
    print("Execute: Step 1")
    await asyncio.sleep(5)
    print("Execute: Step 2")

async def process2():
    print("Execute: Step 3")
    await asyncio.sleep(5)
    print("Execute: Step 4")

# Begin Event Loop1
# asyncio.run(process1())
# use await process1() directly in Databricks notebooks, since the event loop is already running.
await process1()

# Begin Event Loop2
await process2()
