import pandas as pd

# ----------------------
# Author: Haya Kornblau
# Date  : 14/05/20 21:10
# ----------------------

# init
print('\nPosition Details.. Start')

# fetch data
print('\nPosition Details.. fetch position..')
pd.set_option('mode.chained_assignment', None)
df_Position = pd.read_csv('../data/tables/Position.csv')

# print data
print('\nPosition Details.. printing..')
print(df_Position)

# end
print('\nPosition Details.. Done!')
