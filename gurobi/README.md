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

## Example

### Python scripts

You can run examples:

```
python examples_from_gurobi/matrix1.py
python examples_from_gurobi/matrix1.py
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

Best documentation and examples:

* https://www.gurobi.com/wp-content/uploads/2020/04/gurobipy_matrixfriendly_webinar-slides.pdf

