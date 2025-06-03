from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()  

df = get_df("cbb")  

sql = "SELECT * FROM cbb WHERE ORB > 35.0"
filtered_df = query(sql, "cbb")

text("# My Basketball Stats App")
table(filtered_df, title="Teams with over 35 Offensive Rebounds Per Game")

fig = px.scatter(df, x="ORB", y="DRB", color="TEAM", title="Teams with ORB > 35") 
plotly(fig)
