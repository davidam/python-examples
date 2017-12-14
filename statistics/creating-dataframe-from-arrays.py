import numpy as np
import pandas
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

print pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
