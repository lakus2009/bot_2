# file = open("students.txt", "w")
# file.write("daniel")
# file.close()
# # file = open("students.txt", "r")
# content = file.read()
# print(type(content))
# print(content)
# file.close()

#
#
# file = open("students.txt", "r")
# content = file.readlines()
# print(content)
# file.close()

# my_list = ["aman\n", "laura\n", "daniel\n", "sayan"]
# file = open("students.txt", "w")
# content = file.writelines(my_list)
# print(content)
# file.close()



# file = open("students.txt", "a")
# file.write("\nhello world")
# # file.close()
# file = open("students.txt", "r")
# content = file.readlines()
# print(content)
# for line in content:
#     new_line = line.replace("\n", "")
# #     print(line)
# # file.close()
# # file = open("fruits.py","w")
# # content = file.writelines("apples banana cherry pineapple grapes")
# # file.write("banana")
# # file.write("cherry")
# # file.write("pineapple")
# # file.write("grapes")
# # file.close()
# with open("fruits.py", "w") as f:
#     for i in range(20):
#         f.write(str(i) + "\n")
#         if i % 2 == 0 and i != 0:
#             print(i)
#
#
#
# with open("fruits.py", "r") as f:
#     f.write(str(i) + "\n")
#
# import json
# import requests
# from certifi import contents
#
# url = "http://api.kanye.rest"
# # key = {'quote and values = 'You basically can say anything to someone on an email or text as long as you put LOL at the end.'}
#
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# if response.status_code == 200:
#     content = json.loads(response.text)
#     print(content)
#     count = 0
#
#
#     print(content.values())
# try:
#     while count < 50:
#         count += 1
#
#
#
# except Exception as e:
#     print(e)
#
# try:
#     with open("quotes.txt", "r") as f:
#         f.readlines()
#
#
#     with open("quotes.txt", "w") as f:
#         f.write()
# except Exception as e:
#     print(e)



