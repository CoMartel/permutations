import itertools

from permutations.core.score_rotation import score_rotation


def test_score_rotation_all_pairs_meet() -> None:
    boys = [f"B{i}" for i in range(2)]
    girls = [f"G{i}" for i in range(2)]
    n_tables = 2
    n_iterations = 3
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


def test_score_rotation_forbidden_pairs() -> None:
    boys = ["Tom", "Alex", "Ben", "David"]
    girls = ["Emma", "Lily", "Sophia", "Olivia"]
    n_tables = 2
    n_iterations = 5
    forbidden_pairs = [("Tom", "Emma"), ("Ben", "Lily")]
    rotations = score_rotation(
        boys, girls, n_tables=n_tables, n_iterations=n_iterations, forbidden_pairs=forbidden_pairs
    )
    forbidden_set = set(frozenset(pair) for pair in forbidden_pairs)
    for rotation in rotations:
        for table in rotation:
            table_set = set(table)
            for pair in forbidden_set:
                assert not pair.issubset(
                    table_set
                ), f"Forbidden pair {set(pair)} found together in table: {table}"


def test_score_rotation_breaks() -> None:
    boys = ["Tom", "Alex", "Ben", "David"]
    girls = ["Emma"]
    n_tables = 2
    n_iterations = 5
    forbidden_pairs = [(boy, "Emma") for boy in boys]
    rotations = score_rotation(
        boys, girls, n_tables=n_tables, n_iterations=n_iterations, forbidden_pairs=forbidden_pairs
    )
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
