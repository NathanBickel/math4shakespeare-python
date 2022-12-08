# Import the rpy2 library and the r magic command
import rpy2 as robjects
from rpy2.robjects.packages import importr

# Import the R base and utils packages
base = importr('base')
utils = importr('utils')

# Use the r magic command to load the .rda files as R objects
%R load("/path/to/file1.rda")
%R load("/path/to/file2.rda")

# Convert the R objects to pandas DataFrames
df1 = robjects.r('file1')
df1 = pandas2ri.ri2py(df1)

df2 = robjects.r('file2')
df2 = pandas2ri.ri2py(df2)

# Save the DataFrames as .csv files
df1.to_csv("file1.csv")
df2.to_csv("file2.csv")
