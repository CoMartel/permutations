import itertools

from permutations.core.score_rotation import score_rotation


def test_score_rotation_all_pairs_meet() -> None:
    boys = [f"B{i}" for i in range(4)]
    girls = [f"G{i}" for i in range(1)]
    n_tables = 4
    n_iterations = 4
    rotations = score_rotation(boys, girls, n_tables=n_tables, n_iterations=n_iterations)
    students = boys + girls
    met_pairs = set()
    for rotation in rotations:
        for table in rotation:
            for pair in itertools.combinations(sorted(table), 2):
                met_pairs.add(pair)
    all_pairs = set(itertools.combinations(sorted(students), 2))
    assert met_pairs == all_pairs, f"Some pairs never met: {all_pairs - met_pairs}"


def test_score_rotation_unique_students_per_iteration() -> None:
    boys = [f"B{i}" for i in range(4)]
    girls = [f"G{i}" for i in range(4)]
    n_tables = 4
    n_iterations = 10
    rotations = score_rotation(boys, girls, n_tables=n_tables, n_iterations=n_iterations)
    students = set(boys + girls)
    for rotation in rotations:
        used = set()
        for table in rotation:
            for student in table:
                assert (
                    student not in used
                ), f"Student {student} used more than once in the same iteration: {rotation}"
                used.add(student)
        assert used == students, f"Not all students are used in iteration: {rotation}"
