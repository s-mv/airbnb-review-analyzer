# airbnb-review-analyzer
Analyze airbnb reviews in seconds!

## Setup
Once the repository is cloned simply run the following in your terminal.
```bash
pip install -r requirements.txt
python init.py
```
It is recommended to set up a virtual environment.

## Running the Analyzer
To run the review analyzer simply run:
```bash
python analyze.py
```
Analysis may take time, so hold tight!

## Sample Output
```
Enter link: (https://www.airbnb.co.in/rooms/[...])
https://www.airbnb.co.in/rooms/706869531113270964?check_in=2024-02-01&check_out=2024-02-06&guests=1&adults=1&viralityEntryPoint=1&s=76&unique_share_id=8cd13050-657b-4141-ada1-297aed2d0122
Preparing review link...
Scraping reviews... May take some time.
Analyzing reviews...
Analysis:
Positive reviews: 11
Negative reviews: 2
Neutral reviews: 3

Most positive review:
I recently stayed at Chitrit's Airbnb, and I must say, it was a great experience. The location was fantastic,  just a short 10 min walk will take you to plenty of restaurants and cafes nearby.As for the Airbnb space itself, it was stunning. The apartment was beautifully decorated, with a perfect mix of modern and classic elements. (it's a shared space)The bedroom was comfortable and cozy and the bathroom was neat and tidy.But what really stood out to me was the host's hospitality. They were always available to answer our questions promptly.Recommended!

Most negative review:
I booked this place after seeing the reviews but after spending two nights there , i am utterly disappointed. I have seen in reviews, this host counterattacking those who have raised or highlighted negative aspects of this place. Therefore, its important to hightlight that place is nothing but average and lacks basics. Moreover, hosts behaviour with occupants is atrocious. Now to list specifics.Shoes outside but no cleaniness in the room. Bedsheets were ragged, torn, had stains and strands of hair. Towels provided were most cheap quality with stains on them. No pressure in shower so  compromise washing with tap. When highlighted, his answer was pressure is less but it works. No sir it doesnot.But the worst part that has forced me to write this review was behaviour of this host who insecurely pesters me with two texts and call at 06.49 am on check out date to remind me that checkout is at 8 am. I am aware dude, i can read when i booked this place. This place not recom.
```

## TODO
1. Scraping reviews from Google and other sources for the same place.
2. Validation of scraped data.
3. Testing setup.
