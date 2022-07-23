
import streamlit
streamlit.title('My parents healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('\N{blueberries} Omega3 & Blueberry Oatmeal')
streamlit.text('(\N{leafy green} Kale, Spinach & Rocket Smoothie');
streamlit.text('\N{egg} Hard-Boiled Free-Range Egg');
streamlit.text('\N{avocado} Avocado Toast');


streamlit.title('\N{grapes}\N{red apple}\N{green apple}Build your own fruit smoothie\N{mango}\N{pear}\N{peach}')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)                
