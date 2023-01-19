# importing the pandas library
import pandas as pd
  
#37K,23.650,184.346,149.133
#36K,23.349,184.341,149.131
#35K,23.652,181.674,149.133
#34K,23.354,181.668,149.133

#RN: remove header in the same
#    format 2 floating points
#    distribute
#       SionMed account on github
#       listen to distribution lecture
height = input('Whats the height? ')
#print(inp)

# reading the csv file
df = pd.read_csv("from_this.csv", header=None)
  
#print(df)


df[4] = float(height) - df[3]

# writing into the file
df.to_csv("sionOutput.csv", index=False, header=None)
  
