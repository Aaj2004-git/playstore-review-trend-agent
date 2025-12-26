def update_trends(trend_data, date, topics):
    for topic in topics:
        trend_data.setdefault(topic, {})
        trend_data[topic][date] = trend_data[topic].get(date, 0) + 1
