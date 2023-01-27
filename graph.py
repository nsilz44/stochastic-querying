import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

d = {'instance': ['first', 'first', 'first', 'first', 'second', 'second', 'second', 'second', 'third','third','third','third','forth','forth','forth','forth'], 'Expected type': ['Comp Algorithm','E[size algorithm/size optimum]','Comp heuristic','E[size heuristic/size optimum]','Comp Algorithm','E[size algorithm/size optimum]','Comp heuristic','E[size heuristic/size optimum]','Comp Algorithm','E[size algorithm/size optimum]','Comp heuristic','E[size heuristic/size optimum]','Comp Algorithm','E[size algorithm/size optimum]','Comp heuristic','E[size heuristic/size optimum]'], 'ratio':[1.10133,1.07717,1.05801,1.04418,1.07583,1.06105,1.07421,1.05977,1.42855,1.52697,1.09602,1.10444,1.93146,1.96086,1.25110,1.24316]} 
df = pd.DataFrame(data=d)
print(df)
sns.catplot(x='instance', y='ratio', hue='Expected type', data=df, kind='bar')
plt.show()