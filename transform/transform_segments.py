from datetime import datetime
import pandas as pd

def transform_customer_data(df):
    # Ensure datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Aggregate
    today = datetime.today()

    rfm = df.groupby("customer_id").agg({
        "order_date": lambda x: (today - x.max()).days,
        "order_id": "nunique",
        "line_total": "sum"
    }).reset_index()

    rfm.columns = ["customer_id", "recency_days", "frequency", "monetary"]
    rfm["monetary"] = rfm["monetary"].round(2)

    # Score RFM (1 = worst, 5 = best)
    rfm["r_score"] = pd.qcut(rfm["recency_days"], 5, labels=[5, 4, 3, 2, 1])
    rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["m_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])

    # Combine RFM score
    rfm["rfm_score"] = rfm["r_score"].astype(str) + rfm["f_score"].astype(str) + rfm["m_score"].astype(str)

    # Segment customers (simple rule-based mapping)
    def segment(row):
        if row["rfm_score"] in ["555", "554", "545"]:
            return "VIP"
        elif row["r_score"] in [4, 5] and row["f_score"] in [4, 5]:
            return "Loyal"
        elif row["r_score"] in [1, 2]:
            return "At-Risk"
        else:
            return "Regular"

    rfm["segment"] = rfm.apply(segment, axis=1)

    return rfm