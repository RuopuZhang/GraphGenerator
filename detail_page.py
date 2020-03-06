import sys
import pandas as pd
import plotly.graph_objects as go



def Veh_detail_page(v1,v2,v3,v5,v6,v7):

        how_many_pages = len(v1)
        j=1
        for i in range(0,how_many_pages):
                #data frame, .csv file location
                df_fig1 = pd.read_csv(v1[i])
                df_fig2 = pd.read_csv(v2[i])
                df_table1 = pd.read_csv(v3[i])
                
                if pd.isnull(df_fig1.loc[1, 'b']) is True:
                        continue              
                #fig 1, bar graph
                fig1 = go.Figure(data = [
                	go.Bar(x = df_fig1['a'], y = df_fig1['e'],marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1),
                	go.Bar(x = df_fig1['a'], y = df_fig1['d'], marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1),
                	go.Bar(x = df_fig1['a'], y = df_fig1['c'], marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1),
                	go.Bar(x = df_fig1['a'], y = df_fig1['b'], marker_color='red', marker_line_color='black', marker_line_width=1, opacity=1),
                	])
                fig1.update_layout(
                	autosize=False,
                	plot_bgcolor='white',
                	showlegend=False,
                	barmode='stack',
                	width=600,
                	height=300,
                	xaxis = dict(
                		title_text="Time of day (h)",
                		showline=True,
                		linewidth=1, 
                		linecolor='black',
                		mirror=True,
                		ticks="outside",
                		range=[0, 23], 
                		dtick=1,
                		),
                	yaxis = dict(
                		title_text="Frequency",
                		showline=True,
                		linewidth=1, 
                		linecolor='black',
                		mirror=True,
                		ticks="inside",
                		range=[0, 30], 
                		dtick=5,
                		),
                	margin=go.layout.Margin(l=0, r=0, b=0, t=0)
                	)

                #fig 2, scatter graph
                fig2 = go.Figure(data = [
                	go.Scatter(x = df_fig2['Critical_Risk_PET'], y = df_fig2['Critical_Risk_Speed'], mode='markers', marker = dict(color = 'red', line=dict(width = 1, color= 'black'))),
                	go.Scatter(x = df_fig2['High_Risk_PET'], y = df_fig2['High_Risk_Speed'], mode='markers', marker = dict(color = 'orange', line=dict(width = 1, color= 'black'))),
                	go.Scatter(x = df_fig2['Medium_Risk_PET'], y = df_fig2['Medium_Risk_Speed'], mode='markers', marker = dict(color = 'yellow', line=dict(width = 1, color= 'black'))),
                	go.Scatter(x = df_fig2['Low_Risk_PET'], y = df_fig2['Low_Risk_Speed'], mode='markers', marker = dict(color = 'green', line=dict(width = 1, color= 'black'))),
                	])

                fig2.update_layout(
                	autosize=False,
                	showlegend=False,
                	width=600,
                	height=300,
                	xaxis = dict(
                		title_text="Post Encroachment Time (s)",
                		showgrid=False,
                		showline=True,
                		linewidth=1, 
                		linecolor='black',
                		mirror=True,
                		range=[0, 3], 
                		dtick=0.5,
                		),
                	yaxis = dict(
                		title_text="Vehicle Speed (km/h)",
                		showgrid=False,
                		showline=True,
                		linewidth=1, 
                		linecolor='black',
                		mirror=True,
                		range=[0, 100], 
                		dtick=10,
                		),
                	margin=go.layout.Margin(l=0, r=0, b=0, t=0),
                	shapes=[
                		#Green
                		go.layout.Shape(
                			type="rect",
                			xref="x",
                			yref="paper",
                			x0=0,
                			y0=0,
                			x1=3,
                			y1=0.35,
                			fillcolor="Green",
                			opacity=0.8,
                			layer="below",
                			line_width=0,
                			),
                        #yellow
                        go.layout.Shape(
                        	type="rect",
                        	xref="x",
                        	yref="y",
                        	x0=0,
                        	y0=35,
                        	x1=3,
                        	y1=50,
                        	fillcolor="Yellow",
                        	line_color="Yellow",
                        	opacity=0.8,
                        	layer="below",
                        	line_width=0,
                        	line=dict(
                        		color="Yellow",
                        		width=3,
                        		),
                        	),
                        # go.layout.Shape(
                        # 	type="rect",
                        # 	xref="x",
                        # 	yref="paper",
                        # 	x0=3,
                        # 	y0=0.5,
                        # 	x1=5,
                        # 	y1=1,
                        # 	fillcolor="Yellow",
                        # 	line_color="Yellow",
                        # 	opacity=0.5,
                        # 	layer="below",
                        # 	line_width=0,
                        # 	line=dict(
                        # 		color="Yellow",
                        # 		width=3,
                        # 		),
                        # 	),
                        #orange
                        go.layout.Shape(
                        	type="rect",
                        	xref="x",
                        	yref="paper",
                        	x0=0,
                        	y0=0.5,
                        	x1=3,
                        	y1=0.7,
                        	fillcolor="Orange",
                        	opacity=0.8,
                        	layer="below",
                        	line_width=0
                        	),
                        go.layout.Shape(
                        	type="rect",
                        	xref="x",
                        	yref="paper",
                        	x0=2,
                        	y0=0.7,
                        	x1=3,
                        	y1=1,
                        	fillcolor="Orange",
                        	opacity=0.8,
                        	layer="below",
                        	line_width=0
                        	),
                        #red
                        go.layout.Shape(
                        	type="rect",
                        	xref="x",
                        	yref="paper",
                        	x0=0,
                        	y0=0.7,
                        	x1=2,
                        	y1=1,
                        	fillcolor="Red",
                        	opacity=0.8,
                        	layer="below",
                        	line_width=0
                        	)
                        ]
                        )


                #table 1, table
                table1 = go.Figure(data=[go.Table(
                        columnorder = [1,2,3,4,5,],
                        columnwidth = [60,25,25,25,25],
                        header=dict(
                                values=list(df_table1.columns[0:5]),
                                font_color = 'black',
                                line = dict(color = 'black'),
                                fill = dict(color = ['grey','red','#ff7f0e','yellow','green']),
                                align=['center']
                                ),
                        cells=dict(
                                values=[df_table1[k].tolist() for k in df_table1.columns[0:5]],
                                font_color = 'black',
                                line = dict(color = 'black'),
                                fill = dict(color = ['grey','red','orange','yellow','green'])
                                )
                        )
                ])
                table1.update_layout(
                        autosize=False,
                        width=400,
                        height=135,
                        margin=go.layout.Margin(l=1, r=2, b=0, t=1)
                        )


                #save files
                fig1.write_image("{}{}.png".format(v5, j))
                fig2.write_image("{}{}.png".format(v6, j))
                table1.write_image("{}{}.png".format(v7, j))
                j += 1


def Ped_detail_page(v1,v2,v3,v5,v6,v7):

        how_many_pages = len(v1)
        j=1

        for i in range(0,how_many_pages):
                #data frame, .csv file location
                df_fig1 = pd.read_csv(v1[i])
                df_fig2 = pd.read_csv(v2[i])
                df_table1 = pd.read_csv(v3[i])

                if pd.isnull(df_fig1.loc[1, 'b']) is True:
                        continue 

                #fig 1, bar graph
                fig1 = go.Figure(data = [
                        go.Bar(x = df_fig1['a'], y = df_fig1['e'],marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1),
                        go.Bar(x = df_fig1['a'], y = df_fig1['d'], marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1),
                        go.Bar(x = df_fig1['a'], y = df_fig1['c'], marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1),
                        go.Bar(x = df_fig1['a'], y = df_fig1['b'], marker_color='red', marker_line_color='black', marker_line_width=1, opacity=1),
                        ])
                fig1.update_layout(
                        autosize=False,
                        plot_bgcolor='white',
                        showlegend=False,
                        barmode='stack',
                        width=600,
                        height=300,
                        xaxis = dict(
                                title_text="Time of day (h)",
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                ticks="outside",
                                range=[0, 23], 
                                dtick=1,
                                ),
                        yaxis = dict(
                                title_text="Frequency",
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                ticks="inside",
                                range=[0, 40], 
                                dtick=5,
                                ),
                        margin=go.layout.Margin(l=0, r=0, b=0, t=0)
                        )

                #fig 2, scatter graph
                fig2 = go.Figure(data = [
                        go.Scatter(x = df_fig2['Critical_Risk_PET'], y = df_fig2['Critical_Risk_Speed'], mode='markers', marker = dict(color = 'red', line=dict(width = 1, color= 'black'))),
                        go.Scatter(x = df_fig2['High_Risk_PET'], y = df_fig2['High_Risk_Speed'], mode='markers', marker = dict(color = 'orange', line=dict(width = 1, color= 'black'))),
                        go.Scatter(x = df_fig2['Medium_Risk_PET'], y = df_fig2['Medium_Risk_Speed'], mode='markers', marker = dict(color = 'yellow', line=dict(width = 1, color= 'black'))),
                        go.Scatter(x = df_fig2['Low_Risk_PET'], y = df_fig2['Low_Risk_Speed'], mode='markers', marker = dict(color = 'green', line=dict(width = 1, color= 'black'))),
                        ])

                fig2.update_layout(
                        autosize=False,
                        showlegend=False,
                        width=600,
                        height=300,
                        xaxis = dict(
                                title_text="Post Encroachment Time (s)",
                                showgrid=False,
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                range=[0, 3], 
                                dtick=0.5,
                                ),
                        yaxis = dict(
                                title_text="Vehicle Speed (km/h)",
                                showgrid=False,
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                range=[0, 65], 
                                dtick=15,
                                ),
                        margin=go.layout.Margin(l=0, r=0, b=0, t=0),
                        shapes=[
                                #Green
                                go.layout.Shape(
                                        type="rect",
                                        xref="x",
                                        yref="y",
                                        x0=0,
                                        y0=0,
                                        x1=3,
                                        y1=15,
                                        fillcolor="Green",
                                        opacity=0.5,
                                        layer="below",
                                        line_width=0,
                                        ),
                        #yellow
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=0,
                                y0=15,
                                x1=3,
                                y1=35,
                                fillcolor="Yellow",
                                line_color="Yellow",
                                opacity=0.8,
                                layer="below",
                                line_width=0,
                                line=dict(
                                        color="Yellow",
                                        width=3,
                                        ),
                                ),
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=2,
                                y0=35,
                                x1=3,
                                y1=65,
                                fillcolor="Yellow",
                                line_color="Yellow",
                                opacity=0.8,
                                layer="below",
                                line_width=0,
                                line=dict(
                                        color="Yellow",
                                        width=3,
                                        ),
                                ),
                        #orange
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=0,
                                y0=35,
                                x1=2,
                                y1=50,
                                fillcolor="Orange",
                                opacity=0.8,
                                layer="below",
                                line_width=0
                                ),
                        
                        #red
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=0,
                                y0=50,
                                x1=2,
                                y1=65,
                                fillcolor="Red",
                                opacity=0.8,
                                layer="below",
                                line_width=0
                                )
                        ]
                        )


                #table 1, table
                table1 = go.Figure(data=[go.Table(
                        columnorder = [1,2,3,4,5,],
                        columnwidth = [50,25,25,25,25],
                        header=dict(
                                values=list(df_table1.columns[0:5]),
                                font_color = 'black',
                                line = dict(color = 'black'),
                                fill = dict(color = ['grey','red','orange','yellow','green']),
                                align=['left','center']
                                ),
                        cells=dict(
                                values=[df_table1[k].tolist() for k in df_table1.columns[0:5]],
                                font_color = 'black',
                                line = dict(color = 'black'),
                                fill = dict(color = ['grey','red','orange','yellow','green']),
                                )
                        )
                ])
                table1.update_layout(
                        autosize=False,
                        width=400,
                        height=135,
                        margin=go.layout.Margin(l=1, r=2, b=0, t=1)
                        )


                #save files
                fig1.write_image("{}{}.png".format(v5, j))
                fig2.write_image("{}{}.png".format(v6, j))
                table1.write_image("{}{}.png".format(v7, j))
                j += 1 


def Cyc_detail_page(v1,v2,v3,v5,v6,v7):

        how_many_pages = len(v1)
        j=1
        for i in range(0,how_many_pages):
                #data frame, .csv file location
                df_fig1 = pd.read_csv(v1[i])
                df_fig2 = pd.read_csv(v2[i])
                df_table1 = pd.read_csv(v3[i])
                if pd.isnull(df_fig1.loc[1, 'b']) is True:
                        continue
                #fig 1, bar graph
                fig1 = go.Figure(data = [
                        go.Bar(x = df_fig1['a'], y = df_fig1['e'],marker_color='green', marker_line_color='black', marker_line_width=1, opacity=1),
                        go.Bar(x = df_fig1['a'], y = df_fig1['d'], marker_color='yellow', marker_line_color='black', marker_line_width=1, opacity=1),
                        go.Bar(x = df_fig1['a'], y = df_fig1['c'], marker_color='orange', marker_line_color='black', marker_line_width=1, opacity=1),
                        go.Bar(x = df_fig1['a'], y = df_fig1['b'], marker_color='red', marker_line_color='black', marker_line_width=1, opacity=1),
                        ])
                fig1.update_layout(
                        autosize=False,
                        plot_bgcolor='white',
                        showlegend=False,
                        barmode='stack',
                        width=600,
                        height=300,
                        xaxis = dict(
                                title_text="Time of day (h)",
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                ticks="outside",
                                range=[0, 23], 
                                dtick=1,
                                ),
                        yaxis = dict(
                                title_text="Frequency",
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                ticks="inside",
                                range=[0, 25], 
                                dtick=5,
                                ),
                        margin=go.layout.Margin(l=0, r=0, b=0, t=0)
                        )

                #fig 2, scatter graph
                fig2 = go.Figure(data = [
                        go.Scatter(x = df_fig2['Critical_Risk_PET'], y = df_fig2['Critical_Risk_Speed'], mode='markers', marker = dict(color = 'red', line=dict(width = 1, color= 'black'))),
                        go.Scatter(x = df_fig2['High_Risk_PET'], y = df_fig2['High_Risk_Speed'], mode='markers', marker = dict(color = 'orange', line=dict(width = 1, color= 'black'))),
                        go.Scatter(x = df_fig2['Medium_Risk_PET'], y = df_fig2['Medium_Risk_Speed'], mode='markers', marker = dict(color = 'yellow', line=dict(width = 1, color= 'black'))),
                        go.Scatter(x = df_fig2['Low_Risk_PET'], y = df_fig2['Low_Risk_Speed'], mode='markers', marker = dict(color = 'green', line=dict(width = 1, color= 'black'))),
                        ])

                fig2.update_layout(
                        autosize=False,
                        showlegend=False,
                        width=600,
                        height=300,
                        xaxis = dict(
                                title_text="Post Encroachment Time (s)",
                                showgrid=False,
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                range=[0, 3], 
                                dtick=0.5,
                                ),
                        yaxis = dict(
                                title_text="Vehicle Speed (km/h)",
                                showgrid=False,
                                showline=True,
                                linewidth=1, 
                                linecolor='black',
                                mirror=True,
                                range=[0, 65], 
                                dtick=15,
                                ),
                        margin=go.layout.Margin(l=0, r=0, b=0, t=0),
                        shapes=[
                                #Green
                                go.layout.Shape(
                                        type="rect",
                                        xref="x",
                                        yref="y",
                                        x0=0,
                                        y0=0,
                                        x1=3,
                                        y1=15,
                                        fillcolor="Green",
                                        opacity=0.8,
                                        layer="below",
                                        line_width=0,
                                        ),
                        #yellow
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=0,
                                y0=15,
                                x1=3,
                                y1=35,
                                fillcolor="Yellow",
                                line_color="Yellow",
                                opacity=0.8,
                                layer="below",
                                line_width=0,
                                line=dict(
                                        color="Yellow",
                                        width=3,
                                        ),
                                ),
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=2,
                                y0=35,
                                x1=3,
                                y1=65,
                                fillcolor="Yellow",
                                line_color="Yellow",
                                opacity=0.8,
                                layer="below",
                                line_width=0,
                                line=dict(
                                        color="Yellow",
                                        width=3,
                                        ),
                                ),
                        #orange
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=0,
                                y0=35,
                                x1=2,
                                y1=50,
                                fillcolor="Orange",
                                opacity=0.8,
                                layer="below",
                                line_width=0
                                ),
                        
                        #red
                        go.layout.Shape(
                                type="rect",
                                xref="x",
                                yref="y",
                                x0=0,
                                y0=50,
                                x1=2,
                                y1=65,
                                fillcolor="Red",
                                opacity=0.8,
                                layer="below",
                                line_width=0
                                )
                        ]
                        )


                #table 1, table
                table1 = go.Figure(data=[go.Table(
                        columnorder = [1,2,3,4,5,],
                        columnwidth = [50,25,25,25,25],
                        header=dict(
                                values=list(df_table1.columns[0:5]),
                                font_color = 'black',
                                line = dict(color = 'black'),
                                fill = dict(color = ['grey','red','orange','yellow','green']),
                                align=['left','center']
                                ),
                        cells=dict(
                                values=[df_table1[k].tolist() for k in df_table1.columns[0:5]],
                                font_color = 'black',
                                line = dict(color = 'black'),
                                fill = dict(color = ['grey','red','orange','yellow','green']),
                                )
                        )
                ])
                table1.update_layout(
                        autosize=False,
                        width=400,
                        height=135,
                        margin=go.layout.Margin(l=1, r=2, b=0, t=1)
                        )


                #save files
                fig1.write_image("{}{}.png".format(v5, j))
                fig2.write_image("{}{}.png".format(v6, j))
                table1.write_image("{}{}.png".format(v7, j))
                j += 1
