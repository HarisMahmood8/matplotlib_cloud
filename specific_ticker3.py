from google.cloud import datastore
from google.oauth2 import service_account
import plotly.graph_objs as go
from plotly.offline import plot

# Path to your JSON key file
key_path = "sentiment-analysis-379200-85d47d170d69.json"

# Initialize the Datastore client with explicit credentials
credentials = service_account.Credentials.from_service_account_file(key_path)
client = datastore.Client(credentials=credentials)

# Create a query to fetch entities from the Datastore
query = client.query(kind='Sentiment_Details')
query.order = ['CallDate']

# Fetch the data
entities = list(query.fetch())

# Prepare the data for plotting
keyword_period_scores = {}

# Filter entities after fetching
filtered_entities = [e for e in entities if e['YahooTicker'] == 'TEP FP']

for entity in filtered_entities:
    period = entity['Period']
    keyword = entity['Keyword']
    score = entity['Score']

    if keyword not in keyword_period_scores:
        keyword_period_scores[keyword] = {}

    if period in keyword_period_scores[keyword]:
        keyword_period_scores[keyword][period].append(score)
    else:
        keyword_period_scores[keyword][period] = [score]

# Prepare the Plotly graph
fig = go.Figure()

for keyword, period_scores in keyword_period_scores.items():
    unique_periods = sorted(period_scores.keys())
    average_scores = [sum(scores) / len(scores)
                      for scores in period_scores.values()]

    # Create a trace for each keyword
    fig.add_trace(go.Scatter(
        x=unique_periods,
        y=average_scores,
        mode='lines+markers',
        name=keyword
    ))

fig.update_layout(
    title='Average Sentiment Scores Over Time by Keyword for YahooTicker TEP FP',
    xaxis_title='Period',
    yaxis_title='Average Sentiment Score',
    legend_title='Keywords',
    xaxis=dict(tickangle=45)
)

# Plot the figure to an interactive HTML file
plot(fig, filename='average_sentiment_scores_by_keyword_tep_fp.html')

print("The interactive graph has been saved as 'average_sentiment_scores_by_keyword_tep_fp.html'")
