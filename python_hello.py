def py_hello(name):
	print(f"Hello {name}")

## calling a Julia function
from julia import Main
Main.eval('include("julia_hello.jl")')
jl_hello = Main.eval("jl_hello")
jl_hello("bichanna")

## calling a R function
import rpy2.robjects as robjects
r = robjects.r
r["source"]("r_hello.R")
r_hello = robjects.globalenv["r_hello"]
r_hello("bichanna")