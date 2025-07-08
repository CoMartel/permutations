from typing import Dict, List, Optional, Set, Tuple

import numpy as np


def score_rotation(
    boys: List[str],
    girls: List[str],
    n_tables: int,
    n_iterations: int = 1,
    forbidden_pairs: Optional[List[Tuple[str, str]]] = None,
) -> List[List[List[str]]]:
    """Generates table rotations maximizing gender diversity and minimizing repeated pairings.

    Returns a list of rotations, each rotation is a list of tables, each table is a list of student
    names.
    """
    students = boys + girls
    n_students = len(students)
    score_matrix = initialize_score_matrix(students, boys, girls)
    forbidden_pairs = forbidden_pairs or []
    forbidden_dict = forbidden_pairs_to_dict(forbidden_pairs)
    rotations: List[List[List[str]]] = []
    # Precompute the length of each table for balanced distribution
    base_table_size = n_students // n_tables
    extra = n_students % n_tables
    table_lengths = [base_table_size + 1 if i < extra else base_table_size for i in range(n_tables)]
    for it in range(n_iterations):
        available = list(range(n_students))
        tables: List[List[str]] = [[] for _ in range(n_tables)]
        for seat in range(max(table_lengths)):
            for t, table in enumerate(tables):
                if len(table) >= table_lengths[t]:
                    continue
                # Find the best student to add to this table
                best_score = None
                best_idx = None
                for student_idx in available:
                    if forbidden_dict.get(students[student_idx], set()).intersection(table):
                        continue
                    if not table:
                        score = np.sum(score_matrix[student_idx, available])
                    else:
                        indices = [students.index(name) for name in table]
                        score = sum(score_matrix[student_idx, j] for j in indices)
                    if best_score is None or score > best_score:
                        best_score = score
                        best_idx = student_idx
                if best_idx is not None:
                    tables[t].append(students[best_idx])
                    available.remove(best_idx)
                if not available:
                    break
        # Update scores: each pair at the same table loses 1 point
        for table in tables:
            indices = [students.index(name) for name in table]
            for i in indices:
                for j in indices:
                    if i != j:
                        score_matrix[i, j] -= 1
        rotations.append(tables)
    return rotations


def initialize_score_matrix(students: List[str], boys: List[str], girls: List[str]) -> np.ndarray:
    """Create and initialize the score matrix for all students."""
    n_students = len(students)
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
    return score_matrix


def forbidden_pairs_to_dict(
    forbidden_pairs: Optional[List[Tuple[str, str]]],
) -> Dict[str, Set[str]]:
    """Convert a list of forbidden pairs (tuples) to a dict for fast lookup."""
    forbidden_dict: Dict[str, Set[str]] = {}
    if forbidden_pairs:
        for a, b in forbidden_pairs:
            forbidden_dict.setdefault(a, set()).add(b)
            forbidden_dict.setdefault(b, set()).add(a)
    return forbidden_dict
