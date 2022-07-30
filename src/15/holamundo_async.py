#! /usr/bin/env python
import asyncio

async def main():
    await asyncio.sleep(1)
    print('Hola, Mundo.')
    
if __name__ == "__main__":
    asyncio.run(main())
