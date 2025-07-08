from typing import List, Tuple

import streamlit as st

from permutations.core.score_rotation import score_rotation

st.title("Table Rotation Generator")

st.header("Step 1: Enter Students")

with st.form("students_form"):
    boys = st.text_area("Boys (one per line)", "Tom\nAlex\nBen\nDavid")
    girls = st.text_area("Girls (one per line)", "Emma\nLily\nSophia\nOlivia")
    submitted_students = st.form_submit_button("Validate Students")

if "boys" not in st.session_state:
    st.session_state.boys = []
if "girls" not in st.session_state:
    st.session_state.girls = []
if submitted_students:
    st.session_state.boys = [b.strip() for b in boys.splitlines() if b.strip()]
    st.session_state.girls = [g.strip() for g in girls.splitlines() if g.strip()]

if st.session_state.boys and st.session_state.girls:
    st.success(f"{len(st.session_state.boys)} boys and {len(st.session_state.girls)} girls loaded.")
    st.header("Step 2: Add Forbidden Pairs (optional)")
    forbidden_pairs: List[Tuple[str, str]] = []
    all_students = st.session_state.boys + st.session_state.girls
    if "forbidden_pairs" not in st.session_state:
        st.session_state.forbidden_pairs = []
    with st.form("forbidden_form"):
        col1, col2 = st.columns(2)
        with col1:
            forbidden_a = st.selectbox("Student 1", all_students, key="forbidden_a")
        with col2:
            forbidden_b = st.selectbox("Student 2", all_students, key="forbidden_b")
        add_pair = st.form_submit_button("Add Forbidden Pair")
        if add_pair and forbidden_a != forbidden_b:
            pair = tuple(sorted((forbidden_a, forbidden_b)))
            if pair not in st.session_state.forbidden_pairs:
                st.session_state.forbidden_pairs.append(pair)
    if st.session_state.forbidden_pairs:
        st.write("Forbidden pairs:")
        for a, b in st.session_state.forbidden_pairs:
            st.write(f"- {a} / {b}")
    st.header("Step 3: Generate Rotations")
    n_tables = st.number_input(
        "Number of tables", min_value=1, max_value=len(all_students), value=2
    )
    n_iterations = st.number_input("Number of rotations", min_value=1, max_value=20, value=5)
    if st.button("Generate Rotations"):
        rotations = score_rotation(
            boys=st.session_state.boys,
            girls=st.session_state.girls,
            n_tables=n_tables,
            n_iterations=n_iterations,
            forbidden_pairs=st.session_state.forbidden_pairs,
        )
        st.success(f"Generated {len(rotations)} rotations.")
        for i, tables in enumerate(rotations):
            st.subheader(f"Rotation {i+1}")
            for t, table in enumerate(tables):
                st.write(f"Table {t+1}: {', '.join(table)}")
