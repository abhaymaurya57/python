# reverse=False
# for i in range(100):
#     if(reverse):
#         print("Odd")
#         # reverse=False
#     else:
#         print("Even")
#         # reverse=True
#     reverse = not reverse
    

import asyncio
async def async_iter():
   for num in range(4):
      await asyncio.sleep(2)
      yield num

async def main():
   async for res in aiter(async_iter()):
      print(res)
        
asyncio.run(main())


import asyncio
async def async_gentr():
   for num in range(4, 8):
      await asyncio.sleep(2)
      yield num

async def main():
   async for res in aiter(async_gentr()):
      print(res)

asyncio.run(main())