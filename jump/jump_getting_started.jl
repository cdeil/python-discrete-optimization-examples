# Use modeling and optimizer package
using JuMP
using GLPK

# Define the model
model = Model(GLPK.Optimizer)
@variable(model, x >= 0)
@variable(model, y >= 0)
@constraint(model, 6x + 8y >= 100)
@constraint(model, 7x + 12y >= 120)
@objective(model, Min, 12x + 20y)

# Optimize the model
optimize!(model)

# Show results
@show value(x);
@show value(y);
@show objective_value(model);


