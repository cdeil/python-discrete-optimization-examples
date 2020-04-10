from mip import Model, MAXIMIZE, CBC, INTEGER, OptimizationStatus

model = Model(sense=MAXIMIZE, solver_name=CBC)
x = model.add_var(name="x", var_type=INTEGER, lb=0, ub=10)
y = model.add_var(name="y", var_type=INTEGER, lb=0, ub=10)
model += x + y <= 10
model.objective = x + y
status = model.optimize(max_seconds=2)
status == OptimizationStatus.OPTIMAL
print("Result:")
print(x.x)
print(y.x)
