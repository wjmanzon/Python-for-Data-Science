# loading in libraries
import pandas as pd
import altair as alt

# personal note: the above import statements cannot be run if the modules haven't been installed. You can do that by running this to the command line: python -m pip install pandas altair

# loading in csv file
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

# creating the chart
chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)

# saving the chart
chart.save("screenshots/altair_viz_1.png")