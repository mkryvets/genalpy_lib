from genalpy import Solver


solver_3d_min = Solver(task_type='func_extremum', create_population_method='shotgun',
                       selection_method='ranging', recombination_method='transitional', mutation_method='real_number',
                       reduction_method='selective_scheme', stop_criterion='generations_limit', stop_value=20,
                       n_pop=100, function='-x * (np.sin(np.sqrt(abs(x)))) + y * np.cos(np.sqrt(abs(y)))',
                       goal='min', dimensions=3, boundaries=[-30, 30, -10, 10])
solver_3d_min.solve()

solver_2d_max = Solver(task_type='func_extremum', create_population_method='shotgun',
                selection_method='ranging', recombination_method='transitional', mutation_method='real_number',
                 reduction_method='selective_scheme', stop_criterion='generations_limit', stop_value=20,
                 n_pop=50, function='-x*x + 4',
                 goal='max', dimensions=2, boundaries=[-100, 100])
solver_2d_max.solve()
