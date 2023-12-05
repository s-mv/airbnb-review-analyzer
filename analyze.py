import airbnb
import sentiment

print("Enter link: (https://www.airbnb.co.in/rooms/[...])")
input_link = input()

print("Preparing review link...")
link = airbnb.strip_reviews_link(input_link)
print("Scraping reviews... May take some time.")
content_bnb = airbnb.get_reviews(link)  # TODO: also scrape google

print("Analyzing reviews...")
# the real deal
most_positive_review: str = ""
most_negative_review: str = ""
most_positive: float = 0
most_negative: float = 0
num_positive = 0
num_negative = 0
num_neutral = 0

for text in content_bnb:
    score = sentiment.analyze(text)
    if score > most_positive:
        most_positive = score
        most_positive_review = text
    elif score < most_negative:
        most_negative = score
        most_negative_review = text

    if score > 0.5:
        num_positive += 1
    elif -0.5 > score:
        num_negative += 1
    else:
        num_neutral += 1

print(
    (
        "Analysis:\n"
        f"Positive reviews: {num_positive}\n"
        f"Negative reviews: {num_negative}\n"
        f"Neutral reviews: {num_neutral}\n\n"
        "Most positive review:\n"
        f"{most_positive_review}\n\n"
        "Most negative review:\n"
        f"{most_negative_review}\n"
    )
)
