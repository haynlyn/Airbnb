<class 'str'> -> bool -> int
<class 'numpy.float64'> -> float
<class 'float'> -> del
<class 'str'> -> datetime
<class 'str'> -> set
<class 'str'> -> int
<class 'numpy.float64'> -> int
<class 'float'> -> int
<class 'str'> -> float
<class 'numpy.float64'> -> del
<class 'str'> -> del
<class 'str'> -> str
<class 'str'> -> bool
<class 'float'> -> str


# This is to drop columns from l with the 7 most np.nan count. This should really be done. Nearly all of the data is na here.
l = l.drop(l.isna().sum().sort_values(ascending = False).head(7).index, axis = 1) 

def type_change(dic
  try:
    return float(x)
  except:
    return np.nan












