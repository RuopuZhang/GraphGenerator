import sys
import pandas as pd
import plotly.graph_objects as go
# come comments

def Veh_Speed_Dist(var1,var2,var3,var4):
	df_fig1 = pd.read_csv(var1)
	df_table1 = pd.read_csv(var2)

	#fig 1, Safe Systems Speed Distribution
	fig1 = go.Figure(data = [
		go.Bar(x = df_fig1['Vehicle_Movement'], y = df_fig1['Low_Speed'],width=0.1, marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1, name="<35 km/h"),
		go.Bar(x = df_fig1['Vehicle_Movement'], y = df_fig1['Medium_Speed'], width=0.1, marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1,name="35-50 km/h"),
		go.Bar(x = df_fig1['Vehicle_Movement'], y = df_fig1['High_Speed'], width=0.1, marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1,name=">50 km/h"),
		])
	fig1.update_layout(
		autosize=False,
		plot_bgcolor='white',
		legend = go.layout.Legend(bordercolor="Black", borderwidth=1, orientation='h'),
		barmode='stack',
		width=600,
		height=300,
		xaxis = dict(
			showline=True,
			linewidth=1, 
			linecolor='black',
			mirror=True,
			),
		yaxis = dict(
			title_text="Frequency(%)",
			showline=True,
			linewidth=1, 
			linecolor='black',
			mirror=True,
			ticks="inside",
			range=[0, 100], 
			dtick=20,
			),
		margin=go.layout.Margin(l=0, r=0, b=0, t=0)
		)


	#table 1
	table1 = go.Figure(data=[go.Table(
		columnorder = [1,2,3,4,5,6,7],
		columnwidth = [80,40,40,40,40,40,40],
		header=dict(
			values=list(df_table1.columns),
			fill_color='grey',
			line_color='darkslategray',
			align=['left','center']
			),
		cells=dict(
			values=[df_table1['Vehicle Movement'], df_table1['Vehicles < 35 km/h'],df_table1['Vehicles 35-50 km/h'],
			df_table1['Vehicles >50 km/h'], df_table1['Average Speed (km/h)'],df_table1['85th percentile (km/h)'],df_table1['Detail Page']],
			fill_color='white',
			line_color='darkslategray',
			align=['left','center'],
			font=dict(size=12)
			)
		)
	])
	table1.update_layout(
		autosize=False,
		width=800,
		height=400,
		margin=go.layout.Margin(l=0, r=1, b=0, t=0)
		)

	table1.write_image('{}.png'.format(var3))
	fig1.write_image('{}.png'.format(var4))






