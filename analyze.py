import airbnb
from bs4 import BeautifulSoup
import requests

example_link = "https://www.airbnb.co.in/rooms/753489119578553975?check_in=2023-12-15&check_out=2023-12-17&guests=1&adults=6&s=67&unique_share_id=e0a8ea9a-382b-4b9f-af19-34359fce4511"

# print("Enter link")
# input_link = input()

link = airbnb.strip_reviews_link(example_link)
content = airbnb.get_reviews(link)

print(content)