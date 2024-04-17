# Jason Miles, April 20224
# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
# Import Snowpark's Col Function
from snowflake.snowpark.functions import col
# Import core pythong random number generator
import random

# Write directly to the app
st.title(":cup_with_straw: Customise Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the Fruits you want to use in your Custom Smoothie!
    """)

name_on_order = st.text_input('Name on Smoothie:')
st.write ('The name on your Smoothie will be', name_on_order)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect (
    'Choose up to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
    )
# print raw form - JSON array
#st.text (ingredients_list)

# initiatise empty order
ingredients_string = ''

if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

# Use SQL to Insert
# st.write(ingredients_string)
# my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
#    values ('"""" + ingredients_string + """"')"""

# print raw form - shows what is built
#st.text (ingredients_string)


# Use SQL to Insert
#my_insert_stmt = """ insert into smoothies.public.orders.ingredients)
#   values ('"""" + ingredients_string + """"','""""+name_on_order+ """"')"""


#my_sql = f”insert into {table}”
my_sql = orders_table = 'smoothies.public.orders'
my_id=random.randint(1, 99999)

my_insert_stmt = f"insert into {orders_table} values ({my_id},FALSE,'{name_on_order}','{ingredients_string}',CURRENT_TIMESTAMP())"


#st.text(my_insert_stmt)

#st.write(my_insert_stmt)
#st.stop()

time_to_insert = st.button('Submit Order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")

# shows content of tables - debugging 
st.write(session.table(orders_table))