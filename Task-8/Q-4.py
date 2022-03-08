import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
for j in ser:
    a = j
    b = a.capitalize()
    print(b , end = " ")

