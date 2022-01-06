def hello(name):
	print(f"Hello {name}")

## calling a Julia function
from julia import Main
# julia.install() might be needed
Main.eval('include("julia_hello.jl")')
jl_hello = Main.eval("hello")
jl_hello("bichanna")