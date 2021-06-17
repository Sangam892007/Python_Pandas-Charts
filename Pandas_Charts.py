import pandas as pd
import plotly.express as pe

Import1 = pd.read_csv("C:/Desktop/Coding/PYTHON/Data-visualization-master/csv files/line_chart.csv")
graph = pe.line(Import1,x = "Per capita income", y = "Year", title="Income of people in different Countries" , color="Country")

graph.show()

graph1 = pe.bar(Import1, x = "Year", y = "Per capita income", title="Income of people in different Countries" , color="Country")
graph1.show()

graph2 = pe.scatter(Import1, x = "Year", y = "Per capita income", title="Income of people in different Countries",color="Country", size="Per capita income", size_max=10)
graph2.show()