import pandas as pd

df_uso = pd.read_csv("USO.csv")
df_slv = pd.read_csv("SLV.csv")
df_spx = pd.read_csv("S&P 500.csv")
df_eur = pd.read_csv("EUR_USD.csv")

df_uso = df_uso.rename(columns={"Price": "USO"})
df_slv = df_slv.rename(columns={"Price": "SLV"})
df_spx = df_spx.rename(columns={"Price": "S&P500"})
df_eur = df_eur.rename(columns={"Price": "EUR/USD"})

df_final = df_uso[["Date", "USO"]] \
    .merge(df_slv[["Date", "SLV"]], on="Date") \
    .merge(df_spx[["Date", "S&P500"]], on="Date") \
    .merge(df_eur[["Date", "EUR/USD"]], on="Date")

df_final.to_csv("final_data.csv", index=False)

