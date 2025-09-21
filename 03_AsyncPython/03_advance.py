import asyncio

async def process1():
    print("Execute: Step 1")
    await asyncio.sleep(5)
    print("Execute: Step 2")

async def process2():
    print("Execute: Step 3")
    await asyncio.sleep(5)
    print("Execute: Step 4")

async def main():
    
    tasks = await asyncio.gather(process1(), process2())
    print("\nAll Main tasks completed.")
    
    # await process1()
    # await process2()

await main()