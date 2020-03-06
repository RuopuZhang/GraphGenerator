import sys
import pandas as pd
import plotly.graph_objects as go


def Veh_Conflicts(v1,v2, v4,v5):

	how_many_tables_each_graph = len(v2)

	# for i in range(1, int(how_many_graphs)+1):

	#fig 1, Safe Systems PET by Vehicle Movement Type
	df_fig1 = pd.read_csv(v1[0])

	fig1 = go.Figure(data = [
		go.Bar(x = df_fig1['a'], y = df_fig1['e'], width=0.3, marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1, name="low risk "),
		go.Bar(x = df_fig1['a'], y = df_fig1['d'], width=0.3, marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1,name="medium risk "),
		go.Bar(x = df_fig1['a'], y = df_fig1['c'], width=0.3, marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1,name="high risk "),
		go.Bar(x = df_fig1['a'], y = df_fig1['b'], width=0.3, marker_color='red', marker_line_color='black', marker_line_width=1, opacity=1,name="critical risk "),

		])
	fig1.update_layout(
		autosize=False,
		plot_bgcolor='white',
		legend = go.layout.Legend(x=0.2,y=-0.25,bordercolor="Black", borderwidth=1, orientation='h'),
		barmode='stack',
		width=800,
		height=600,
		xaxis = dict(
			showline=True,
			linewidth=1, 
			linecolor='black',
			ticks="outside",
			mirror=True,
			),
		yaxis = dict(
			title_text="Frequency",
			showline=True,
			linewidth=1, 
			linecolor='black',
			mirror=True,
			ticks="inside",
			range=[0, 120], 
			dtick=10,
			),
		margin=go.layout.Margin(l=0, r=0, b=0, t=0)
		)

	fig1.write_image('{}.png'.format(v4))


	#table 1
	for j in range(0,how_many_tables_each_graph):

		df_table1 = pd.read_csv(v2[j], usecols=[0,1,2,3,4,5])

		table1 = go.Figure(data=[go.Table(
			columnorder = [1,2,3,4,5,6],
			columnwidth = [100,40,40,40,40,40],
			header=dict(
				values=list(df_table1.columns),
				fill_color='grey',
				line_color='darkslategray',
				align=['left','center']
				),
			cells=dict(
				values=[df_table1['Configuration'], df_table1['Critical Risk (rate)'],df_table1['High Risk (rate)'],
				df_table1['Medium Risk (rate)'], df_table1['Low Risk (rate)'],df_table1['Detail Page']],
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
			height=200,
			margin=go.layout.Margin(l=0, r=1, b=0, t=0)
			)
		
		table1.write_image("{}{}.png".format(v5, j))

def Cyc_Conflicts(v1,v2,v4,v5):

	how_many_tables_each_graph = len(v2)

	# for i in range(1, int(how_many_graphs)+1):

	#fig 1, Safe Systems PET by Vehicle Movement Type
	df_fig1 = pd.read_csv(v1[0])

	fig1 = go.Figure(data = [
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_low'], width=0.3, marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1, name="low risk "),
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_medium'], width=0.3, marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1,name="medium risk "),
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_high'], width=0.3, marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1,name="high risk "),
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_critical'], width=0.3, marker_color='red', marker_line_color='black', marker_line_width=1, opacity=1,name="critical risk "),

		])
	fig1.update_layout(
		autosize=False,
		plot_bgcolor='white',
		legend = go.layout.Legend(x=0.2,y=-0.25,bordercolor="Black", borderwidth=1, orientation='h'),
		barmode='stack',
		width=800,
		height=600,
		xaxis = dict(
			showline=True,
			linewidth=1, 
			linecolor='black',
			ticks="outside",
			mirror=True,
			),
		yaxis = dict(
			title_text="Frequency",
			showline=True,
			linewidth=1, 
			linecolor='black',
			mirror=True,
			ticks="inside",
			range=[0, 80], 
			dtick=5,
			),
		margin=go.layout.Margin(l=0, r=0, b=0, t=0)
		)

	fig1.write_image('{}.png'.format(v4))


	#table 1
	for j in range(0,how_many_tables_each_graph):

		df_table1 = pd.read_csv(v2[j], usecols=[0,1,2,3,4,5])

		table1 = go.Figure(data=[go.Table(
			columnorder = [1,2,3,4,5,6],
			columnwidth = [100,40,40,40,40,40],
			header=dict(
				values=list(df_table1.columns),
				fill_color='grey',
				line_color='darkslategray',
				align=['left','center']
				),
			cells=dict(
				values=[df_table1['Configuration'], df_table1['Critical_Freq'],df_table1['High_Freq'],
				df_table1['Medium_Freq'], df_table1['Low_Freq'],df_table1['Detail Page']],
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
			height=200,
			margin=go.layout.Margin(l=0, r=1, b=0, t=0)
			)
		
		table1.write_image("{}{}.png".format(v5, j))

def Ped_Conflicts(v1,v2,v4,v5):

	how_many_tables_each_graph = len(v2)

	# for i in range(1, int(how_many_graphs)+1):

	#fig 1, Safe Systems PET by Vehicle Movement Type
	df_fig1 = pd.read_csv(v1[0])

	fig1 = go.Figure(data = [
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_low'], width=0.3, marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1, name="low risk "),
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_medium'], width=0.3, marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1,name="medium risk "),
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_high'], width=0.3, marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1,name="high risk "),
		go.Bar(x = df_fig1['Direction'], y = df_fig1['Frequency_critical'], width=0.3, marker_color='red', marker_line_color='black', marker_line_width=1, opacity=1,name="critical risk "),

		])
	fig1.update_layout(
		autosize=False,
		plot_bgcolor='white',
		legend = go.layout.Legend(x=0.2,y=-0.25,bordercolor="Black", borderwidth=1, orientation='h'),
		barmode='stack',
		width=800,
		height=600,
		xaxis = dict(
			showline=True,
			linewidth=1, 
			linecolor='black',
			ticks="outside",
			mirror=True,
			),
		yaxis = dict(
			title_text="Frequency",
			showline=True,
			linewidth=1, 
			linecolor='black',
			mirror=True,
			ticks="inside",
			range=[0, 300], 
			dtick=20,
			),
		margin=go.layout.Margin(l=0, r=0, b=0, t=0)
		)

	fig1.write_image('{}.png'.format(v4))


	#table 1
	for j in range(0,how_many_tables_each_graph):

		df_table1 = pd.read_csv(v2[j], usecols=[0,1,2,3,4,5])

		table1 = go.Figure(data=[go.Table(
			columnorder = [1,2,3,4,5,6],
			columnwidth = [100,40,40,40,40,40],
			header=dict(
				values=list(df_table1.columns),
				fill_color='grey',
				line_color='darkslategray',
				align=['left','center']
				),
			cells=dict(
				values=[df_table1['Configuration'], df_table1['Critical_Freq'],df_table1['High_Freq'],
				df_table1['Medium_Freq'], df_table1['Low_Freq'],df_table1['Detail Page']],
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
			height=200,
			margin=go.layout.Margin(l=0, r=1, b=0, t=0)
			)
		
		table1.write_image("{}{}.png".format(v5, j))










