from typing import List
from permutations.core.score_rotation import score_rotation


def pretty_print_rotations(rotations: List[List[List[str]]]) -> None:
    for it, tables in enumerate(rotations):
        print(f"Rotation {it+1}:")
        for t, table in enumerate(tables):
            print(f"  Table {t+1}: {', '.join(table)}")
        print()


if __name__ == "__main__":
    boys = ["Tom", "Alex", "Ben", "David"]
    girls = ["Emma"," Mia", "Sophia", "Olivia"]
    n_tables = 4
    n_iterations = 4

    rotations = score_rotation(
        boys=boys,
        girls=girls,
        n_tables=n_tables,
        n_iterations=n_iterations,
    )

    pretty_print_rotations(rotations)
