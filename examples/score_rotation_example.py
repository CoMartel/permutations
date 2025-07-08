from permutations.core.score_rotation import score_rotation, pretty_print_rotations

if __name__ == "__main__":
    boys = ["Tom", "Alex", "Ben", "David"]
    girls = ["Emma"]
    n_tables = 2
    n_iterations = 4

    rotations = score_rotation(
        boys=boys,
        girls=girls,
        n_tables=n_tables,
        n_iterations=n_iterations,
    )

    pretty_print_rotations(rotations)
