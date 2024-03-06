1. You will need a json key to run this file, change the json file in the program to the one you have.

2. run the file

          python3 specific_ticker3.py



## How It Works
1. **Data Retrieval**: Connects to Google Cloud Datastore using a service account JSON key to fetch sentiment data.
2. **Data Processing**: Filters and aggregates sentiment scores by keywords and periods from the fetched data.
3. **Visualization**: Uses Plotly to create an interactive line graph displaying average sentiment scores for each keyword across different periods.



## Usage
To generate the visualization:
1. Ensure that the JSON key file path is correctly set in `key_path`.
2. Run the script. It will create an interactive HTML file showing the sentiment scores plotted over time.
