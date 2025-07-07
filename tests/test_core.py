import pytest

from permutations.core.table_rotation import TableRotationSolver


class TestTableRotationSolver:
    n_tables = 3
    needed_rotations = 5
    max_attempts = 5000
    # You can add more shared parameters here for future tests

    @pytest.mark.parametrize("n_students", [12, 13])
    def test_table_rotation_unique_students_per_rotation(self, n_students: int) -> None:
        solver: TableRotationSolver = TableRotationSolver(
            n_students=n_students,
            n_tables=self.n_tables,
            needed_rotations=self.needed_rotations,
            max_attempts=self.max_attempts,
        )
        rotations = solver.solve()
        for rotation in rotations:
            all_students = [student for table in rotation for student in table]
            assert len(all_students) == len(
                set(all_students)
            ), f"A student is duplicated in the rotation: {rotation}"
            assert (
                len(all_students) == n_students
            ), f"Some students are missing or extra in the rotation: {rotation}"

    @pytest.mark.parametrize("n_students", [12, 13])
    def test_table_rotation_parity_respected(self, n_students: int) -> None:
        solver = TableRotationSolver(
            n_students=n_students,
            n_tables=self.n_tables,
            needed_rotations=self.needed_rotations,
            max_attempts=self.max_attempts,
        )
        rotations = solver.solve()
        for rotation in rotations:
            all_students = [student for table in rotation for student in table]
            even_count = sum(1 for s in all_students if s % 2 == 0)
            odd_count = sum(1 for s in all_students if s % 2 == 1)
            assert (
                abs(even_count - odd_count) <= 1
            ), f"Parity not respected: even={even_count}, odd={odd_count}, students={all_students}"

    @pytest.mark.parametrize("n_students,n_tables", [(12, 4)])
    def test_table_rotation_invalid_division(self, n_students: int, n_tables: int) -> None:
        with pytest.raises(ValueError):
            TableRotationSolver(
                n_students=n_students,
                n_tables=n_tables,
                needed_rotations=self.needed_rotations,
                max_attempts=self.max_attempts,
            )

    def test_table_rotation_forbidden_pair(self) -> None:
        # Forbid students 0 and 1 from sitting together
        forbidden_pairs = [{0, 1}]
        solver = TableRotationSolver(
            n_students=12,
            n_tables=3,
            needed_rotations=3,
            max_attempts=2000,
            forbidden_pairs=forbidden_pairs,
        )
        rotations = solver.solve()
        for rotation in rotations:
            for table in rotation:
                assert not ({0, 1}.issubset(set(table))), (
                    f"Forbidden pair {{0, 1}} found together at table: "
                    f"{table} in rotation: {rotation}"
                )
