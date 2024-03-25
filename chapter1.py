# load libraries
import pandas as pd
import altair as alt

# personal note: the above import statements cannot be run if the modules haven't been installed. You can do that by running this to the command line: python -m pip install pandas altair

# load csv file
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

# create the chart
chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)

# call the chart so it shows on the interactive window
chart

# save the chart in screenshots folder. That folder should have been precreated.
chart.save("screenshots/altair_viz_1.png")