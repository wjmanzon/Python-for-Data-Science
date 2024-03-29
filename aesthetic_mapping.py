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


# the chart below has colored points that distinguishes car types. That's called "mapping class to color encoding"
chart = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    color = "class"
  )
  .mark_circle())

chart

chart.save("screenshots/altair_viz_2.png")

# now we will try to map the class to size encoding. This is a bad example. Channel size should not be used with an unsorted discreet field.
chart = (alt.Chart(mpg)
         .encode(
             x = "displ",
             y = "hwy",
             size = "class"
         )
         .mark_circle())

chart

chart.save("screenshots/altair_viz_3.png")

# mapping class to the opacity encoding
chart1 = (alt.Chart(mpg)
          .encode(
              x = "displ",
              y = "hwy",
              opacity = "class"
          )
          .mark_circle())

chart1

chart1.save("screenshots/altair_opacity.png")

# mapping class to the shape encoding
# note that altair can only use 8 shapes at a time
chart2 = (alt.Chart(mpg)
          .encode(
              x = "displ",
              y = "hwy",
              shape = "class"
          )
          .mark_point())

chart2

chart2.save("screenshots/altair_shape.png")

# make all points in plot blue

chart = (alt.Chart(mpg)
         .encode(
             x = "displ",
             y = "hwy",
             color = alt.value("blue")
         )
         .mark_circle())

chart

chart.save("screenshots/altair_viz_4.png")

