from google_play_scraper import reviews
from datetime import datetime

def fetch_reviews(app_id, start_date, end_date):
    result, _ = reviews(
        app_id,
        lang='en',
        country='in',
        count=5000
    )

    daily_reviews = {}
    for r in result:
        review_date = r['at'].date()
        if start_date <= review_date <= end_date:
            daily_reviews.setdefault(review_date, []).append(r['content'])

    return daily_reviews
