import pandas as pd
import altair as alt
alt.data_transformers.enable("vegafusion")

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/diamonds/diamonds.csv"
diamonds = pd.read_csv(url)

diamonds['cut'] = pd.Categorical(diamonds.cut, ordered = True,  categories =  ["Fair", "Good", "Very Good", "Premium", "Ideal" ])

diamonds

diamonds['color'] = pd.Categorical(diamonds.color, ordered = True, categories =  ["D", "E", "F", "G", "H", "I", "J"])

diamonds

diamonds['clarity'] = pd.Categorical(diamonds.clarity, ordered = True, categories =  ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

diamonds

chart = (alt.Chart(diamonds)
         .encode(
             x = "cut",
             y = alt.Y("count():Q")
         )
         .mark_bar()
         .properties(width = 400))

chart


