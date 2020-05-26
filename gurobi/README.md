# gurobipy

## Infos

* https://www.gurobi.com/

## Plus points

* Feature rich, has a solver and Python API for every problem
* Very high performance 

## Minus points

* Commercial license, cost and friction in dev process
* Function signature and docstring information doesn't show argument defaults
* Matrix interface (gurobipy.MVar) is immature (see comments below)

## Installation

As mentioned [here](https://www.gurobi.com/gurobi-and-anaconda-for-mac/), install gurobipy with these commands:

```
conda config --add channels http://conda.anaconda.org/gurobi
conda install gurobi
```

Then if you have a floating license as mentioned
[here](https://www.gurobi.com/documentation/9.0/quickstart_mac/setting_up_and_using_a_flo.html)
get a token from the Gurobi website, then create a license file via this command:

```
% grbgetkey <token>
info  : grbgetkey version 9.0.2, build v9.0.2rc0
info  : Contacting Gurobi key server...
info  : Key for license ID <id> was successfully retrieved
info  : License expires at the end of the day on 2020-05-15
info  : Saving license key...

In which directory would you like to store the Gurobi license key file?
[hit Enter to store it in /Library/gurobi]: 

error : Unable to create directory '/Library/gurobi', check write permissions

In which directory would you like to store the Gurobi license key file?
[hit Enter to store it in /Users/cdeil]: 

info  : License <id> written to file /Users/cdeil/gurobi.lic
```

Then as mentioned [here](https://www.gurobi.com/documentation/9.0/quickstart_mac/sta_a_token_server.html) start a token server via this command

```
% grb_ts
Gurobi Token Server version 9.0.2
Gurobi Token Server version 9.0.2 started: Mon Apr 27 18:23:07 2020
Gurobi Token Server syslog: /var/log/system.log
Gurobi license file: /Users/cdeil/gurobi.lic
Gurobi Token Server use limit: 1
```

Now the installation and license is set up, you can use gurobipy like any other package.

## Using Gurobi from Google OR-Tools

It is possible to use the Gurobi MIP solver as a backend for a model
defined via Google OR-Tools.

Instructions: https://developers.google.com/optimization/install/python/source_mac#third_party

Note that the OR-Tools Python interface is a SWIG wrapper of the OR-Tools C++ library.
The linking to the Gurobi solver can only happen at the C layer, not from Python.

The Gurobi Anaconda package (see https://www.gurobi.com/get-anaconda/ and above) doesn't
include C headers like `gurobi_c.h`, you can't use it from Google OR Tools.

Instead you have to download and install the Gurobi package as described here: 
https://www.gurobi.com/documentation/9.0/quickstart_mac/software_installation_guid.html

Settings for `Makefile.local`
```
UNIX_GUROBI_DIR=/Library/gurobi902
GUROBI_LIB_VERSION=90
```

Commands:
```
# You might need this or a few other build dependencies:
brew install swig
pip install virtualenv

make all # Runs for 10 min, then fails for .NET part, ignore that
PYTHONPATH=. python -c 'from ortools.linear_solver import pywraplp; print(pywraplp.Solver.GUROBI_MIXED_INTEGER_PROGRAMMING)
PYTHONPATH=. python examples/python/integer_programming.py
make test_package_python
make install_python
```

The `=GUROBI_MIXED_INTEGER_PROGRAMMING` is a drop-in replacement (at least for simple cases)
for the default `CBC_MIXED_INTEGER_PROGRAMMING` solver that finds solutions in more cases
and runs faster (for a small price).

## Example

### Python scripts

You can run examples:

```
python examples_from_gurobi/matrix1.py
python examples_from_gurobi/matrix2.py
```

The files in [examples_from_gurobi](examples_from_gurobi) are a copy of
`anaconda3/pkgs/gurobi-9.0.2-py37_0/share/doc/gurobi/examples/python`.
They don't seem to be available on Github, so I added them to this repo.
They are described a bit here: https://www.gurobi.com/resource/functional-code-examples/

### Jupyter notebooks

Gurobi also produced a nice set of gurobipy tutorials as Jupyter notebooks.
In this case, they are available via a Github repo.

* https://github.com/Gurobi/modeling-examples
* https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/

## Matrix MVar

Only examples from Gurobi:
- [examples_from_gurobi/matrix1.py](examples_from_gurobi/matrix1.py)
- [examples_from_gurobi/matrix2.py](examples_from_gurobi/matrix2.py)

Best documentation and examples for the new matrix interface:

* https://www.gurobi.com/wp-content/uploads/2020/04/gurobipy_matrixfriendly_webinar-slides.pdf

The matrix interface is very new, isn't fleshed out and mature yet.
I didn't manage to get `gurobipy.max_` to work, or `sum` in some cases,
and also `+` or `+=` doesn't seem to work for a `MLinExpr` and `LinExpr`
or generally mixing `MVar` or `MLinExpr` with int, float or other Gurobi
objects sometimes works, but often doesn't for no clear reason.

Overall I decided to just not use the matrix interface for now, but it might
become more attractive in the next releases.
