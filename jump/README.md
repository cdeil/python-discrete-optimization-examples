# JuMP

## Infos

* https://jump.dev/
* Started in 2012, significant breaking changes in Jump v0.19 in Feb 2019
* Last release v0.21.2 from April 2020
* Solvers: supports many open-source and commercial solvers, need to be installed separately

## Plus points

* Very modern implementation, nice API
* Most active open-source discrete optimization project? (yearly workshops, Numfocus support)

## Minus points

* Still work in progress, not fully stable or feature-complete yet
* It's Julia, and our team so far only uses Python

## Installation

```
brew cask install julia
```

```
import Pkg
Pkg.add("JuMP")
Pkg.add("GLPK")
Pkg.add("Ipopt")
```

## Sudoku

* https://github.com/JuliaOpt/JuMP.jl/blob/master/examples/sudoku.jl
* https://github.com/JuliaOpt/juliaopt-notebooks/blob/master/notebooks/JuMP-Sudoku.ipynb
