# How to use
Very easy. You just need to create consecutive pandas DataFrames, where each next DataFrame has the number of rows equal to the number of columns in the previous DataFrames (and their identical names — otherwise the package will warn you), and submit them into the class Net as a list.
```python
import pandas as pd
import multipartitegraph as mp

a_layer = [[1,1,0,0],[0,1,0,0]]
b_layer = [[1,0],[1,1],[0,1],[0,0]]
c_layer = [[1,1,0],[0,0,1]]
d_layer = [[0,1,0],[0,0,0],[1,0,1]]

a_layer_df = pd.DataFrame(a_layer)
a_layer_df.index = ['a1','a2']
a_layer_df.index.name = 'source'
a_layer_df.columns = ['b1','b2','b3','b4'] 

b_layer_df = pd.DataFrame(b_layer)
b_layer_df.index = a_layer_df.columns
b_layer_df.index.name = 'source'
b_layer_df.columns = ['c1','c2']

c_layer_df = pd.DataFrame(c_layer)
c_layer_df.index = b_layer_df.columns
c_layer_df.index.name = 'source'
c_layer_df.columns = ['d1','d2','d3']

d_layer_df = pd.DataFrame(d_layer)
d_layer_df.index = c_layer_df.columns
d_layer_df.index.name = 'source'
d_layer_df.columns = ['e1','e2','e3']

myNet = mp.Net([a_layer_df, b_layer_df, c_layer_df, d_layer_df])
myNet.plot()
```
![multipartite](https://user-images.githubusercontent.com/14263965/189504615-77254714-2a3f-43c2-abe9-088ed0b398a0.png)
