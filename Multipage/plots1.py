import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('Visualise data')
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader('scatterplot')
  features_list=st.multiselect("select the x axis value",('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for i in features_list:
    st.subheader(f"scatter plot between{i}and price")
    plt.figure(figsize=(12,6))
    sns.scatterplot(x=i,y='price',data=car_df)
    st.pyplot()

  st.subheader("Visualisation Selector")
  plot_types = st.multiselect("Select charts or plots:", ('Histogram', 'Box Plot', 'Correlation Heatmap'))

  if 'Histogram' in plot_types:
    st.subheader("Histogram") 
    columns=st.selectbox("select the column for histogram",('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize=(12,6))
    plt.title(f"Hostogram for {columns}")
    plt.hist(columns=car_df[columns],bins='sturges',edgecolor='black')
    plt.show()
  if 'BoxPlot' in plot_types:
    st.subheader("Box Plot")
    columns = st.selectbox("Select the column to create its box plot",
                                      ('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize = (12, 2))
    plt.title(f"Box plot for {columns}")
    sns.boxplot(car_df[columns])
    st.pyplot()
  
  if 'Correlation Heatmap' in plot_types:
    st.subheader("Correlation Heatmap")
    plt.figure(figsize = (8, 5))
    sns.heatmap(car_df.corr(), annot = True)
    st.pyplot()
    