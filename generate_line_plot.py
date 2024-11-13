import re
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
from scipy.interpolate import CubicSpline


# Read the RAG-LIST.md file
with open('RAG-LIST.md', 'r', encoding='utf-8') as file:
    content = file.read()

date_pattern = r"Published Date: (\d{1,2})\s([A-Za-z]+)\s(\d{4})"
dates = re.findall(date_pattern, content)

date_objects = [datetime.strptime(f"{day} {month} {year}", "%d %b %Y") for day, month, year in dates]
df = pd.DataFrame(date_objects, columns=['Publication Date'])

df['Month'] = df['Publication Date'].dt.strftime('%b')  
df['Year'] = df['Publication Date'].dt.year  # Year

monthly_counts = df.groupby(['Month', 'Year']).size().reset_index(name='Count')

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_counts['Month'] = pd.Categorical(monthly_counts['Month'], categories=month_order, ordered=True)

# Sort by Month and Year
monthly_counts = monthly_counts.sort_values(by=['Year', 'Month'])

data = {
    'Month': monthly_counts['Month'].tolist(),
    'Year': monthly_counts['Year'].tolist(),
    'Count': monthly_counts['Count'].tolist(),
}

df = pd.DataFrame(data)

# Mapping month names to numbers
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

df['Month'] = df['Month'].map(month_map)

df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))

df_with_zero = pd.DataFrame({'Month': [2], 'Year': [2024], 'Count': [0]})

df_with_zero['Date'] = pd.to_datetime(df_with_zero[['Year', 'Month']].assign(DAY=1))

df = pd.concat([df_with_zero, df], ignore_index=True)

df = df.sort_values(by='Date')

df['Cumulative Count'] = df['Count'].cumsum()

x = pd.to_numeric(df['Date']) 
y_cumulative = df['Cumulative Count']  
y_monthly = df['Count']  

cs_cumulative = CubicSpline(x, y_cumulative, bc_type='natural')
cs_monthly = CubicSpline(x, y_monthly, bc_type='natural')

# Generate new x-values (dates) for smooth curve plotting
x_smooth = pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='D')
x_smooth_num = pd.to_numeric(x_smooth)
y_smooth_cumulative = cs_cumulative(x_smooth_num)
y_smooth_monthly = cs_monthly(x_smooth_num)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_smooth,
    y=y_smooth_cumulative,
    mode='lines',
    line=dict(color='royalblue', width=4, dash='dot'), 
    name="Cumulative Publication Count"
))

fig.add_trace(go.Scatter(
    x=x_smooth,
    y=y_smooth_monthly,
    mode='lines',
    line=dict(color='green', width=4, dash='solid'), 
    name="Monthly Publication Count"
))

# Add shaded area under the cumulative curve
fig.add_trace(go.Scatter(
    x=x_smooth,
    y=y_smooth_cumulative,
    fill='tozeroy',
    fillcolor='rgba(72, 209, 204, 0.4)', 
    line=dict(color='rgba(255,255,255,0)'),
    showlegend=False
))

# Add annotations for each data point showing the count for that month
for i, row in df.iterrows():
    fig.add_annotation(
        x=row['Date'],
        y=row['Count'],
        text=str(row['Count']),
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-30,
        font=dict(size=10, color="black")
    )

# Customize layout
fig.update_layout(
    title="Number of RAG Benchmarks Published (Monthly & Cumulative)",
    xaxis_title="Month",
    yaxis_title="Publications",
    xaxis=dict(
        tickmode='array',
        tickvals=df['Date'],
        ticktext=df['Date'].dt.strftime('%b %Y'),
        tickangle=45
    ),
    template="plotly_white",
    showlegend=True,
    autosize=True
)

fig.write_image("assets/publication_daywise_line_plot.png")
