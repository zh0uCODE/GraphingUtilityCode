#Graphing Project - Lucas Zhou - 7/19/2025
#I wrote code that produced a graph of the frequency difference over time. It is important to keep the frequency difference around a very small range over time so that GPS signals are locked in faster. 
import pandas as pd #import pd
import matplotlib.pyplot as plt #imp plt
df = pd.read_csv('A.csv'); #pandas dataframe for csv file
def drawPowerOnClockDriftChart(f0, csv_name):
  df = pd.read_csv(csv_name); #pandas dataframe for csv file
  df['Diff F'] = (df['Freq'].shift(1)-df['Freq']) / f0 * 10**10 #compute difference between curr and prev
  df = df.dropna() #remove any rows that have no values! 
  #plot:
  plt.plot(df['Time'], df['Diff F'], marker='o')
  plt.title("Diff F over Time")
  plt.xlabel("Time")
  plt.ylabel("Diff: Curr - Prev")
  plt.grid(True)
  plt.show()
drawPowerOnClockDriftChart(38.4 * 10**6, 'A.csv')




