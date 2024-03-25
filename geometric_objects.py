import pandas as pd
import altair as alt

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

chartp = (alt.Chart(mpg)
          .encode(
              x = "displ",
              y = "hwy"
          )
          .mark_circle())

chartp

chartf = (alt.Chart(mpg)
          .encode(
              x = "displ",
              y = "hwy"
          )
          .transform_loess("displ","hwy")
          .mark_line()
          )

chartf

chartp.save("screenshots/altair_basics_points.png")
chartf.save("screenshots/altair_smooth_line.png")

# Both plots contain the same x variable, the same y variable, and both describe the same data. But the plots are not identical. Each plot uses a different visual object to represent the data. In Altair syntax, we say that they use different marks. A mark is the geometrical object that a plot uses to represent data. The first plot uses the point mark, and the second plot uses the line mark, a smooth line fitted to the data is calculated using a transformation.

chartl = (alt.Chart(mpg)
  .transform_loess("displ", "hwy", groupby = ["drv"])
  .encode(
    x = "displ",
    y = "hwy",
    strokeDash = "drv"
    )
  .mark_line())

chartl
  
chartl.save("screenshots/altair_dashed_lines.png")


###################
###################

chartleft = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    )
  .transform_loess("displ", "hwy")
  .mark_line())

chartleft

chartmiddle = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    detail = "drv"
    )
  .transform_loess("displ", "hwy", groupby = ["drv"])
  .mark_line())

chartmiddle

chartright = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    color=alt.Color("drv", legend=None)
    )
  .transform_loess("displ", "hwy", groupby = ["drv"])
  .mark_line())
  
chartright

chartleft.save("screenshots/altair_chartleft.png")
chartmiddle.save("screenshots/altair_chartmiddle.png")
chartright.save("screenshots/altair_chartright.png")

#########################
#########################
# To display multiple marks in the same plot, you can used layered charts as shown in the example below that uses the chartleft object from the above code chunk:

chartp = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy"
  )
  .mark_circle()
)

chart = chartp + chartleft  

chart

chart.save("screenshots/altair_chartcombine.png")

# This, however, introduces some duplication in our code. Imagine if you wanted to change the y-axis to display cty instead of hwy. You’d need to change the variable in two places, and you might forget to update one. You can avoid this type of repetition by passing a set of encodings to a base alt.Chart(). Altair will treat these encodings as global encodings that apply to each mark layer in the layered chart. In other words, this code will produce the same plot as the previous code:

base = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy"
    ))

chart = base.mark_circle() + base.transform_loess("displ", "hwy").mark_line()

chart

chart.save("screenshots/altair_combine_clean.png")

# If you place encodings in an encode function, Altair will treat them as local mappings for the layer. It will use these mappings to extend or overwrite the base encodings for that layer only. This makes it possible to display different aesthetics in different layers.

base =(alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy"
  ))

chart = base.encode(color = "drv").mark_circle() + base.transform_loess("displ", "hwy").mark_line()

chart

chart.save("screenshots/altair_combine_clean_color.png")

##################################
##################################
# column name of class does not work nicely with Altair filter.

base = (alt.Chart(mpg.rename(columns = {"class": "class1"}))
  .encode(
    x = "displ",
    y = "hwy"
    ))

chart_smooth_sub = (base
  .transform_filter(alt.datum.class1 == "subcompact")
  .transform_loess("displ", "hwy")
  .mark_line()
)  

chart = base.encode(color = "class1").mark_circle() + chart_smooth_sub

chart

chart.save("screenshots/altair_combine_clean_color_filter.png")