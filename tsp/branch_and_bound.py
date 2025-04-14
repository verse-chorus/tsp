"""
Branch and Bound algorithm implementation for the Traveling Salesman Problem.
"""

from typing import List, Tuple, Optional
import numpy as np
from .city import City
from .route import Route
import time

class BranchNode:
    def __init__(self, matr):
        self.matrix = matr.copy()
        self.rminval = []
        self.cminval = []
        self.matchange()
        self.value = sum(self.rminval) + sum(self.cminval)

    def est(self, matrix):
        e = sum(self.rmin(matrix)) + sum(self.cmin(matrix))
        return e

    def rmin(self, matrix):
        minl = []
        n = len(matrix)
        for i in range(n):
            min_val = np.inf
            for j in range(n):
                if matrix[i][j] == 0:
                    min_val = 0
                    break
                if matrix[i][j] < min_val:
                    min_val = matrix[i][j]
            if min_val == np.inf:
                min_val = 0
            minl.append(min_val)
        return minl

    def cmin(self, matrix):
        minl = []
        n = len(matrix)
        for j in range(n):
            min_val = np.inf
            for i in range(n):
                if matrix[i][j] == 0:
                    min_val = 0
                    break
                elif matrix[i][j] < min_val:
                    min_val = matrix[i][j]
            if min_val == np.inf:
                min_val = 0
            minl.append(min_val)
        return minl

    def evalz(self):
        n = len(self.matrix)
        maxsum = 0
        si = 0
        sj = 0
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 0:
                    minx = np.inf
                    miny = np.inf
                    for k in range(n):
                        if self.matrix[i][k] < miny and k != j:
                            miny = self.matrix[i][k]
                        if self.matrix[k][j] < minx and k != i:
                            minx = self.matrix[k][j]
                    if minx + miny > maxsum:
                        maxsum = minx + miny
                        si = i
                        sj = j
        return si, sj

    def getbranch(self, di, dj):
        n = len(self.matrix)
        an1 = self.matrix.copy()
        an1[dj][di] = np.inf
        for i in range(n):
            for j in range(n):
                if i == di or j == dj:
                    an1[i][j] = np.inf

        an2 = self.matrix.copy()
        an2[di][dj] = np.inf
        e1 = self.est(an1)
        e2 = self.est(an2)
        if e1 > e2:
            self.matrix = an2
            return self, e2
        else:
            self.matrix = an1
            return self, e1

    def matchange(self):
        m1 = self.rmin(self.matrix)
        self.rminval = m1
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                self.matrix[i][j] -= m1[i]

        m2 = self.cmin(self.matrix)
        self.cminval = m2
        for j in range(n):
            for i in range(n):
                self.matrix[i][j] -= m2[j]

class BranchAndBound:
    """
    Branch and Bound algorithm implementation for solving the Traveling Salesman Problem.
    """
    
    def __init__(self):
        self.best_route: Optional[Route] = None
        self.best_length = float('inf')
        
    def run(self, cities: List[City], time_limit: float = 60.0) -> Tuple[Route, float]:
        """
        Run the Branch and Bound algorithm.
        
        Args:
            cities (List[City]): List of cities to visit
            time_limit (float): Maximum time to run in seconds
            
        Returns:
            Tuple[Route, float]: Best route found and time taken
        """
        start_time = time.time()
        
        # Create cost matrix from cities
        n = len(cities)
        cost_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i != j:
                    cost_matrix[i][j] = cities[i].distance_to[cities[j].name]
                else:
                    cost_matrix[i][j] = np.inf

        # Run the Branch and Bound algorithm
        size = n
        mat = np.array(cost_matrix)
        mat = mat.astype(float)
        amat = BranchNode(mat)
        e0 = amat.value

        while size > 1:
            bri, brj = amat.evalz()
            amat, e00 = amat.getbranch(bri, brj)
            e0 += e00
            size -= 1

        # Create route from the solution
        route = []
        visited = [False] * n
        current = 0
        route.append(cities[current])
        visited[current] = True

        for _ in range(n - 1):
            min_dist = float('inf')
            next_city = -1
            for j in range(n):
                if not visited[j] and cost_matrix[current][j] < min_dist:
                    min_dist = cost_matrix[current][j]
                    next_city = j
            route.append(cities[next_city])
            visited[next_city] = True
            current = next_city

        self.best_route = Route(route)
        self.best_length = e0

        return self.best_route, time.time() - start_time 