""" A sensor placement optimizer """
import numpy as np
import copy
from docplex.mp.model import Model

# Qiskit imports
from qiskit import Aer
from qiskit.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler
from qiskit.utils.algorithm_globals import algorithm_globals
from qiskit_optimization.algorithms import MinimumEigenOptimizer, CplexOptimizer
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.problems.variable import VarType
from qiskit_optimization.converters.quadratic_program_to_qubo import (
    QuadraticProgramToQubo,
)
from qiskit_optimization.translators import from_docplex_mp

import rustworkx
import matplotlib.pyplot as plt
from rustworkx.visualization import mpl_draw

import pandas as pd
import random


from pyqubo import Binary
from pyqubo import Array
from pprint import pprint
import neal


class SensorPlacementOptimizer:
    def __init__(self, node_params, edge_params, cost_params):
        self.node_params = node_params
        self.edge_params = edge_params
        self.reset()

    @property
    def graph(self):
        if self.__graph is None:
            self.__graph = self.gen_graph()

        return self.__graph

    def reset(self):
        self.__graph = None

    def gen_graph(self):
        graph = rustworkx.PyGraph()

        C = self.cost_params.get("C", 2)
        D = self.cost_params.get("D", 2)

        name2index = {}

        for node_name, node_data in self.node_params.items():
            self.name2index[node_name] = graph.add_node(
                {"name": node_name, **node_data}
            )

        for edge_name, edge_data in self.edge_params.items():
            node0_name, node1_name = edge_name
            if node0_name not in self.name2index:
                self.name2index[node0_name] = graph.add_node(
                    {
                        "name": node0_name,
                    }
                )

            elif node0_name not in self.name2index:
                self.name2index[node1_name] = graph.add_node(
                    {
                        "name": node1_name,
                    }
                )

            graph.add_edge(name2index[node0_name], name2index[node1_name], edge_data)

        return graph
