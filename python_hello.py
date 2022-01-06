def hello(name):
	print(f"Hello {name}")

## calling a Julia function
from julia import Main
# julia.install() might be needed
Main.eval('include("julia_hello.jl")')
jl_hello = Main.eval("hello")
jl_hello("bichanna")

## calling a R function
import rpy2.robjects as robjects
r = robjects.r
r["source"]("r_hello.R")
r_hello = robjects.globalenv["hello"]
r_hello("bichanna")