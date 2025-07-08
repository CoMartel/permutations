"""Table rotation solver for organizing students into tables with constraints."""

import itertools
import random
from typing import List, Optional, Set, Tuple


class TableRotationSolver:
    """Solver for table rotation problems with various constraints."""

    def __init__(
        self,
        n_students: int,
        n_tables: int,
        forbidden_pairs: Optional[List[Set[int]]] = None,
        max_intersection: int = 3,
        max_attempts: int = 10000,
        needed_rotations: int = 25,
    ):
        """Initialize the table rotation solver.

        Args:
            n_students: Number of students to arrange
            n_tables: Number of tables available
            forbidden_pairs: List of sets containing pairs of students that cannot sit together
            max_intersection: Maximum number of students that can be shared between tables
            max_attempts: Maximum number of attempts to find a valid solution
            needed_rotations: Number of rotation configurations needed
        """
        self.n_students = n_students
        self.n_tables = n_tables
        self.forbidden_pairs = forbidden_pairs or []
        self.max_intersection = max_intersection
        self.max_attempts = max_attempts
        self.needed_rotations = needed_rotations
        self.students_per_table = n_students // n_tables

    def _check_forbidden_pairs(self, table: Tuple[int, ...]) -> bool:
        """Check if a table arrangement violates forbidden pair constraints."""
        return any(forbidden_pair.issubset(set(table)) for forbidden_pair in self.forbidden_pairs)

    def _check_intersection(self, table: Tuple[int, ...], used_tables: List[Set[int]]) -> bool:
        """Check if a table arrangement violates intersection constraints."""
        return any(
            len(set(table).intersection(prev_table)) >= self.max_intersection
            for prev_table in used_tables
        )

    def _handle_odd_student(
        self, tables: List[Tuple[int, ...]], used_tables: List[Set[int]]
    ) -> List[Tuple[int, ...]]:
        """Handle the case of an odd number of students."""
        missing_student = tuple(
            set(range(self.n_students)) - set(itertools.chain.from_iterable(tables))
        )

        # Find best table to add the odd student to
        best_score = None
        best_table_idx = None
        for idx, table in enumerate(tables):
            candidate_table = table + missing_student
            # Vérifie les paires interdites
            if self._check_forbidden_pairs(candidate_table):
                continue
            score = sum(
                len(set(candidate_table).intersection(prev_table)) for prev_table in used_tables
            )
            if best_score is None or score < best_score:
                best_score = score
                best_table_idx = idx
        if best_table_idx is not None:
            tables[best_table_idx] = tables[best_table_idx] + missing_student
        return tables

    def solve(self) -> List[List[Tuple[int, ...]]]:
        """Find valid table rotations satisfying all constraints.

        Returns:
            List of rotation configurations, where each configuration is a list of tables,
            and each table is a tuple of student IDs.
        """
        rotation_list = []

        for _ in range(self.max_attempts):
            tables: List[Tuple[int, ...]] = []
            used_tables: List[Set[int]] = []
            table: Tuple[int, ...] = tuple()

            # Generate random pairs of boys and girls (even/odd numbers)
            boys = random.sample(range(1, self.n_students, 2), self.n_students // 2)
            girls = random.sample(range(0, self.n_students, 2), self.n_students // 2)

            # Create pairs ensuring gender balance
            for boy, girl in zip(boys, girls):
                if self.forbidden_pairs and self._check_forbidden_pairs(table + (boy, girl)):
                    table = tuple()
                    tables = []
                    break

                table = table + (boy, girl)

                if len(table) == self.students_per_table:
                    if not self._check_intersection(table, used_tables):
                        tables.append(table)
                        used_tables.append(set(table))
                    table = tuple()

                    if len(tables) == self.n_tables:
                        # Handle odd number of students if necessary
                        if self.n_students % 2 == 1:
                            tables = self._handle_odd_student(tables, used_tables)

                        rotation_list.append(sorted(tables))
                        tables = []

            if len(rotation_list) >= self.needed_rotations:
                break

        if not rotation_list:
            raise RuntimeError("Could not find valid solution within maximum attempts")

        return rotation_list
