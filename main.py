from datetime import date, timedelta
from agents.ingestion_agent import fetch_reviews
from agents.preprocessing_agent import clean_text
from agents.topic_extraction_agent import extract_topics
from agents.canonicalization_agent import TopicCanonicalizer
from agents.trend_agent import update_trends
from agents.report_agent import generate_report

APP_ID = "in.swiggy.android"
END_DATE = date(2024, 6, 30)
START_DATE = END_DATE - timedelta(days=29)

canonicalizer = TopicCanonicalizer()
trend_data = {}

daily_reviews = fetch_reviews(APP_ID, START_DATE, END_DATE)

for day, reviews in daily_reviews.items():
    for r in reviews:
        clean = clean_text(r)
        topics = extract_topics(clean)
        canonical_topics = [canonicalizer.canonicalize(t) for t in topics]
        update_trends(trend_data, day.strftime("%b %d"), canonical_topics)

dates = [(START_DATE + timedelta(days=i)).strftime("%b %d") for i in range(30)]

generate_report(
    trend_data,
    dates,
    "output/swiggy_trend_2024_06_30.csv"
)
