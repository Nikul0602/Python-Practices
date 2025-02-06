import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n * 5

print(fx(5))
print("Done for 5")
print(fx(10))
print("Done for 10")
print(fx(15))
print("Done for 15")

print(fx(5))
print("Done for 5")
print(fx(10))
print("Done for 10")
print(fx(15))
print("Done for 15")
