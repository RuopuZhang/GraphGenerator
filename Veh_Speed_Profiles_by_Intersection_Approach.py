import sys
import pandas as pd
import plotly.graph_objects as go


def Veh_speed_Profiles_by_Intersection_App(v1,v2,v3,v5,v6,v7):

    how_many_pages = len(v1)
    j=1
    for i in range(0,how_many_pages):
    
    #data frame, .csv file location
        df_table1 = pd.read_csv(v1[i])
        df_fig1 = pd.read_csv(v2[i])
        df_fig2 = pd.read_csv(v3[i])
    
        if pd.isnull(df_fig1.loc[2, 'Low_Freq']) is True:
            continue
        #table 1
        table1 = go.Figure(data=[go.Table(
            columnorder = [1,2],
            columnwidth = [50,25],
            header=dict(
            values=[['Speed Criteria'], ['Results']],
            font_color = 'black',
            fill_color='white',
            line_color='black',
            align=['center']
            ),
            cells=dict(
            values=[df_table1[k].tolist() for k in df_table1.columns[0:2]],
            font_color = 'black',
            fill_color='white',
            line_color='black',
            )
            )
        ])
        table1.update_layout(
            autosize=False,
            width=400,
            height=200,
            margin=go.layout.Margin(l=0, r=1, b=0, t=1)
            )


        #fig 1, line graph

        fig1 = go.Figure(go.Scatter(x = df_fig1['Cumulative_Bin'], y = df_fig1['Cumulative_Percentile']))
        fig1.update_layout(
        autosize=False,
        plot_bgcolor='white',
        width=600,
        height=300,
        xaxis = dict(
        title_text="Speed (km/h)",
        showline=True,
        linewidth=1, 
        linecolor='black',
        mirror=True,
        ticks="inside",
        range=[0, 100], 
        dtick=5,
        ),
        yaxis = dict(
        title_text="Cumulative Percentage (%)",
        showline=True,
        linewidth=1, 
        linecolor='black',
        mirror=True,
        ticks="inside",
        range=[0, 100], 
        dtick=10,
        ),
        margin=go.layout.Margin(l=0, r=0, b=0, t=0)
        )

        

        #fig 2, bar graph
        fig2 = go.Figure(data = [
        go.Bar(x = df_fig2['Low_Bin'], y = df_fig2['Low_Freq'],width=1, marker_color='green', marker_line_color='black', marker_line_width=0.8,opacity=1),
        go.Bar(x = df_fig2['Medium_Bin'], y = df_fig2['Medium_Freq'],width=1, marker_color='yellow', marker_line_color='black', marker_line_width=0.8,opacity=1),
        go.Bar(x = df_fig2['High_Bin'], y = df_fig2['High_Freq'], width=1, marker_color='orange', marker_line_color='black', marker_line_width=0.8,opacity=1),
        ])
        fig2.update_layout(
        autosize=False,
        plot_bgcolor='white',
        showlegend=False,
        width=650,
        height=300,
        xaxis = dict(
        title_text="Speed (km/h)",
        showline=True,
        linewidth=1, 
        linecolor='black',
        mirror=True,
        ticks="outside",
        range=[0, 50], 
        dtick=5,
        ),
        yaxis = dict(
        title_text="Frequency (%)",
        showline=True,
        linewidth=1, 
        linecolor='black',
        mirror=True,
        ticks="inside",
        range=[0, 15], 
        dtick=1,
        ),
        margin=go.layout.Margin(l=0, r=0, b=0, t=0)
        )


        table1.write_image("{}{}.png".format(v5, j))
        fig1.write_image("{}{}.png".format(v6, j))
        fig2.write_image("{}{}.png".format(v7, j))
        j += 1
