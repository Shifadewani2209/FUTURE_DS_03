import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

os.makedirs("data", exist_ok=True)

channels = ["Google Ads", "Facebook Ads", "Instagram", "LinkedIn", "Email", "Organic Search"]
campaigns = ["Spring Launch", "AI Webinar", "Free Trial Push", "Festive Offer", "Lead Magnet"]
regions = ["North", "South", "East", "West", "Central"]

rows = []

start_date = datetime(2025, 1, 1)

for i in range(450):
    date = start_date + timedelta(days=np.random.randint(0, 180))
    channel = np.random.choice(channels)
    campaign = np.random.choice(campaigns)
    region = np.random.choice(regions)

    visitors = np.random.randint(800, 6000)

    # Channel-based conversion behavior
    if channel == "Google Ads":
        lead_rate = np.random.uniform(0.18, 0.30)
        qualified_rate = np.random.uniform(0.45, 0.65)
        customer_rate = np.random.uniform(0.25, 0.40)
        cost_per_visitor = np.random.uniform(0.8, 1.6)

    elif channel == "Facebook Ads":
        lead_rate = np.random.uniform(0.12, 0.24)
        qualified_rate = np.random.uniform(0.35, 0.55)
        customer_rate = np.random.uniform(0.16, 0.30)
        cost_per_visitor = np.random.uniform(0.5, 1.2)

    elif channel == "Instagram":
        lead_rate = np.random.uniform(0.14, 0.26)
        qualified_rate = np.random.uniform(0.30, 0.50)
        customer_rate = np.random.uniform(0.14, 0.28)
        cost_per_visitor = np.random.uniform(0.4, 1.0)

    elif channel == "LinkedIn":
        lead_rate = np.random.uniform(0.10, 0.20)
        qualified_rate = np.random.uniform(0.55, 0.75)
        customer_rate = np.random.uniform(0.28, 0.45)
        cost_per_visitor = np.random.uniform(1.2, 2.5)

    elif channel == "Email":
        lead_rate = np.random.uniform(0.22, 0.35)
        qualified_rate = np.random.uniform(0.50, 0.70)
        customer_rate = np.random.uniform(0.30, 0.50)
        cost_per_visitor = np.random.uniform(0.1, 0.4)

    else:
        lead_rate = np.random.uniform(0.16, 0.28)
        qualified_rate = np.random.uniform(0.45, 0.65)
        customer_rate = np.random.uniform(0.22, 0.38)
        cost_per_visitor = np.random.uniform(0.05, 0.2)

    leads = int(visitors * lead_rate)
    qualified_leads = int(leads * qualified_rate)
    customers = int(qualified_leads * customer_rate)

    spend = visitors * cost_per_visitor
    revenue = customers * np.random.randint(120, 500)

    rows.append({
        "date": date.strftime("%Y-%m-%d"),
        "channel": channel,
        "campaign": campaign,
        "region": region,
        "visitors": visitors,
        "leads": leads,
        "qualified_leads": qualified_leads,
        "customers": customers,
        "marketing_spend": round(spend, 2),
        "revenue": round(revenue, 2)
    })

df = pd.DataFrame(rows)
df.to_csv("data/marketing_funnel_data.csv", index=False)

print("Dataset created successfully: data/marketing_funnel_data.csv")