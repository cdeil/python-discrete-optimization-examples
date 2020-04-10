# Google OR-Tools

## Infos

* [Google OR-Tools](https://developers.google.com/optimization)
* Open-sourced by Google in 2015
* Last release v7.5 from Jan 2020
* Written in C++, also supports Python, C#, Java
* Supports Linux, MacOS, Windows
* Solvers: several performant ones built-in, can interface to other popular open-source and commercial ones
* Google internally uses Gurobi and SCIP solvers, which have much better performance than the OSS MIP solvers.
* Easy pip install ([PyPI](https://pypi.org/project/ortools/))
* Active [development on Github](https://github.com/google/or-tools)
* Active [discussion forum](https://groups.google.com/forum/#!forum/or-tools-discuss)
* Good high-level documentation with examples, API documentation not polished (auto wrapper code?)
* Book from apress from 2018: [Practical Python AI Projects](https://www.apress.com/de/book/9781484234228) (not free)

## Plus points

* Probably one of the most powerful and best options, besides Pyomo

## Minus points

* API is 1:1 translation of C++ API in all wrappers - low-level and not Pythonic
* No MIP solver built-in, only links to OSS ones, performance not on par with e.g. Gurobi
* No conda-forge package yet (see [conda-forge issue](https://github.com/conda-forge/staged-recipes/issues/2717))

## Installation

```
pip install ortools
```

Test:

```
python -c "from ortools.linear_solver import pywraplp"
```

## Examples

* [sudoku_ortools.ipynb](sudoku_ortools.ipynb)
* https://github.com/google/or-tools/blob/master/examples/python/sudoku_sat.py
* https://gitlab.hce.heidelbergcement.com/jtherhaa/ortools_playground/blob/master/src/notebooks/sudoku_ortools.ipynb
