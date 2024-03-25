import pandas as pd
import altair as alt

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

chart_f = (alt.Chart(mpg)
           .encode(
               x = "displ",
               y = "hwy",
           )
           .mark_circle()
           .facet(
               facet = "class", columns = 4
           ))

chart_f

chart_f.save("screenshots/altair_facet_1.png")

# To facet your plot on the combination of two variables, the first argument of .facet() is column and the second is row

chart_f2 = (alt.Chart(mpg)
            .encode(
                x = "displ",
                y = "hwy",
            )
            .mark_circle()
            .facet(
                column = "drv",
                row = "cyl"
            ))

chart_f2

#WARN row encoding should be discrete (ordinal / nominal / binned)

chart_f2.save("screenshots/altair_facet_2.png")