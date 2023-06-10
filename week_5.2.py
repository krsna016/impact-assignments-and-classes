import io
with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test2.txt","wb") as f:
    file = io.BufferedWriter(f)
    file.write(b"Multithreading involves the use of multiple threads within a single process. Threads are lightweight units of execution that can be scheduled to run concurrently within a program. Multiple threads share the same memory space, allowing them to access shared data and communicate more easily.\n")
    file.write(b"This is my second line")
    file.flush()

with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test2.txt","rb") as f:
    file = io.BufferedReader(f)
    print(file.read(100)) # 100 = 100 bytes