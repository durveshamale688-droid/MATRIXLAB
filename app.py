
import streamlit as st
import numpy as np
import pandas as pd

# =====================================================
# 1. APPLICATION CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="MATRIXLAB | Matrix Calculator",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# 2. PREMIUM BLACK AND WHITE DESIGN
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #080808;
    color: #FFFFFF;
}

.block-container {
    max-width: 1250px;
    padding: 2rem 1.5rem;
}

header[data-testid="stHeader"] {
    background: #080808;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    background: linear-gradient(145deg, #191919, #080808);
    border: 1px solid #383838;
    border-radius: 24px;
    padding: 45px 20px;
    text-align: center;
    margin-bottom: 30px;
}

.logo {
    width: 75px;
    height: 75px;
    border: 2px solid #FFFFFF;
    border-radius: 20px;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 43px;
    font-weight: 800;
    color: #FFFFFF;
}

.hero h1 {
    font-size: clamp(30px, 5vw, 48px);
    font-weight: 800;
    letter-spacing: 5px;
    color: #FFFFFF;
    margin-top: 20px;
}

.hero p {
    color: #A0A0A0;
    letter-spacing: 2px;
    font-size: 12px;
}

.section-title {
    font-size: 23px;
    font-weight: 700;
    color: #FFFFFF;
    margin: 30px 0 15px 0;
}

.panel {
    background: #151515;
    border: 1px solid #383838;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.panel h3 {
    color: #FFFFFF;
    font-size: 19px;
}

.muted {
    color: #A0A0A0;
    font-size: 13px;
}

.stButton > button {
    width: 100%;
    min-height: 48px;
    background: #FFFFFF;
    color: #080808;
    border: 1px solid #FFFFFF;
    border-radius: 10px;
    font-weight: 700;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #D6D6D6;
    color: #000000;
    border-color: #FFFFFF;
}

.stButton > button:focus {
    border: 2px solid #FFFFFF;
}

div[data-testid="stNumberInput"] input {
    background: #202020;
    color: #FFFFFF;
    border: 1px solid #505050;
    border-radius: 8px;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: #202020;
}

div[data-testid="stRadio"] label {
    color: #FFFFFF;
}

.result-panel {
    background: #151515;
    border: 1px solid #555555;
    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #777777;
    border-top: 1px solid #292929;
    margin-top: 50px;
    padding: 25px 5px;
    font-size: 12px;
}

[data-testid="stDataFrame"] {
    border: 1px solid #444444;
    border-radius: 10px;
}

@media(max-width: 640px) {
    .block-container {
        padding: 1rem 0.7rem;
    }

    .hero {
        padding: 30px 12px;
    }

    .panel {
        padding: 14px;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. SESSION STATE
# =====================================================

defaults = {
    "launched": False,
    "A_values": [],
    "B_values": [],
    "active_matrix": "A",
    "dimensions": None,
    "input_nonce": 0,
    "result": None,
    "error": None,
    "operation_done": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# 4. LOGO AND WELCOME SCREEN
# =====================================================

if not st.session_state.launched:

    st.markdown("""
    <div class="hero">
        <div class="logo">M</div>
        <h1>MATRIXLAB</h1>
        <p>ADVANCED MATRIX COMPUTATION SYSTEM</p>
        <br>
        <p>POWERED BY PYTHON AND NUMPY</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<h3 style='text-align:center;color:white;'>"
        "Welcome to MatrixLab</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#999999;'>"
        "A smarter way to calculate, explore and understand matrices."
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("")

    if st.button("LAUNCH MATRIXLAB  →", use_container_width=True):
        st.session_state.launched = True
        st.rerun()

    st.markdown("""
    <div class="footer">
        MATRIXLAB © 2026
        <br><br>
        OPEN SOURCE MATRIX CALCULATOR
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# =====================================================
# 5. MAIN APPLICATION HEADER
# =====================================================

st.markdown("""
<div class="hero">
    <div class="logo">M</div>
    <h1>MATRIXLAB</h1>
    <p>ADVANCED MATRIX COMPUTATION SYSTEM</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">01 / MATRIX CONFIGURATION</div>',
    unsafe_allow_html=True
)


# =====================================================
# 6. MATRIX DIMENSION SELECTION
# =====================================================

col1, col2 = st.columns(2)

with col1:
    st.markdown("### MATRIX A")

    rows_a = st.selectbox(
        "Number of rows",
        list(range(1, 11)),
        index=1,
        key="rows_a"
    )

    cols_a = st.selectbox(
        "Number of columns",
        list(range(1, 11)),
        index=1,
        key="cols_a"
    )

with col2:
    st.markdown("### MATRIX B")

    rows_b = st.selectbox(
        "Number of rows",
        list(range(1, 11)),
        index=1,
        key="rows_b"
    )

    cols_b = st.selectbox(
        "Number of columns",
        list(range(1, 11)),
        index=1,
        key="cols_b"
    )


current_dimensions = (
    rows_a, cols_a, rows_b, cols_b
)

if st.session_state.dimensions != current_dimensions:

    st.session_state.dimensions = current_dimensions

    st.session_state.A_values = [None] * (rows_a * cols_a)
    st.session_state.B_values = [None] * (rows_b * cols_b)

    st.session_state.active_matrix = "A"
    st.session_state.input_nonce += 1

    st.session_state.result = None
    st.session_state.error = None

    st.rerun()


# =====================================================
# 7. MATRIX PREVIEW FUNCTION
# =====================================================

def display_matrix_preview(name, values, rows, cols):

    matrix_data = []

    for i in range(rows):

        row = []

        for j in range(cols):

            index = i * cols + j
            value = values[index]

            if value is None:
                row.append("—")
            else:
                row.append(value)

        matrix_data.append(row)

    st.markdown(f"**{name} Preview**")

    df = pd.DataFrame(
        matrix_data,
        columns=[f"C{i+1}" for i in range(cols)]
    )

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )


# =====================================================
# 8. KEYBOARD MATRIX INPUT
# =====================================================

st.markdown(
    '<div class="section-title">02 / MATRIX INPUT</div>',
    unsafe_allow_html=True
)

active = st.session_state.active_matrix

if active is not None:

    if active == "A":
        current_values = st.session_state.A_values
        rows = rows_a
        cols = cols_a
        matrix_name = "MATRIX A"

    else:
        current_values = st.session_state.B_values
        rows = rows_b
        cols = cols_b
        matrix_name = "MATRIX B"

    completed = sum(
        value is not None for value in current_values
    )

    total = rows * cols

    st.markdown(f"""
    <div class="panel">
        <h3>{matrix_name}</h3>
        <p class="muted">
            Enter each element and press ENTER to save
            and proceed to the next element.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(completed / total)

    st.write(f"Elements entered: **{completed} / {total}**")

    if completed < total:

        index = completed

        row_number = index // cols + 1
        col_number = index % cols + 1

        with st.form(
            key=f"entry_form_{active}_{index}_{st.session_state.input_nonce}"
        ):

            value = st.number_input(
                f"Enter {matrix_name} element [{row_number}, {col_number}]",
                value=0.0,
                step=1.0,
                format="%.4f",
                key=f"entry_value_{active}_{index}_{st.session_state.input_nonce}"
            )

            submitted = st.form_submit_button(
                "ENTER  →  NEXT ELEMENT",
                use_container_width=True
            )

            if submitted:

                current_values[index] = float(value)

                if active == "A":
                    st.session_state.A_values = current_values

                    if completed + 1 == total:
                        st.session_state.active_matrix = "B"

                else:
                    st.session_state.B_values = current_values

                    if completed + 1 == total:
                        st.session_state.active_matrix = None

                st.rerun()

    else:

        st.success(f"{matrix_name} completed successfully!")

else:

    st.success("Both matrices have been entered successfully!")


# =====================================================
# 9. DISPLAY MATRIX PREVIEWS
# =====================================================

st.markdown(
    '<div class="section-title">03 / MATRIX PREVIEW</div>',
    unsafe_allow_html=True
)

preview1, preview2 = st.columns(2)

with preview1:

    display_matrix_preview(
        "MATRIX A",
        st.session_state.A_values,
        rows_a,
        cols_a
    )

with preview2:

    display_matrix_preview(
        "MATRIX B",
        st.session_state.B_values,
        rows_b,
        cols_b
    )


# =====================================================
# 10. CONVERT INPUTS INTO NUMPY ARRAYS
# =====================================================

def get_numpy_matrices():

    if (
        any(v is None for v in st.session_state.A_values)
        or any(v is None for v in st.session_state.B_values)
    ):
        raise ValueError("Please complete both matrices first.")

    A = np.array(
        st.session_state.A_values,
        dtype=float
    ).reshape(rows_a, cols_a)

    B = np.array(
        st.session_state.B_values,
        dtype=float
    ).reshape(rows_b, cols_b)

    return A, B


# =====================================================
# 11. MATRIX CALCULATION BACKEND
# =====================================================

def calculate(A, B, operation, target):

    if operation == "Addition":

        if A.shape != B.shape:
            raise ValueError(
                "Addition requires both matrices to have "
                "the same number of rows and columns."
            )

        return np.add(A, B)

    elif operation == "Multiplication":

        if A.shape[1] != B.shape[0]:
            raise ValueError(
                "Multiplication is not possible. "
                "Columns of Matrix A must equal "
                "rows of Matrix B."
            )

        return np.matmul(A, B)

    elif operation == "Determinant":

        if target.shape[0] != target.shape[1]:
            raise ValueError(
                "Determinant can only be calculated "
                "for a square matrix."
            )

        return float(np.linalg.det(target))

    elif operation == "Inverse":

        if target.shape[0] != target.shape[1]:
            raise ValueError(
                "Inverse can only be calculated "
                "for a square matrix."
            )

        if np.linalg.matrix_rank(target) < target.shape[0]:
            raise ValueError(
                "This matrix is singular. "
                "Its inverse does not exist."
            )

        return np.linalg.inv(target)


# =====================================================
# 12. OPERATION SELECTION
# =====================================================

st.markdown(
    '<div class="section-title">04 / MATRIX OPERATIONS</div>',
    unsafe_allow_html=True
)

operation = st.selectbox(
    "Select calculation",
    [
        "Addition",
        "Multiplication",
        "Determinant",
        "Inverse"
    ],
    key="operation"
)

target = None

if operation in ["Determinant", "Inverse"]:

    target_choice = st.radio(
        "Choose matrix",
        ["Matrix A", "Matrix B"],
        horizontal=True
    )

else:
    target_choice = None


# =====================================================
# 13. CALCULATION AND RESET BUTTONS
# =====================================================

ready = (
    all(v is not None for v in st.session_state.A_values)
    and all(v is not None for v in st.session_state.B_values)
)

button1, button2 = st.columns(2)

with button1:

    calculate_button = st.button(
        "CALCULATE RESULT",
        disabled=not ready,
        use_container_width=True
    )

with button2:

    reset_button = st.button(
        "RESET ALL INPUTS",
        use_container_width=True
    )


# =====================================================
# 14. RESET FUNCTIONALITY
# =====================================================

if reset_button:

    st.session_state.A_values = [None] * (rows_a * cols_a)
    st.session_state.B_values = [None] * (rows_b * cols_b)

    st.session_state.active_matrix = "A"
    st.session_state.input_nonce += 1

    st.session_state.result = None
    st.session_state.error = None

    st.rerun()


# =====================================================
# 15. PERFORM CALCULATIONS
# =====================================================

if calculate_button:

    try:

        A, B = get_numpy_matrices()

        if operation in ["Determinant", "Inverse"]:

            target = A if target_choice == "Matrix A" else B

        result = calculate(
            A,
            B,
            operation,
            target
        )

        st.session_state.result = result
        st.session_state.error = None

    except (ValueError, np.linalg.LinAlgError) as e:

        st.session_state.result = None
        st.session_state.error = str(e)

    except Exception as e:

        st.session_state.result = None
        st.session_state.error = f"Calculation failed: {e}"


# =====================================================
# 16. RESULT DISPLAY
# =====================================================

st.markdown(
    '<div class="section-title">05 / CALCULATION RESULT</div>',
    unsafe_allow_html=True
)

if st.session_state.error:

    st.error(st.session_state.error)

elif st.session_state.result is not None:

    result = st.session_state.result

    st.markdown(
        '<div class="result-panel">',
        unsafe_allow_html=True
    )

    st.markdown("### RESULT")

    if isinstance(result, np.ndarray):

        result_df = pd.DataFrame(
            np.round(result, 4)
        )

        st.dataframe(
            result_df,
            hide_index=True,
            use_container_width=True
        )

    else:

        st.metric(
            "Calculated Value",
            f"{result:.6f}"
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

else:

    st.info(
        "Your calculation result will appear here. "
        "Complete both matrices and select an operation."
    )


# =====================================================
# 17. FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    <h3 style="color:white;letter-spacing:4px;">
        MATRIXLAB
    </h3>
    ADVANCED MATRIX COMPUTATION SYSTEM
    <br><br>
    BUILT WITH PYTHON • STREAMLIT • NUMPY
    <br><br>
    OPEN SOURCE SOFTWARE © 2026
</div>
""", unsafe_allow_html=True)
