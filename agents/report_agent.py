import pandas as pd

def generate_report(trend_data, dates, output_path):
    df = pd.DataFrame(index=trend_data.keys(), columns=dates)

    for topic, counts in trend_data.items():
        for d in dates:
            df.loc[topic, d] = counts.get(d, 0)

    df.fillna(0, inplace=True)
    df.to_csv(output_path)
