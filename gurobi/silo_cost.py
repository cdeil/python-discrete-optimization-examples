import gurobipy


def gurobi_test_low_silo_cost():
    """Attempt to get low silo cost term to work with Gurobi.

    It seems `MVar` and `MLinExpr` doesn't play nice with `max_` and `sum`
    Also it seems MLinExpr and LinExpr can't be mixed in expressions.
    """
    n_bin = 5
    price = 10 * np.ones(n_bin)

    model = gurobipy.Model()

    milling = model.addMVar(n_bin, vtype=GRB.BINARY)
    cost_milling = milling @ price

    silo = model.addMVar(n_bin, vtype=GRB.CONTINUOUS, lb=2, ub=10)
    silo_min = 7 * np.ones(n_bin)
    # import IPython; IPython.embed()
    cost_silo = (silo_min - silo) @ price

    model.setObjective(cost_milling + cost_silo, sense=GRB.MINIMIZE)
    model.optimize()

    print(f"milling: {milling.x}")
    print(f"cost_milling: {np.sum(cost_milling.x.obj * cost_milling.x.x)}")
    print(f"silo: {silo.x}")
    print(f"cost_silo: {np.sum(cost_silo.x.obj * cost_silo.x.x)}")
    print(f'Obj: {model.objVal}')


def gurobi_test_low_silo_cost():
    """Attempt to get low silo cost term to work with Gurobi.

    It seems `MVar` and `MLinExpr` doesn't play nice with `max_` and `sum`
    """
    n_bin = 5
    price = 10 * np.ones(n_bin)

    model = gurobipy.Model()

    milling = model.addVars(n_bin, vtype=GRB.BINARY)
    cost_milling = sum(milling[i] * price[i] for i in range(n_bin))

    silo = model.addVars(n_bin, vtype=GRB.CONTINUOUS, lb=2, ub=10)
    silo_min = 7 * np.ones(n_bin)
    cost_silo = sum((silo_min[i] - silo[i]) * price[i] for i in range(n_bin))
    model.update()

    model.setObjective(cost_milling + gurobipy.max_(cost_silo, 2) - 99, sense=GRB.MINIMIZE)
    model.optimize()

    import IPython;
    IPython.embed()

    print(f"milling: {[_.x for _ in milling.values()]}")
    print(f"cost_milling: {cost_milling.getValue()}")
    print(f"silo: {[_.x for _ in silo.values()]}")
    print(f"cost_silo: {cost_silo.getValue()}")
    print(f'Obj: {model.objVal}')
