# import multiprocessing
# def test():
#     print("This is my multiprocessing program")
# # test()
# if __name__ == '__main__':
#     m = multiprocessing.Process(target=test)
#     print("This is my main Program")
#     m.start()
#     m.join()



# import multiprocessing
# def square(n):
#     return(n**2)
# # print(square(5))
# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         output =pool.map(square,[1,56,7,54,64,342,22,3])
#         print(output)



# import multiprocessing
# def producer(q):
#     for i in range(10):
#         q.put(i)
# def consumer(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(item)
# if __name__ == '__main__':
#     queue = multiprocessing.Queue()
#     m1 = multiprocessing.Process(target=producer,args=(queue,))
#     m2 = multiprocessing.Process(target=consumer,args=(queue,))
#     m1.start()
#     m2.start()
#     queue.put("Anurag")
#     m1.join()
#     m2.join()



# import multiprocessing
# def square(index,value):
#     value[index] = value[index] ** 2
# if __name__ == '__main__':
#     arr = multiprocessing.Array('i',[2,3,4,5,6,7,8])
#     process = []
#     for i in range(7):
#         m = multiprocessing.Process(target=square,args=(i,arr))
#         process.append(m)
#         m.start()
#     for m in process:
#         m.join()
#     print(list(arr))



import multiprocessing
def sender(conn,msg):
    for i in msg:
        conn.send(i)
    conn.close()
def receiver(conn):
    while True:
        try:
            msg = conn.receiver()
        except Exception as e:
            print(e)
            break
        print(msg)
if __name__ == '__main__':
    msg = ["My name is Anurag","This is my message to Krsna","I am taking your class"]
    parent_conn,child_conn = multiprocessing.Pipe()
    m1 = multiprocessing.Process(target=sender,args=(child_conn,msg))
    m2 = multiprocessing.Process(target=receiver,args=(parent_conn,))
    m1.start()
    m2.start()
    m1.join()
    child_conn.close()
    m2.join()
    parent_conn.close()


