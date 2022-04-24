import asyncio


async def fetch_data():
    print ('start fetching')
    await asyncio.sleep(2)
    print ('done fetching')
    return {'data': 1}
async def print_numbers():

    for i in range(10):
        print(i)
        # await asyncio.sleep(0.25)

        # If we change this to 0.5 print_numbers
        '''
        will run along the same time as the fetch_data() 
        
        '''
        await asyncio.sleep(0.5)


async def main():

    #These 2 codes run concurrently here
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # We must use await values for to wait for the task1 to finish
    value = await task1

    print(value)
    await task2
asyncio.run(main())