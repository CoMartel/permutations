import math
from typing import List

import numpy as np


def score_rotation(
    boys: List[str],
    girls: List[str],
    n_tables: int,
    n_iterations: int = 1,
) -> List[List[List[str]]]:
    """Génère des rotations de tables en maximisant la diversité de genre et en minimisant les
    répétitions.

    Retourne une liste de rotations, chaque rotation étant une liste de tables, chaque table étant
    une liste de noms d'étudiants.
    """
    students = boys + girls
    n_students = len(students)
    table_size = math.ceil(n_students / n_tables)
    # Initialisation de la matrice de scores
    score_matrix = np.zeros((n_students, n_students))
    for i in range(n_students):
        for j in range(n_students):
            if i == j:
                score_matrix[i, j] = 0
            elif (students[i] in boys and students[j] in boys) or (
                students[i] in girls and students[j] in girls
            ):
                score_matrix[i, j] = 0.5
            else:
                score_matrix[i, j] = 1
    rotations: List[List[List[str]]] = []
    for it in range(n_iterations):
        available = set(range(n_students))
        tables: List[List[str]] = [[] for _ in range(n_tables)]
        # Remplissage des tables
        for seat in range(table_size):
            for t in range(n_tables):
                if not available:
                    break
                current_table = tables[t]
                if not current_table:
                    idx = max(available, key=lambda i: np.sum(score_matrix[i, list(available)]))
                else:
                    indices = [students.index(name) for name in current_table]
                    idx = max(
                        available,
                        key=lambda i: sum(score_matrix[i, j] for j in indices),
                    )
                tables[t].append(students[idx])
                available.remove(idx)
        # Mise à jour des scores : chaque paire à la même table perd 1 point
        for table in tables:
            indices = [students.index(name) for name in table]
            for i in indices:
                for j in indices:
                    if i != j:
                        score_matrix[i, j] -= 1
        rotations.append(tables)
    return rotations
