
# import requests
# from bs4 import BeautifulSoup
# import random

# def create_file(key_num):

#     records = [["N", "📝 Title", "🤓 Author", "💲Price"]]

#     topics = {
#         1: "952.1001_Books_You_Must_Read_Before_You_Die",
#         2: "2700.Science_Fiction_and_Fantasy_Must_Reads",
#         3: "1362.Best_History_Books_",
#         4: "281.Best_Memoir_Biography_Autobiography",
#         5: "7616.Motivational_and_Self_Improvement_Books"
#     }    
#     for n in range(3):
#         url = f"https://www.goodreads.com/list/show/{topics[key_num]}?page={n+1}"
#         r = requests.get(url)
#         c = r.text

#         soup = BeautifulSoup(c, 'html.parser')
#         data = soup.find_all("tr")

#         for index, row in enumerate(data, start=1):
#             book_info = row.find_all("span")
#             title = book_info[0].text
#             author = book_info[3].text
#             price = f"{round(random.uniform(9.0, 42.0), 2)}$"
#             item = [index, title, author, price]
#             records.append(item)

#     # workbook = Workbook()
#     # filename = "books.xlsx"
#     workbook = load_workbook("books.xlsx")
#     sheet = workbook["Sheet5"]
#     for item in records:
#         sheet.append(item) 
#     workbook.save("books.xlsx")
#     # workbook.save(filename)
#     # workbook.close