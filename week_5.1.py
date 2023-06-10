# import json

# data = {
#     "name" : "anurag",
#     "mail" : "abc@gamil.com",
#     "phone" : 3847837523,
#     "hobby" : "coding",
#     "subjects" : ["Data Science","Maths","AIML"]
#         }

# with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test.json","w") as f:
#     json.dump(data,f)

# with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test.json") as f:
#     data1 = json.load(f)
# print(data1["name"])





import csv

data = [
        ["Name","Email","Phone Number"],
        ["Anurag","abc@gmail.com","9233874831"],
        ["Krsna","bfd@gmail.com","8237826334"],
        ]

# with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test.csv","w") as f:
#     writer = csv.writer(f)
#     for i in data:
#         writer.writerow(i)

# with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test.csv","r") as f:
#     read_data = csv.reader(f)
#     for i in read_data:
#         print(i)

# with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test.bin","wb") as f:
#     f.write(b"\x01\x02\x031234")

# with open(r"/Users/anuragpareek/Downloads/IMPACT 2.0/Week-5-Python/test.bin","rb") as f:
#     print(f.read())
