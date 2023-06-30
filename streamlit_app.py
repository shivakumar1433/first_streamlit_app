import streamlit
import pandas
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 🥗  Omega 3  & blueberry oatmeal')
streamlit.text('🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled free range-egg')
streamlit.text('🥑🍞 avocado toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
