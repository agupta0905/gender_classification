import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wget

def save_img(df, index):
  print(index)
  img_arr = np.zeros((100,100))
  for r in range(0,100):
    for c in range(0,100):
      pixel = df["px" + str(r*100 + c)].iloc[index]
      img_arr[r][c] = pixel

  if df["gender"].iloc[index] == 1:
    plt.imsave("input/images/man/img_" + str(index) + ".png",img_arr, cmap="gray")
  else:
    plt.imsave("input/images/woman/img_" + str(index) + ".png",img_arr, cmap="gray")

url = "http://datax.kennesaw.edu/imdb_wiki/wiki5.csv"
wget.download(url, 'input/wiki5.csv')

df = pd.read_csv('input/wiki5.csv')
for i in range(0, len(df.index)):
  save_img(df, i)
