# pip install pandas streamlit plotly
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Graph", layout="wide")
if "traces" not in st.session_state:
    st.session_state["traces"] = []
# TO Run the streamlit app, write into the console 'streamlit run app.py'
st.title("Graph")
st.write("Toto je test Mirkova programu"
         )
# Creates uploader
uploaded_file = st.file_uploader("Upload a csv file")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep = ",")
        st.dataframe(df)
    # Download example data from:
    # https://github.com/bracerino/2D_plot_example
        st.subheader("add date to the plot")
        col1, col2,col3  = st.columns([1,1,2])
        with col1:
            x_column = st.selectbox("Select x-axis column", df.columns)
        with col2:
            y_column = st.selectbox("Select y-axis column", df.columns)

        col3, col4, col5 = st.columns(3)
        with col3:
            x_label = st.text_input("Name of the x-axis label",value=x_column)
        with col4:
            y_label = st.text_input("Name of the y-axis label", value=y_column)
        with col5:
            legend_name = st.text_input("Name of the legend", value=f"{x_column} vs {y_column}")

        if st.button("add to plot", type="primary"):
            new_trace = {
                "x": df[x_column].tolist(),
                "y": df[y_column].tolist(),
                "name": legend_name,
                "x_label": x_column,
                "y_label": y_column
            }
            st.session_state["traces"].append(new_trace)
            st.success(f"Added {x_column} vs {y_column} to plot"
                       f"{st.session_state["traces"]}")
        if st.button("remove traces", type="primary"):
            st.session_state.traces = []
            st.success(f"Removed all: {st.session_state["traces"]}")




    except Exception as e:
        st.error(f"toto je chyba {e}")
        #st.session_state["traces"].append(df)

if st.session_state["traces"]:
    fig = go.Figure()
    for trace in st.session_state["traces"]:
        fig.add_trace(go.Scatter(x=trace["x"], y=trace["y"],
                                 name=trace["name"],))
    st.plotly_chart(fig, width="stretch")
    



