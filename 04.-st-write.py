import streamlit as st
import pandas as pd
import numpy as np
import altair
import matplotlib.pyplot as plt


st.header("st.write")

# Example -1 
st.subheader("1. Different styles")
st.write("Normal, **bold**, *italics*, :sunglasses: <-emojis, ")

# Example - 2
st.subheader("2. Display Numbers")
st.write(1234)

# Example - 3
st.subheader("3. Display DataFrame")

df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
})

st.write(df)

# Example - 4
st.subheader("4. Accept multiple arguments")

st.write("Below is a dataframe", df, "Above is a dataframe")

# Example - 5
st.subheader("5. Display charts")

df2 = pd.DataFrame(
    np.random.randn(200, 3),  # creates a 200 rows, 3 cols normal distribution  dataframe
    columns = ['a', 'b', 'c']
    )


chart = altair.Chart(df2).mark_circle().encode(
    x = 'a',
    y = 'b',
    size = 'c',
    color = 'c',
    tooltip = ['a', 'b', 'c']  # this means which param will be shown when mouse is hovered over the datapoint

)

# fig, ax = plt.subplots(figsize=(6, 4))
# ax.scatter(df2['a'], df2['b'], s = df2['c'], color='green')
# ax.set_xlabel('a')
# ax.set_ylabel('b')
# ax.set_title("Scatter")

# st.write(fig)



st.write(chart)

# Example - 6
st.subheader("6. matplotlib chart")

fig, ax = plt.subplots(figsize = (8, 4))
ax.bar(df['first column'], df['second column'], width = 0.5)
ax.set_xlabel("First")
ax.set_ylabel("Second")
ax.set_title("Bar chart example")

st.write(fig)

# Example - 7 : python dictionary

st.subheader("7. python dictionary")
mydict = dict()
s = "shivamsharma"

for i in s:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1
        
st.write(mydict)