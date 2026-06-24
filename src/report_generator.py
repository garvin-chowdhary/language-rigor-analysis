import pandas as pd

def save_results(results):

    df = pd.DataFrame(results)

    df.to_csv(

        "output/results.csv",

        index=False

    )