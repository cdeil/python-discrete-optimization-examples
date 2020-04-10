# python-discrete-optimization-examples

Quick try-out of (mostly Python) discrete optimization packages.

Contributions via pull requests welcome!

## What is this?

The goal here is to find some that are performant, flexible, widely used, easy
to install, easy to use, well maintained, have good documentation. At the
moment, the evaluation here is super limited, we just tried to install each code
and get one simple example to run.

See README files, Python scripts and notebooks in the sub-folders for each
package.

## Examples

* A `*_getting_started.py` for each package, with the front-page docs example, so that you can try it out quickly.
* [Wikipedia Sudoku example](https://en.wikipedia.org/wiki/Sudoku)

## Open-source codes

* [Google OR-Tools](https://developers.google.com/optimization) - see [ortools](ortools)
* [Pyomo](http://www.pyomo.org/) - see [pyomo](pyomo)
* [JuMP](https://jump.dev/) - see [jump](jump) (this one is Julia, not Python)
* [PuLP](https://coin-or.github.io/pulp/) - see [pulp](pulp)
* [Python-MIP](https://www.python-mip.com/) - see [mip](mip)
* [CVXPY](https://www.cvxpy.org/) - see [cvxpy](cvxpy)

Note that there's two things:
* [algebraic modeling languages](https://en.wikipedia.org/wiki/Algebraic_modeling_language)
* Solvers, see e.g.
  [here](https://www.juliaopt.org/JuMP.jl/stable/installation/) or
  [here](https://en.wikipedia.org/wiki/AMPL#Solvers) or
  [here](https://github.com/joaojunior/awesome-operational_research#solvers).

We're only looking at codes where the modeling language is a Python API.
Sometimes the line is a bit blurry and a package has built-in solvers, but
usually the solvers are separate.

The list above is not extensive at all - just the best options we found so far.

## Commercial codes

Unfortunately, it seems that the most performant packages in this domain, such
as [Gurobi](https://www.gurobi.com/), [SCIP](https://scip.zib.de/) or
[CPLEX](https://www.ibm.com/analytics/cplex-optimizer) are proprietary and
expensive (on the order of 10 kEUR per year per user or machine). We will not
try those out here, since choosing an expensive product causes friction: how
many licenses, how to optimise their usage among developers and test and
production machines, convincing the company to buy it. If we were to buy a
commercial package, using `gurobipy` seems to be a good choice.

Most of the packages mentioned above (Google OR-Tools, Pyomo, JuMP) offer a
model definition API, and have flexible solver backend support, including these
commercial solvers. So a possible strategy, if the modeling tool is good enough,
to stick with it, and only make a small change to hook up to a better solver at
some later time, if needed.

There's also [NEOS Server](https://neos-server.org/) which could be used to try
out different solvers, including the commercial ones, without purchasing a
license, albeit only on test or open data.

## Installation

One way to install the codes is to install [Anaconda](https://www.anaconda.com/)
and use this to install all codes:

```
conda create -n python-discrete-optimization-examples anaconda
conda activate python-discrete-optimization-examples
conda config --add channels conda-forge
conda install pyomo pyomo.extras coincbc ipopt glpk
conda install pulp
pip install ortools
pip install mip
pip install cvxpy
```

The COIN and OR-Tools packaging is being improved, see e.g.
[here](https://github.com/coin-or/COIN-OR-OptimizationSuite) and
[here](https://github.com/conda-forge/staged-recipes/issues/2717). There's a
COIN-OR
[optimization-suite-docker](https://github.com/tkralphs/optimization-suite-docker),
and we could also create our own docker image with all the codes we want to use.

For the Julia and JuMP installation instrucations, see [jump](jump)

## References

### Books

* https://www.manning.com/books/classic-computer-science-problems-in-python
* https://www.apress.com/de/book/9781484234228

### Courses

* https://www.coursera.org/learn/discrete-optimization
* https://www.coursera.org/learn/basic-modeling
* https://www.coursera.org/learn/julia-programming
* https://www.edx.org/course/optimization-methods-for-business-analytics

### Sudoku

* https://emerentius.github.io/sudoku_web/
* https://norvig.com/sudoku.html
