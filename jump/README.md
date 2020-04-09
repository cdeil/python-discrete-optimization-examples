# JuMP

## Infos

* https://jump.dev/
* Started in 2012, shortly after Julia was created
* Significant breaking changes in Jump v0.19 in Feb 2019 to fix things based on lessons learnt
* Last release v0.21.2 from April 2020
* Solvers: supports many open-source and commercial solvers, need to be installed separately
* [2013 JuMP paper](https://arxiv.org/abs/1312.1431)
* [2017 JuMP paper](https://mlubin.github.io/pdf/jump-sirev.pdf)

## Plus points

* Very modern implementation, nice API
* Most active open-source discrete optimization project? (yearly workshops, Numfocus support)

## Minus points

* Still work in progress, not fully stable or feature-complete yet (see [JuMP 1.0 roadmap](https://www.juliaopt.org/JuMP.jl/stable/roadmap/))
* No JuMP conda package, have to use Julia package manager (try [Conda.jl](https://github.com/JuliaPy/Conda.jl)?)
* It's Julia, and our team so far only uses Python, need to build up some expertise

## Installation

I used Homebrew to install Julia:

```
brew cask install julia
```

Package install is pretty fast:

```
$ julia

import Pkg
Pkg.add("JuMP")
Pkg.add("GLPK")
Pkg.add("Ipopt")
Pkg.add("Cbc")
```

First-time import will trigger pre-compilation, also pretty fast:

```
$ julia

using JuMP
using GLPK
using Ipopt
using Cbc
```


## Sudoku

* https://github.com/JuliaOpt/JuMP.jl/blob/master/examples/sudoku.jl
* https://github.com/JuliaOpt/juliaopt-notebooks/blob/master/notebooks/JuMP-Sudoku.ipynb
