import concurrent.futures
from multiprocessing import Process
import requests
# impprt



def downloadFile(url, name):
    print(f"Started Download for {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading of {name}")

url = "https://picsum.photos/2000/3000"

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:

        l = [url for i in range (25)]
        l1 = [i for i in range (25)]
        results = executor.map(downloadFile, l, l1)
        for r in results:
            print(r)
# pros = []
#
# for i in range (10):
#     i = i + 1
#     # downloadFile(url, i)
#     if __name__ == "__main__":
#         p = Process(target=downloadFile, args = [url, i])
#         p.start()
#         pros.append(p)
#
# for p in pros:
#     p.join()

