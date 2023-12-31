# import time

# def job(number):
#   print(f'Job {number} started')
#   time.sleep(1) # 매우 오래 걸리는 작업, 일반 sleep은 CPU를 쉬게함 동기 프로그래밍 특징
#   print(f'Job {number} completed')

# job(1)
# job(2)
# job(3)

# import asyncio

# async def job(number):
#   print(f'Job {number} started')
#   await asyncio.sleep(1)
#   print(f'Job {number} completed')

# async def main():
#   await asyncio.gather(job(1), job(2), job(3)) # job1, job2 job3가 동시에 실행됨

# asyncio.run(main())
# print('hello world')
import time
import asyncio #비동기도 동기화 가능 

async def job(number):
    print(f'Job {number} started')
    await asyncio.sleep(1)
    print(f'Job {number} completed')

asyncio.run(job(1))
asyncio.run(job(2))
asyncio.run(job(3))

# 코루틴 : async를 붙인 코루틴 함수. await 키워드를 만나면 코루틴 실행 잠시 중단

async def job():
    print('job')
    return 100

print(job) #<function job at 0x00000246765F6480>
# print(await job()) # await가 함수밖에 사용하는거 허용되지 않음

# async def : 코루틴함수를 선언하는데 사용. 이 함수를 비동기적으로 실행할수 있는 코루틴 객체소환
# await : 코루틴의 작업이 완료될 때까지 기다린 후 결과 반환
# asyncio.run() : 코루틴을 실행하는 함수. 이벤트 루프 생성, 주어진 코루틴을 실행한 후 이벤트 루프 닫음
# asynciio.gather() : 여러 코루틴을 동시에 실행하도록 스케줄링하는 함수