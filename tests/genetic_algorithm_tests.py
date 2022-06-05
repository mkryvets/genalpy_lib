import unittest
import math
from genalpy import Solver


class GeneticTestCase(unittest.TestCase):

    def setUp(self):
        self.genetic = Solver(task_type='func_extremum', create_population_method='shotgun',
                 selection_method='ranging', recombination_method='transitional', mutation_method='real_number',
                 reduction_method='selective_scheme', stop_criterion='generations_limit', stop_value=10,
                 n_pop=100, function='-x * (np.sin(np.sqrt(abs(x)))) + y * np.cos(np.sqrt(abs(y)))',
                 goal='min', dimensions=3, boundaries=[-30, 30, -10, 10])


if __name__ == '__main__':
    unittest.main()