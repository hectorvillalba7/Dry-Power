import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def run():
    # Read Data and filter the columns desired
    jpy_info = pd.read_excel(r'C:\Users\hector\Documents\trading\cftc data\years\dea_fut_jpy.xlsx')
    jpy_info['NonComm_Positions_Short_All'] = jpy_info['NonComm_Positions_Short_All'].map(lambda x: x*(-1))
    df_filtered = jpy_info[[
        "Traders_NonComm_Long_All", 
        "NonComm_Positions_Long_All", 
        "Traders_NonComm_Short_All", 
        "NonComm_Positions_Short_All"]]

    # create data for plotting
    x_long = df_filtered['Traders_NonComm_Long_All']
    y_long = df_filtered['NonComm_Positions_Long_All']
    x_short = df_filtered['Traders_NonComm_Short_All']
    y_short = df_filtered['NonComm_Positions_Short_All']

    # Red point
    first_point_long = go.Scatter(
        x=[x_long.iloc[0]],
        y=[y_long.iloc[0]],
        mode='markers',
        marker=dict(color='red', size=12, opacity=0.7),
        name='Last Long Position'
    )

    first_point_short = go.Scatter(
        x=[x_short.iloc[0]],
        y=[y_short.iloc[0]],
        mode='markers',
        marker=dict(color='red', size=12, opacity=0.7),
        name='Last Short Position'
    )

    # create scatter
    scatter_long = go.Scatter(
        x=x_long,
        y=y_long,
        mode='markers',
        marker=dict(color='blue', size=8, opacity=0.4),
        name='Long Positions'
    )

    scatter_short = go.Scatter(
        x=x_short,
        y=y_short,
        mode='markers',
        marker=dict(color='orange', size=8, opacity=0.4),
        name='Short Positions'
    )

    # Merge all in one figure
    fig = go.Figure(data=[scatter_long, scatter_short,first_point_long,first_point_short])

    fig.update_layout(
        title="Dry Power Indicator (JPY)",
        xaxis=dict(title="Number of Non-Commercial Traders", zeroline=True, zerolinecolor="black"),
        yaxis=dict(title="Open Interest"),
        legend=dict(title="Position Type"),
        plot_bgcolor="white",
        width=800,
        height=500
    )

    # Description
    st.title("Dry Power Indicator for Yen Futures (JPY)")
    st.subheader("From 2015 to 2025")
    st.markdown(
        """
        This chart shows a classic DP indicator for Yen futures. The individual long and 
        short non-commercial positions are plotted in the form of a scatter chart above and below the x-axis, respectively. Each point represents a week with the data going back to 2015.
        """
    )

    # deploy in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Dry Powder (DP) Analysis")
    st.markdown(
        """
         Dry Powder (DP) analysis is a simple and intuitive methodology used to visualise positioning. It reconciles the size of the long and short futures position (open interest) in a group (for example 
        the non-commercials group) against the number of individual long and short traders in that group. DP analysis requires that the underlying positioning data needs to report both the long and short open interest and the number of long and short traders.
        
        The objective of DP analysis is to provide an indication of how much bigger long or short position can get. Simply how much dry powder is available in that trader group to build the position 
        further. Conversely, DP analysis also provides an indication of how small a position can get. A useful metric when large positions unwind.
        """
    )