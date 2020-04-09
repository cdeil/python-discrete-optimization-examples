# Pyomo

**Probably one of the most powerful and best options, besides Google OR-Tools.**

* [Pyomo](https://www.pyomo.org/)
* [Wikipedia](https://en.wikipedia.org/wiki/Pyomo)
* Developed at [Sandia National Labs](https://en.wikipedia.org/wiki/Sandia_National_Laboratories) since 2008, part of the [COIN-OR](https://en.wikipedia.org/wiki/COIN-OR) project.
* Last release 5.6.9 from March 2020
* Supports Linux, MacOS, Windows
* Solvers: need to be installed extra, can interface to many open-source and commercial, and remote solve via NEOS
* Easy to install with pip or conda (see https://www.pyomo.org/installation)
* Active [development on Github](https://github.com/Pyomo/pyomo) (moved from Sandia to Github in 2016)
* Active [discussion forum](https://groups.google.com/forum/#!forum/pyomo-forum)
* Decent [documentation](https://www.pyomo.org/documentation)
* [Pyomo book](https://www.springer.com/gp/book/9783319588193) from 2017 that covers Pyomo v5 (not free)
* [ND-Pyomo-Cookbook](https://jckantor.github.io/ND-Pyomo-Cookbook/) from 2018 (free) - is it updated with Pyomo?
* Higher-level and more Pythonic API than Google OR-Tools?

Negative points:
* Old codebase and API with some quirks - e.g. "Set" is 1-indexed and seems to be an array.
* Old design with some limitations (see e.g. [GH issue](https://github.com/Pyomo/pyomo/issues/1349)) - created before Numpy, and way before e.g. Tensorflow or PyTorch
* Documentation in multiple places, examples/tutorials separate (updated?); most examples use `*` imports
* Doesn't interface to Google OR-Tools solvers, and doesn't support some of the features there, like routing. (Probably true the other way around as well, Pyomo has features that OR-Tools doesn't have?)


## Installation

Installation is very simple, since Pyomo and the open-source solvers have been packaged at conda-forge:

```
conda config --add channels conda-forge
conda install pyomo pyomo.extras coincbc ipopt glpk
```

## Sudoku

* https://github.com/Pyomo/pyomo/blob/master/examples/doc/pyomobook/scripts-ch/sudoku/sudoku.py
