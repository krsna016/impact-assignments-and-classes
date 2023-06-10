# import threading
# def test(id):
#     print("program Starts %d" %id)
# # test(55)
# thread = [threading.Thread(target=test,args=(i,)) for i in range(10)]
# for t in thread:
#     t.start()
# print(thread)



# import threading
# import urllib.request # To take file from internet
# def file_download(url,file_name):
#     urllib.request.urlretrieve(url,file_name)
# url_list = ["https://gist.githubusercontent.com/khaykov/a6105154becce4c0530da38e723c2330/raw/41ab415ac41c93a198f7da5b47d604956157c5c3/gistfile1.txt",
#             "https://github.com/kennyn510/random-lists/blob/master/websites.txt",
#             "https://github.com/itsfoss/text-files/blob/master/agatha.txt"]
# file_name_list = ["data1.txt","data2.txt","data3.txt"]
# thread = [threading.Thread(target=file_download,args=(url_list[i],file_name_list[i])) for i in range(len(url_list))]
# for i in thread:
#     i.start()



# import time
# import threading
# def test(id):
#     for i in range(10):
#         print("Test1 %d printing %d : %s" %(id,i,time.ctime()))
#         time.sleep(1) # Let's comment this and see the changes # Context switching
# thread = [threading.Thread(target=test,args=(i,)) for i in range(3)]
# for i in thread:
#     i.start()


import threading,time
shared_var = 0
lock_var = threading.Lock()
def test(id):
    global shared_var
    with lock_var:
        shared_var = shared_var + 1
        print("Test ID is %d has increased the shared variable by %d" %(id, shared_var))
        time.sleep(1)
thread = [threading.Thread(target=test,args=(i,)) for i in range(3)]
# print(lock_var)
for i in thread:
    i.start()