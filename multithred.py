import threading
import time as t
from concurrent.futures.thread import ThreadPoolExecutor

# from isapi.threaded_extension import ThreadPoolExtension


## Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds") 
    t.sleep(seconds)


# def main():
#     time = t.perf_counter()
#     # # Normal method to run function
#     # func(1)
#     # func(2)
#     # func(3)
#
#
#     # threading method to run function
#
#     t1 = threading.Thread(target = func, args = [1])
#     t2 = threading.Thread(target = func, args = [2])
#     t3 = threading.Thread(target = func, args = [3])
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     t1.join()
#     t3.join()
#
#     time1 = t.perf_counter()
#
#     print(time1 - time)

def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [1,3,2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()