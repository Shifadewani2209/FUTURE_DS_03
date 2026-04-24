<img width="1899" height="970" alt="image" src="https://github.com/user-attachments/assets/0a500798-fb8e-414f-aa09-eefc7e3707d0" />
<img width="1889" height="973" alt="image" src="https://github.com/user-attachments/assets/698be26f-eaf4-48d6-b066-50b2089acc10" />
<img width="1900" height="962" alt="image" src="https://github.com/user-attachments/assets/792e501a-6eb3-470f-815c-9cd0c164e25d" />


# FUTURE_DS_03 - Marketing Funnel & Conversion Performance Analysis

## Project Overview

This project analyzes marketing funnel data to identify conversion drop-offs, channel performance, campaign efficiency, and opportunities to improve lead-to-customer conversion.

The dashboard is built using Python and Streamlit and provides a client-ready view of funnel performance with KPIs, funnel visualization, drop-off analysis, channel ROI, campaign performance, and actionable recommendations.

## Internship Track

Data Science & Analytics  
Task 3: Marketing Funnel & Conversion Performance Analysis

## Objective

The main objective of this project is to analyze marketing funnel data and answer the following business questions:

- Where are users dropping off in the marketing funnel?
- Which channels generate the highest conversion rate?
- Which channels deliver the best ROI?
- Which campaigns generate the highest customers?
- How can the business improve lead-to-customer conversion?

## Tools and Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- VS Code
- GitHub

## Dataset

A synthetic marketing funnel dataset is generated using `generate_data.py`.

The dataset includes:

- Date
- Marketing Channel
- Campaign
- Region
- Visitors
- Leads
- Qualified Leads
- Customers
- Marketing Spend
- Revenue

## Key Metrics Analyzed

- Total Visitors
- Total Leads
- Qualified Leads
- Total Customers
- Overall Conversion Rate
- Cost Per Lead
- Customer Acquisition Cost
- Marketing ROI
- Funnel Drop-off Rate
- Channel-wise Conversion Rate
- Campaign Performance

## Dashboard Features

- Interactive date, channel, campaign, and region filters
- KPI cards
- Funnel visualization
- Funnel drop-off analysis
- Channel performance analysis
- Spend vs revenue comparison
- Campaign performance analysis
- Monthly conversion trend
- Automated insights
- Actionable business recommendations

## Key Insights

The dashboard helps identify:

- The strongest and weakest marketing channels
- The largest funnel leakage stage
- Channels with high customer acquisition cost
- Campaigns generating the most customers
- Monthly conversion performance trends

## Recommendations

Based on the funnel analysis, the business should:

1. Improve the funnel stage with the highest drop-off.
2. Increase investment in high-ROI channels.
3. Optimize weak-performing channels through better targeting and creatives.
4. Reduce customer acquisition cost using better segmentation.
5. Improve lead nurturing through email automation, retargeting, and personalized offers.

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/FUTURE_DS_03.git
cd FUTURE_DS_03

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Generate dataset
python generate_data.py

Step 4: Run Streamlit app
streamlit run app.py


---

## 5. Run the project

In terminal:

```bash
python generate_data.py
streamlit run app.py
