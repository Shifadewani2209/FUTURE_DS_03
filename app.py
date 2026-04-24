import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Marketing Funnel Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# Navy Blue Premium Theme Colors
# -------------------------------------------------------
MIDNIGHT = "#020617"
NAVY = "#071A2F"
DEEP_NAVY = "#0B1F3A"
STEEL_BLUE = "#1E3A5F"
OCEAN_BLUE = "#2563EB"
SKY_BLUE = "#38BDF8"
ICE_BLUE = "#E0F2FE"
SOFT_BLUE = "#DBEAFE"
PLATINUM = "#E5E7EB"
MUTED = "#94A3B8"
WHITE = "#FFFFFF"
INK = "#0F172A"


# -------------------------------------------------------
# Global Styling
# -------------------------------------------------------
st.markdown(f"""
<style>
    .stApp {{
        background:
            radial-gradient(circle at top left, rgba(56,189,248,0.16), transparent 28%),
            radial-gradient(circle at top right, rgba(37,99,235,0.18), transparent 30%),
            linear-gradient(135deg, {MIDNIGHT} 0%, {NAVY} 42%, {DEEP_NAVY} 100%);
        color: {PLATINUM};
    }}

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(180deg, #020617 0%, #061B33 100%);
        border-right: 1px solid rgba(56,189,248,0.22);
    }}

    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: #E5E7EB !important;
    }}

    /* Sidebar filter input boxes */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {{
        background: rgba(2, 6, 23, 0.78) !important;
        border: 1px solid rgba(56,189,248,0.16) !important;
        border-radius: 16px !important;
        min-height: 52px !important;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
    }}

    section[data-testid="stSidebar"] div[data-baseweb="select"] input {{
        color: #E5E7EB !important;
    }}

    /* Subtle selected chips instead of red */
    section[data-testid="stSidebar"] span[data-baseweb="tag"] {{
        background: linear-gradient(135deg, rgba(191,219,254,0.18), rgba(96,165,250,0.22)) !important;
        border: 1px solid rgba(147,197,253,0.28) !important;
        border-radius: 12px !important;
        color: #DCEAFE !important;
        box-shadow: none !important;
    }}

    section[data-testid="stSidebar"] span[data-baseweb="tag"] span {{
        color: #EAF3FF !important;
        font-weight: 650 !important;
    }}

    section[data-testid="stSidebar"] span[data-baseweb="tag"] svg {{
        fill: #BFDBFE !important;
    }}

    section[data-testid="stSidebar"] span[data-baseweb="tag"] div[role="button"] {{
        background: transparent !important;
        border-radius: 8px !important;
    }}

    section[data-testid="stSidebar"] span[data-baseweb="tag"] div[role="button"]:hover {{
        background: rgba(255,255,255,0.08) !important;
    }}

    div[role="listbox"] {{
        background: #0B1F3A !important;
        border: 1px solid rgba(56,189,248,0.18) !important;
        border-radius: 14px !important;
    }}

    div[role="option"] {{
        color: #E5E7EB !important;
        background: transparent !important;
    }}

    div[role="option"]:hover {{
        background: rgba(56,189,248,0.10) !important;
    }}

    .hero {{
        background:
            linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.025)),
            radial-gradient(circle at top right, rgba(56,189,248,0.20), transparent 38%),
            linear-gradient(135deg, rgba(14,165,233,0.13), rgba(37,99,235,0.08));
        border: 1px solid rgba(56,189,248,0.30);
        border-radius: 30px;
        padding: 36px 38px;
        margin-bottom: 30px;
        box-shadow:
            0 30px 90px rgba(0,0,0,0.45),
            inset 0 1px 0 rgba(255,255,255,0.10);
    }}

    .eyebrow {{
        color: {SKY_BLUE};
        font-size: 13px;
        font-weight: 900;
        letter-spacing: 1.8px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }}

    .title {{
        color: #FFFFFF;
        font-size: 46px;
        font-weight: 950;
        line-height: 1.08;
        margin-bottom: 14px;
        letter-spacing: -1px;
    }}

    .subtitle {{
        color: #CBD5E1;
        font-size: 17px;
        line-height: 1.75;
        max-width: 1000px;
    }}

    .section-header {{
        color: #FFFFFF;
        font-size: 28px;
        font-weight: 950;
        margin-top: 38px;
        margin-bottom: 10px;
        letter-spacing: -0.4px;
    }}

    .section-header::after {{
        content: "";
        display: block;
        width: 82px;
        height: 3px;
        margin-top: 9px;
        border-radius: 999px;
        background: linear-gradient(90deg, {SKY_BLUE}, {OCEAN_BLUE});
    }}

    .section-subtext {{
        color: {MUTED};
        font-size: 15px;
        margin-top: 0px;
        margin-bottom: 18px;
        line-height: 1.6;
    }}

    .metric-card {{
        background:
            linear-gradient(145deg, #FFFFFF 0%, #F8FAFC 100%);
        padding: 23px;
        border-radius: 22px;
        box-shadow:
            0 22px 55px rgba(0,0,0,0.28),
            inset 0 1px 0 rgba(255,255,255,0.90);
        border: 1px solid rgba(56,189,248,0.25);
        min-height: 134px;
        position: relative;
        overflow: hidden;
    }}

    .metric-card::before {{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        height: 5px;
        width: 100%;
        background: linear-gradient(90deg, {SKY_BLUE}, {OCEAN_BLUE}, {STEEL_BLUE});
    }}

    .metric-label {{
        color: #475569;
        font-size: 12.5px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }}

    .metric-value {{
        color: {INK};
        font-size: 32px;
        font-weight: 950;
        margin-top: 9px;
    }}

    .metric-note {{
        color: #64748B;
        font-size: 13px;
        font-weight: 650;
        margin-top: 9px;
        line-height: 1.45;
    }}

    .chart-card {{
        background:
            linear-gradient(145deg, #FFFFFF 0%, #F8FAFC 100%);
        border-radius: 24px;
        padding: 20px 20px 10px 20px;
        border: 1px solid rgba(56,189,248,0.25);
        box-shadow:
            0 25px 65px rgba(0,0,0,0.32),
            inset 0 1px 0 rgba(255,255,255,0.85);
        margin-bottom: 16px;
    }}

    .insight-box {{
        background:
            linear-gradient(145deg, #FFFFFF 0%, #F8FAFC 100%);
        color: #111827;
        padding: 21px 24px;
        border-radius: 20px;
        box-shadow: 0 22px 55px rgba(0,0,0,0.28);
        border-left: 7px solid {OCEAN_BLUE};
        border-top: 1px solid rgba(56,189,248,0.25);
        margin-bottom: 15px;
        font-size: 16.5px;
        line-height: 1.75;
        font-weight: 650;
    }}

    .insight-box b {{
        color: #020617;
        font-weight: 950;
    }}

    .warning-box {{
        background:
            linear-gradient(145deg, #EFF6FF 0%, #DBEAFE 100%);
        color: #1E3A8A;
        padding: 21px 24px;
        border-radius: 20px;
        box-shadow: 0 22px 55px rgba(0,0,0,0.25);
        border-left: 7px solid {SKY_BLUE};
        border-top: 1px solid rgba(56,189,248,0.35);
        margin-bottom: 15px;
        font-size: 16.5px;
        line-height: 1.75;
        font-weight: 650;
    }}

    .warning-box b {{
        color: #172554;
        font-weight: 950;
    }}

    .recommendation-box {{
        background:
            linear-gradient(145deg, #F0F9FF 0%, #E0F2FE 100%);
        color: #0C4A6E;
        padding: 21px 24px;
        border-radius: 20px;
        box-shadow: 0 22px 55px rgba(0,0,0,0.25);
        border-left: 7px solid {OCEAN_BLUE};
        border-top: 1px solid rgba(37,99,235,0.25);
        margin-bottom: 15px;
        font-size: 16.5px;
        line-height: 1.75;
        font-weight: 650;
    }}

    .recommendation-box b {{
        color: #082F49;
        font-weight: 950;
    }}

    div[data-testid="stDataFrame"] {{
        background: #FFFFFF;
        border-radius: 20px;
        padding: 12px;
        box-shadow: 0 22px 55px rgba(0,0,0,0.28);
        border: 1px solid rgba(56,189,248,0.25);
    }}

    .footer-text {{
        color: #CBD5E1;
        font-size: 15px;
        line-height: 1.9;
        padding-bottom: 22px;
    }}

    hr {{
        border-color: rgba(56,189,248,0.22);
    }}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# Chart Styling Helper
# -------------------------------------------------------
def style_chart(fig, title, height=460):
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(color=INK, size=23),
            x=0.02,
            xanchor="left"
        ),
        font=dict(color="#111827", size=14),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        height=height,
        margin=dict(l=55, r=35, t=70, b=55),
        legend=dict(
            font=dict(color="#111827"),
            bgcolor="rgba(255,255,255,0)"
        )
    )

    fig.update_xaxes(
        title_font=dict(color="#334155", size=14),
        tickfont=dict(color="#334155", size=12),
        gridcolor="#E5E7EB",
        linecolor="#CBD5E1",
        zerolinecolor="#CBD5E1"
    )

    fig.update_yaxes(
        title_font=dict(color="#334155", size=14),
        tickfont=dict(color="#334155", size=12),
        gridcolor="#E5E7EB",
        linecolor="#CBD5E1",
        zerolinecolor="#CBD5E1"
    )

    return fig


def chart_container(fig):
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------------
# Load Data
# -------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/marketing_funnel_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    df["visitor_to_lead_rate"] = df["leads"] / df["visitors"]
    df["lead_to_qualified_rate"] = df["qualified_leads"] / df["leads"]
    df["qualified_to_customer_rate"] = df["customers"] / df["qualified_leads"]
    df["overall_conversion_rate"] = df["customers"] / df["visitors"]

    df["cost_per_lead"] = df["marketing_spend"] / df["leads"]
    df["customer_acquisition_cost"] = df["marketing_spend"] / df["customers"]
    df["roi"] = (df["revenue"] - df["marketing_spend"]) / df["marketing_spend"]

    df = df.replace([float("inf"), -float("inf")], 0)
    df = df.fillna(0)

    return df


df = load_data()


# -------------------------------------------------------
# Hero Header
# -------------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="eyebrow"> · Data Science & Analytics ·</div>
    <div class="title">Marketing Funnel & Conversion Performance Analysis</div>
    <div class="subtitle">
        Navy blue executive dashboard for tracking funnel leakage, channel efficiency,
        campaign ROI, acquisition cost, and lead-to-customer conversion performance.
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# Sidebar Filters
# -------------------------------------------------------
st.sidebar.header("Dashboard Filters")

min_date = df["date"].min()
max_date = df["date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

selected_channels = st.sidebar.multiselect(
    "Select Channels",
    options=sorted(df["channel"].unique()),
    default=sorted(df["channel"].unique())
)

selected_campaigns = st.sidebar.multiselect(
    "Select Campaigns",
    options=sorted(df["campaign"].unique()),
    default=sorted(df["campaign"].unique())
)

selected_regions = st.sidebar.multiselect(
    "Select Regions",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

filtered_df = df.copy()

if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
    filtered_df = filtered_df[
        (filtered_df["date"] >= start_date) &
        (filtered_df["date"] <= end_date)
    ]

filtered_df = filtered_df[
    (filtered_df["channel"].isin(selected_channels)) &
    (filtered_df["campaign"].isin(selected_campaigns)) &
    (filtered_df["region"].isin(selected_regions))
]


# -------------------------------------------------------
# KPI Calculations
# -------------------------------------------------------
total_visitors = int(filtered_df["visitors"].sum())
total_leads = int(filtered_df["leads"].sum())
total_qualified = int(filtered_df["qualified_leads"].sum())
total_customers = int(filtered_df["customers"].sum())
total_spend = filtered_df["marketing_spend"].sum()
total_revenue = filtered_df["revenue"].sum()

overall_conversion = total_customers / total_visitors if total_visitors else 0
lead_conversion = total_leads / total_visitors if total_visitors else 0
cac = total_spend / total_customers if total_customers else 0
roi = (total_revenue - total_spend) / total_spend if total_spend else 0


# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------
st.markdown('<div class="section-header">Executive KPI Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">High-level performance snapshot across traffic, leads, customers, spend, revenue, and ROI.</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Visitors</div>
        <div class="metric-value">{total_visitors:,}</div>
        <div class="metric-note">Top-of-funnel audience volume</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Leads</div>
        <div class="metric-value">{total_leads:,}</div>
        <div class="metric-note">Visitor to lead rate: {lead_conversion:.2%}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Customers</div>
        <div class="metric-value">{total_customers:,}</div>
        <div class="metric-note">Lead-to-customer output</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Overall Conversion</div>
        <div class="metric-value">{overall_conversion:.2%}</div>
        <div class="metric-note">Visitors converted to customers</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Marketing Spend</div>
        <div class="metric-value">${total_spend:,.0f}</div>
        <div class="metric-note">Total acquisition investment</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Revenue</div>
        <div class="metric-value">${total_revenue:,.0f}</div>
        <div class="metric-note">Revenue from acquired customers</div>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">CAC</div>
        <div class="metric-value">${cac:,.2f}</div>
        <div class="metric-note">Customer acquisition cost</div>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">ROI</div>
        <div class="metric-value">{roi:.2f}x</div>
        <div class="metric-note">Return on marketing spend</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------------------------------
# Overall Funnel
# -------------------------------------------------------
st.markdown('<div class="section-header">Overall Marketing Funnel</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Stage-wise movement from visitors to paying customers.</div>', unsafe_allow_html=True)

funnel_values = [total_visitors, total_leads, total_qualified, total_customers]
funnel_stages = ["Visitors", "Leads", "Qualified Leads", "Customers"]

fig_funnel = go.Figure(go.Funnel(
    y=funnel_stages,
    x=funnel_values,
    textinfo="value+percent initial+percent previous",
    marker=dict(
        color=[ICE_BLUE, SOFT_BLUE, SKY_BLUE, OCEAN_BLUE],
        line=dict(width=1.3, color="#0F172A")
    )
))

fig_funnel.update_layout(
    title=dict(
        text="Overall Marketing Funnel",
        font=dict(color=INK, size=23),
        x=0.02,
        xanchor="left"
    ),
    font=dict(color="#111827", size=15),
    height=500,
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    margin=dict(l=55, r=45, t=70, b=50)
)

fig_funnel.update_traces(textfont=dict(color="#111827", size=15))
chart_container(fig_funnel)


# -------------------------------------------------------
# Drop-off Analysis
# -------------------------------------------------------
st.markdown('<div class="section-header">Funnel Drop-off Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Identifies the stage where the business loses the largest percentage of potential customers.</div>', unsafe_allow_html=True)

dropoff_data = pd.DataFrame({
    "Stage": ["Visitors to Leads", "Leads to Qualified Leads", "Qualified Leads to Customers"],
    "Start Count": [total_visitors, total_leads, total_qualified],
    "End Count": [total_leads, total_qualified, total_customers]
})

dropoff_data["Drop-off Count"] = dropoff_data["Start Count"] - dropoff_data["End Count"]
dropoff_data["Drop-off Rate"] = dropoff_data["Drop-off Count"] / dropoff_data["Start Count"]

fig_dropoff = px.bar(
    dropoff_data,
    x="Stage",
    y="Drop-off Rate",
    text=dropoff_data["Drop-off Rate"].apply(lambda x: f"{x:.2%}"),
    title="Drop-off Rate by Funnel Stage",
    color="Drop-off Rate",
    color_continuous_scale=["#DBEAFE", "#38BDF8", "#1E3A8A"]
)

fig_dropoff.update_traces(
    textposition="outside",
    textfont=dict(color="#111827", size=14),
    marker_line_color="#0F172A",
    marker_line_width=1
)

fig_dropoff = style_chart(fig_dropoff, "Drop-off Rate by Funnel Stage", height=470)
fig_dropoff.update_yaxes(title_text="Drop-off Rate", tickformat=".0%")
fig_dropoff.update_xaxes(title_text="Funnel Stage")
fig_dropoff.update_layout(coloraxis_showscale=False)
chart_container(fig_dropoff)


# -------------------------------------------------------
# Channel Summary
# -------------------------------------------------------
channel_summary = filtered_df.groupby("channel").agg({
    "visitors": "sum",
    "leads": "sum",
    "qualified_leads": "sum",
    "customers": "sum",
    "marketing_spend": "sum",
    "revenue": "sum"
}).reset_index()

channel_summary["conversion_rate"] = channel_summary["customers"] / channel_summary["visitors"]
channel_summary["cost_per_lead"] = channel_summary["marketing_spend"] / channel_summary["leads"]
channel_summary["customer_acquisition_cost"] = channel_summary["marketing_spend"] / channel_summary["customers"]
channel_summary["roi"] = (channel_summary["revenue"] - channel_summary["marketing_spend"]) / channel_summary["marketing_spend"]
channel_summary = channel_summary.replace([float("inf"), -float("inf")], 0).fillna(0)


# -------------------------------------------------------
# Channel Performance
# -------------------------------------------------------
st.markdown('<div class="section-header">Channel Performance</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Compares acquisition channels by conversion efficiency and ROI contribution.</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    sorted_conv = channel_summary.sort_values("conversion_rate", ascending=False)

    fig_channel_conv = px.bar(
        sorted_conv,
        x="channel",
        y="conversion_rate",
        text=sorted_conv["conversion_rate"].apply(lambda x: f"{x:.2%}"),
        title="Conversion Rate by Channel",
        color="conversion_rate",
        color_continuous_scale=["#E0F2FE", "#38BDF8", "#1D4ED8"]
    )

    fig_channel_conv.update_traces(
        textposition="outside",
        textfont=dict(color="#111827", size=13),
        marker_line_color="#0F172A",
        marker_line_width=1
    )

    fig_channel_conv = style_chart(fig_channel_conv, "Conversion Rate by Channel", height=460)
    fig_channel_conv.update_xaxes(title_text="Channel")
    fig_channel_conv.update_yaxes(title_text="Conversion Rate", tickformat=".0%")
    fig_channel_conv.update_layout(coloraxis_showscale=False)
    chart_container(fig_channel_conv)

with c2:
    sorted_roi = channel_summary.sort_values("roi", ascending=False)

    fig_roi = px.bar(
        sorted_roi,
        x="channel",
        y="roi",
        text=sorted_roi["roi"].apply(lambda x: f"{x:.2f}x"),
        title="ROI by Channel",
        color="roi",
        color_continuous_scale=["#DBEAFE", "#2563EB", "#0B1F3A"]
    )

    fig_roi.update_traces(
        textposition="outside",
        textfont=dict(color="#111827", size=13),
        marker_line_color="#0F172A",
        marker_line_width=1
    )

    fig_roi = style_chart(fig_roi, "ROI by Channel", height=460)
    fig_roi.update_xaxes(title_text="Channel")
    fig_roi.update_yaxes(title_text="ROI")
    fig_roi.update_layout(coloraxis_showscale=False)
    chart_container(fig_roi)


# -------------------------------------------------------
# Spend vs Revenue
# -------------------------------------------------------
st.markdown('<div class="section-header">Marketing Spend vs Revenue</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Evaluates how efficiently each channel converts marketing investment into revenue.</div>', unsafe_allow_html=True)

fig_spend_revenue = px.scatter(
    channel_summary,
    x="marketing_spend",
    y="revenue",
    size="customers",
    color="channel",
    hover_name="channel",
    title="Channel Efficiency: Spend vs Revenue",
    labels={
        "marketing_spend": "Marketing Spend",
        "revenue": "Revenue",
        "channel": "Channel",
        "customers": "Customers"
    },
    color_discrete_sequence=[
        "#38BDF8",
        "#2563EB",
        "#1D4ED8",
        "#0EA5E9",
        "#60A5FA",
        "#1E3A8A"
    ]
)

fig_spend_revenue.update_traces(
    marker=dict(line=dict(width=1.2, color="#0F172A"))
)

fig_spend_revenue = style_chart(fig_spend_revenue, "Channel Efficiency: Spend vs Revenue", height=520)
fig_spend_revenue.update_xaxes(title_text="Marketing Spend")
fig_spend_revenue.update_yaxes(title_text="Revenue")
chart_container(fig_spend_revenue)


# -------------------------------------------------------
# Campaign Performance
# -------------------------------------------------------
st.markdown('<div class="section-header">Campaign Performance</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Highlights the campaigns generating the strongest customer outcomes.</div>', unsafe_allow_html=True)

campaign_summary = filtered_df.groupby("campaign").agg({
    "visitors": "sum",
    "leads": "sum",
    "qualified_leads": "sum",
    "customers": "sum",
    "marketing_spend": "sum",
    "revenue": "sum"
}).reset_index()

campaign_summary["conversion_rate"] = campaign_summary["customers"] / campaign_summary["visitors"]
campaign_summary["roi"] = (campaign_summary["revenue"] - campaign_summary["marketing_spend"]) / campaign_summary["marketing_spend"]
campaign_summary = campaign_summary.replace([float("inf"), -float("inf")], 0).fillna(0)

fig_campaign = px.bar(
    campaign_summary.sort_values("customers", ascending=False),
    x="campaign",
    y="customers",
    color="roi",
    text="customers",
    title="Customers Generated by Campaign",
    color_continuous_scale=["#E0F2FE", "#38BDF8", "#1E3A8A"],
    labels={
        "campaign": "Campaign",
        "customers": "Customers",
        "roi": "ROI"
    }
)

fig_campaign.update_traces(
    textposition="outside",
    textfont=dict(color="#111827", size=14),
    marker_line_color="#0F172A",
    marker_line_width=1
)

fig_campaign = style_chart(fig_campaign, "Customers Generated by Campaign", height=470)
fig_campaign.update_xaxes(title_text="Campaign")
fig_campaign.update_yaxes(title_text="Customers")
fig_campaign.update_layout(
    coloraxis_colorbar=dict(
        title=dict(text="ROI", font=dict(color="#111827")),
        tickfont=dict(color="#111827")
    )
)
chart_container(fig_campaign)


# -------------------------------------------------------
# Monthly Trend
# -------------------------------------------------------
st.markdown('<div class="section-header">Monthly Conversion Trend</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Tracks conversion consistency and performance movement over time.</div>', unsafe_allow_html=True)

monthly = filtered_df.copy()
monthly["month"] = monthly["date"].dt.to_period("M").astype(str)

monthly_summary = monthly.groupby("month").agg({
    "visitors": "sum",
    "leads": "sum",
    "customers": "sum",
    "revenue": "sum"
}).reset_index()

monthly_summary["conversion_rate"] = monthly_summary["customers"] / monthly_summary["visitors"]

fig_monthly = px.line(
    monthly_summary,
    x="month",
    y="conversion_rate",
    markers=True,
    title="Monthly Visitor-to-Customer Conversion Rate"
)

fig_monthly.update_traces(
    line=dict(width=4, color=OCEAN_BLUE),
    marker=dict(size=10, color=SKY_BLUE, line=dict(width=1.4, color="#0F172A"))
)

fig_monthly = style_chart(fig_monthly, "Monthly Visitor-to-Customer Conversion Rate", height=460)
fig_monthly.update_xaxes(title_text="Month")
fig_monthly.update_yaxes(title_text="Conversion Rate", tickformat=".0%")
chart_container(fig_monthly)


# -------------------------------------------------------
# Detailed Channel Table
# -------------------------------------------------------
st.markdown('<div class="section-header">Detailed Channel Summary</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Tabular breakdown of channel-level funnel performance and financial efficiency.</div>', unsafe_allow_html=True)

display_table = channel_summary.copy()

display_table = display_table.rename(columns={
    "channel": "Channel",
    "visitors": "Visitors",
    "leads": "Leads",
    "qualified_leads": "Qualified Leads",
    "customers": "Customers",
    "marketing_spend": "Marketing Spend",
    "revenue": "Revenue",
    "conversion_rate": "Conversion Rate",
    "cost_per_lead": "Cost Per Lead",
    "customer_acquisition_cost": "CAC",
    "roi": "ROI"
})

display_table["Conversion Rate"] = display_table["Conversion Rate"].apply(lambda x: f"{x:.2%}")
display_table["Cost Per Lead"] = display_table["Cost Per Lead"].apply(lambda x: f"${x:,.2f}")
display_table["CAC"] = display_table["CAC"].apply(lambda x: f"${x:,.2f}")
display_table["ROI"] = display_table["ROI"].apply(lambda x: f"{x:.2f}x")
display_table["Marketing Spend"] = display_table["Marketing Spend"].apply(lambda x: f"${x:,.0f}")
display_table["Revenue"] = display_table["Revenue"].apply(lambda x: f"${x:,.0f}")

st.dataframe(display_table, use_container_width=True)


# -------------------------------------------------------
# Automated Insights
# -------------------------------------------------------
st.markdown('<div class="section-header">Key Insights</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Automatically generated business observations from the selected data view.</div>', unsafe_allow_html=True)

best_channel = channel_summary.sort_values("conversion_rate", ascending=False).iloc[0]
worst_channel = channel_summary.sort_values("conversion_rate", ascending=True).iloc[0]
best_roi_channel = channel_summary.sort_values("roi", ascending=False).iloc[0]
highest_cac_channel = channel_summary.sort_values("customer_acquisition_cost", ascending=False).iloc[0]
biggest_dropoff = dropoff_data.sort_values("Drop-off Rate", ascending=False).iloc[0]

st.markdown(f"""
<div class="insight-box">
    <b>Best converting channel:</b> {best_channel['channel']} has the highest visitor-to-customer conversion rate of {best_channel['conversion_rate']:.2%}, making it the strongest channel for converting traffic into paying customers.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="insight-box">
    <b>Weakest converting channel:</b> {worst_channel['channel']} has the lowest conversion rate of {worst_channel['conversion_rate']:.2%}, indicating a need to review targeting, messaging, landing page relevance, or lead quality.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="insight-box">
    <b>Best ROI channel:</b> {best_roi_channel['channel']} delivers the strongest return on investment at {best_roi_channel['roi']:.2f}x, making it a strong candidate for budget scaling.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="warning-box">
    <b>Major funnel leakage:</b> The biggest drop-off occurs at the <b>{biggest_dropoff['Stage']}</b> stage with a drop-off rate of {biggest_dropoff['Drop-off Rate']:.2%}. This stage should be treated as the first optimization priority.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="warning-box">
    <b>Highest acquisition cost:</b> {highest_cac_channel['channel']} has the highest customer acquisition cost of ${highest_cac_channel['customer_acquisition_cost']:.2f}, which may reduce profitability if not optimized.
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# Recommendations
# -------------------------------------------------------
st.markdown('<div class="section-header">Actionable Recommendations</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtext">Recommended actions to improve lead quality, funnel efficiency, and customer conversion.</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="recommendation-box">
    <b>1. Fix the largest funnel drop-off:</b> Since the highest leakage is happening at the <b>{biggest_dropoff['Stage']}</b> stage, improve landing page clarity, lead capture forms, call-to-action placement, page loading speed, and follow-up speed.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="recommendation-box">
    <b>2. Scale high-ROI channels:</b> Gradually increase marketing budget for <b>{best_roi_channel['channel']}</b> because it currently delivers the strongest ROI. Scale in controlled increments while monitoring CAC and conversion quality.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="recommendation-box">
    <b>3. Improve low-converting channels:</b> Review audience targeting, ad creatives, value proposition, and landing page alignment for <b>{worst_channel['channel']}</b> because it has the weakest conversion rate.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="recommendation-box">
    <b>4. Reduce acquisition cost:</b> For <b>{highest_cac_channel['channel']}</b>, improve segmentation, retarget warm leads, exclude low-intent audiences, and test lower-cost campaign objectives.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="recommendation-box">
    <b>5. Strengthen lead nurturing:</b> Use automated email follow-ups, retargeting ads, demo reminders, personalized offers, and educational content to move more leads from awareness to purchase.
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.write("")
st.markdown("---")
st.markdown("""
<div class="footer-text">
<b>Project:</b> FUTURE_DS_03 — Marketing Funnel & Conversion Performance Analysis<br>
<b>Tools Used:</b> Python, Streamlit, Pandas, Plotly<br>
<b>Internship Track:</b> Data Science & Analytics<br>
<b>Prepared By:</b> Shifa Dewani
</div>
""", unsafe_allow_html=True)