# python-discrete-optimization-examples

Quick try-out of (mostly Python) discrete optimization packages.

Contributions via pull requests welcome!

## What is this?

The goal here is to find some that are performant, flexible, widely used, easy
to install, easy to use, well maintained, have good documentation. At the
moment, the evaluation here is super limited, we just tried to install each code
and get one simple example to run.

*Unfortunately, it seems that the most performant packages in this domain, such
as [Gurobi](https://www.gurobi.com/) or
[CPLEX](https://www.ibm.com/analytics/cplex-optimizer) are proprietary and
expensive (on the order of 10 kEUR per year per user or machine). We will not
try those out here, since choosing an expensive product causes friction: how
many licenses, how to optimise their usage among developers and test and
production machines, convincing the company to buy it. If we were to buy a
commercial package, using `gurobipy` seems to be a good choice.*

See README files, Python scripts and notebooks in the sub-folders for each
package.

## Examples

* [Wikipedia Sudoku example](https://en.wikipedia.org/wiki/Sudoku)

## Codes

* [Google OR-Tools](https://developers.google.com/optimization) - see [ortools](ortools)
* [Pyomo](http://www.pyomo.org/) - see [pyomo](pyomo)
* [PySCIPOpt](https://github.com/SCIP-Interfaces/PySCIPOpt) interface to [SCIP](https://scip.zib.de/)
* [JuMP](https://jump.dev/) (this one is Julia, not Python)
* [PuLP](https://coin-or.github.io/pulp/)
* [NEOS Server](https://neos-server.org/)
* from scratch implementation in Python

## Execute

One way to install the codes is to install [Anaconda](https://www.anaconda.com/)
and use this to install all codes:

```
conda env create -f environment.yml
conda activate python-discrete-optimization-examples
```

## Other

* https://norvig.com/sudoku.html
* https://www.coursera.org/learn/discrete-optimization

