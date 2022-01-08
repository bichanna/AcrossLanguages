function jl_hello(name::String)
	println("Hello $(name)")
end

## calling a Python function
using PyCall
pushfirst!(PyVector(pyimport("sys")."path"), @__DIR__)
pyhello = pyimport("python_hello")
pyhello.py_hello("bichanna")

## calling a R function
using RCall
R"""source("r_hello.R")"""
R"""r_hello("bichanna")"""