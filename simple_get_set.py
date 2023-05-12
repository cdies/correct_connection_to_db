# simple connect
import time
from multiprocessing import Pool
from redis.client import Redis

REQUESTS_COUNT = 100000

def test(i):
    client = Redis(host='0.0.0.0', port=6379)
    client.set(i, i)
    assert client.get(i) != i, 'wrong save'


start_time = time.time()

with Pool(16) as p:
    p.map(test, range(REQUESTS_COUNT))

sec = time.time() - start_time
print(f'time {sec:0.2f} seconds')

