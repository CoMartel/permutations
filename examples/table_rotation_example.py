"""Example script demonstrating table rotation functionality."""

from permutations.core.table_rotation import TableRotationSolver


def main() -> None:
    # Example setup: 24 students, 6 tables (4 students per table)
    n_students = 24
    n_tables = 6

    # Some students should never sit together
    forbidden_pairs = [
        {0, 5},  # Student 0 and 5 should never sit together
        {2, 7},  # Student 2 and 7 should never sit together
    ]

    # Create solver
    solver = TableRotationSolver(
        n_students=n_students,
        n_tables=n_tables,
        forbidden_pairs=forbidden_pairs,
        needed_rotations=5  # We want 5 different rotation configurations
    )

    # Find rotations
    try:
        rotations = solver.solve()
        print(f"Found {len(rotations)} valid rotation configurations!")
        # Affichage lisible des rotations
        for i, rotation in enumerate(rotations, 1):
            print(f"\nRotation {i}:")
            for table_idx, table in enumerate(rotation, 1):
                print(f"  Table {table_idx}: {sorted(table)}")
    except RuntimeError as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
