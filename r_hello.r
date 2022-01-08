r_hello <- function(name) {
	print(paste("Hello", name, sep=" "))
}

## calling a Python function
# install.packages("reticulate", repos="http://cran.us.r-project.org") # might be needed
library("reticulate")
use_python("/usr/local/bin/python3", required=T) # choose python you want
source_python("python_hello.py")
py_hello("bichanna")