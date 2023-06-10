# try : 
#     a = 10/0
# except:
#     print("Can't divided by 0")
# else:
#     print(f"All Correct, the answer is : {a/0}")
# finally:
#     print("All done")
    

# try:
#     f = open("file.txt","r")
# except Exception as e:
#     print(f"Error:{e}")
# else:
#     print("No error in the program")
# finally:
#     print("All done")


# try:
#     f = open("file.txt","w")
#     f.write("Writing into the file")
#     f.close()
# except Exception as e:
#     print(f"Error:{e}")
# else:
#     print("No error in the program")
# finally:
#     print("All done")



try:
    f = open("file1.txt","r")
    f.write("Writing into the file")
    f.close()
finally:
    print("All done") # This will exceute 