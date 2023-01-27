import pandas as pd
data = pd.read_csv("2018_central_park_squirrel_census.csv")

black_count = len(data[data["Primary Fur Color"] == "Black"])
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

fur_dict = {'fur colour': ['black', 'grey', 'cinnamon'],
             'count': [black_count, grey_count, cinnamon_count]}

fur_df = pd.DataFrame(fur_dict)
fur_df.to_csv("fur_count.csv")