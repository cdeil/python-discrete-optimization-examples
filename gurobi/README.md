# gurobipy

## Infos

* https://www.gurobi.com/

## Plus points

* Feature rich, has a solver and Python API for every problem
* Very high performance 

## Minus points

* Commercial license, cost and friction in dev process
* Function signature and docstring information doesn't show argument defaults

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

## Example

The [gurobi_getting_started.py](gurobi_getting_started.py) example is a slightly modified version of the example
[here](https://www.gurobi.com/documentation/9.0/quickstart_mac/py_example_mip1_py.html):

```
% python gurobi/gurobi_getting_started.py
Using license file /Users/cdeil/gurobi.lic
Set parameter TokenServer to value Christophs-MacBook-Pro.local
Gurobi Optimizer version 9.0.2 build v9.0.2rc0 (mac64)
Optimize a model with 2 rows, 3 columns and 5 nonzeros
Model fingerprint: 0xf43f5bdf
Variable types: 0 continuous, 3 integer (3 binary)
Coefficient statistics:
  Matrix range     [1e+00, 3e+00]
  Objective range  [1e+00, 2e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 4e+00]
Found heuristic solution: objective 2.0000000
Presolve removed 2 rows and 3 columns
Presolve time: 0.00s
Presolve: All rows and columns removed

Explored 0 nodes (0 simplex iterations) in 0.00 seconds
Thread count was 1 (of 8 available processors)

Solution count 2: 3 

Optimal solution found (tolerance 1.00e-04)
Best objective 3.000000000000e+00, best bound 3.000000000000e+00, gap 0.0000%
x 1
y 0
z 1
Obj: 3
```

The [matrix1.py](matrix1.py) example is from
[here](https://www.gurobi.com/documentation/9.0/quickstart_mac/py_example_matrix1_py.html).
It shows the matrix interface added to Gurobipy 9.0, see tutorial
[here](https://www.gurobi.com/resource/gurobi-python-interface-matrix-friendly-modeling-techniques/).

More working examples:

* https://github.com/Gurobi/modeling-examples
* https://www.gurobi.com/resource/functional-code-examples/
* https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/
