def read_titles():
    with open('small.txt', 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def get_article(title):
    with open('small.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() == title:
                content = ''
                for line in file:
                    if line.startswith('!'):
                        break
                    content += line
                return content.strip()
    return None

def calculate_average_letter_count():
    total_letter_count = 0
    distinct_letters = set()
    article_count = 0

    for title in read_titles():
        article = get_article(title)
        article_letters = set(article)
        distinct_letters.update(article_letters)
        total_letter_count += len(article_letters)
        article_count += 1

    if article_count > 0:
        average_letter_count = total_letter_count / len(distinct_letters)
        return average_letter_count
    else:
        return 0

average = calculate_average_letter_count()
print(f"Średnia liczba liter na artykuł: {average}")


# kod dzialajacy ze strona wikipedii

# import requests
# from bs4 import BeautifulSoup
#
# def get_article_length(title):
#     url = f"https://pl.wikipedia.org/wiki/{title}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     content = soup.find(id="mw-content-text").get_text()
#     content = content.replace("\n", "").replace("\r", "")
#     content = " ".join(content.split())
#     return len(content)
#
# def calculate_average_length(articles):
#     total_length = 0
#     for article in articles:
#         length = get_article_length(article)
#         total_length += length
#     if len(articles) > 0:
#         average_length = total_length / len(articles)
#         return average_length
#     else:
#         return 0
#
# with open("small.txt", "r") as file:
#     article_titles = [line.strip() for line in file]
#
# average_length = calculate_average_length(article_titles)
# print(f"Średnia liczba liter na artykuł: {average_length}")
