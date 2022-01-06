function hello(name::String)
	println("Hello ", name)
end

using PyCall

pushfirst!(PyVector(pyimport("sys")."path"), @__DIR__)

pyhello = pyimport("python_hello")
pyhello.hello("bichanna")