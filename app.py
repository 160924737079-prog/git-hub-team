import streamlit as st
from datetime import date

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GitHub Team Task Manager",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# ============================================================
# CONSTANTS
# ============================================================

STATUSES = [
    "Todo",
    "In Progress",
    "Review",
    "Done"
]

PRIORITIES = [
    "High",
    "Medium",
    "Low"
]


# ============================================================
# THEME COLORS
# ============================================================

if st.session_state.theme == "Dark":

    BG_COLOR = "#0f172a"
    SIDEBAR_BG = "#020617"
    CARD_BG = "#1e293b"
    CARD_BORDER = "#334155"
    TEXT_COLOR = "#f8fafc"
    SECONDARY_TEXT = "#94a3b8"
    BORDER_COLOR = "#334155"
    SHADOW = "rgba(0,0,0,0.35)"
    INPUT_BG = "#1e293b"

else:

    BG_COLOR = "#f8fafc"
    SIDEBAR_BG = "#ffffff"
    CARD_BG = "#ffffff"
    CARD_BORDER = "#e2e8f0"
    TEXT_COLOR = "#0f172a"
    SECONDARY_TEXT = "#475569"
    BORDER_COLOR = "#e2e8f0"
    SHADOW = "rgba(15,23,42,0.10)"
    INPUT_BG = "#ffffff"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {{
        background: {BG_COLOR};
        color: {TEXT_COLOR};
    }}

    .main {{
        padding-top: 1rem;
    }}

    body {{
        color: {TEXT_COLOR};
    }}


    /* ========================================================
       HEADER
       ======================================================== */

    .header {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {TEXT_COLOR};
        margin-bottom: 5px;
        animation: fadeDown 0.7s ease;
    }}

    .subtitle {{
        color: {SECONDARY_TEXT};
        font-size: 1rem;
        margin-bottom: 25px;
        animation: fadeDown 0.9s ease;
    }}


    /* ========================================================
       ANIMATIONS
       ======================================================== */

    @keyframes fadeDown {{
        from {{
            opacity: 0;
            transform: translateY(-15px);
        }}

        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes cardAppear {{
        from {{
            opacity: 0;
            transform: translateY(15px);
        }}

        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes fadeIn {{
        from {{
            opacity: 0;
        }}

        to {{
            opacity: 1;
        }}
    }}


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {{
        background: {SIDEBAR_BG};
        border-right: 1px solid {BORDER_COLOR};
    }}


    /* ========================================================
       TASK CARD
       ======================================================== */

    .task-card {{
        padding: 18px;
        border-radius: 14px;
        border: 1px solid {CARD_BORDER};
        background: {CARD_BG};
        margin-bottom: 12px;
        box-shadow: 0 8px 25px {SHADOW};
        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            border-color 0.25s ease;
        animation: cardAppear 0.5s ease;
        color: {TEXT_COLOR};
    }}

    .task-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 14px 30px {SHADOW};
    }}

    .task-title {{
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 12px;
        color: {TEXT_COLOR};
    }}

    .task-info {{
        color: {SECONDARY_TEXT};
        line-height: 1.8;
        font-size: 0.92rem;
    }}


    /* ========================================================
       METRICS
       ======================================================== */

    div[data-testid="stMetric"] {{
        background: {CARD_BG};
        border: 1px solid {CARD_BORDER};
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 8px 20px {SHADOW};
        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;
        animation: cardAppear 0.6s ease;
    }}

    div[data-testid="stMetric"]:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 28px {SHADOW};
    }}


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {{
        border-radius: 10px;
        font-weight: 600;
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 7px 18px {SHADOW};
    }}

    .stButton > button:active {{
        transform: scale(0.97);
    }}


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="input"] {{
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }}

    div[data-baseweb="input"]:focus-within {{
        transform: scale(1.01);
        box-shadow:
            0 0 0 2px rgba(59,130,246,0.25);
    }}

    div[data-baseweb="select"] {{
        transition: transform 0.2s ease;
    }}

    div[data-baseweb="select"]:focus-within {{
        transform: scale(1.01);
    }}


    /* ========================================================
       DATAFRAME
       ======================================================== */

    div[data-testid="stDataFrame"] {{
        border-radius: 12px;
        overflow: hidden;
        animation: fadeIn 0.6s ease;
    }}


    /* ========================================================
       ALERTS
       ======================================================== */

    div[data-testid="stAlert"] {{
        border-radius: 10px;
        animation: fadeIn 0.4s ease;
    }}


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {{
        border-color: {BORDER_COLOR};
    }}


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1,
    h2,
    h3 {{
        color: {TEXT_COLOR};
    }}


    /* ========================================================
       SCROLLBAR
       ======================================================== */

    ::-webkit-scrollbar {{
        width: 8px;
    }}

    ::-webkit-scrollbar-track {{
        background: {BG_COLOR};
    }}

    ::-webkit-scrollbar-thumb {{
        background: #64748b;
        border-radius: 10px;
    }}


    /* ========================================================
       FOOTER
       ======================================================== */

    footer {{
        color: {SECONDARY_TEXT};
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def generate_task_id():
    """Generate a unique task ID."""

    if not st.session_state.tasks:
        return 1

    return max(
        task["id"]
        for task in st.session_state.tasks
    ) + 1


def add_task(
    title,
    member,
    status,
    priority,
    deadline
):
    """Add a new task."""

    new_task = {
        "id": generate_task_id(),
        "title": title.strip(),
        "member": member.strip(),
        "status": status,
        "priority": priority,
        "deadline": str(deadline)
    }

    st.session_state.tasks.append(new_task)


def get_task_counts():
    """Calculate dashboard statistics."""

    total = len(st.session_state.tasks)

    todo = sum(
        task["status"] == "Todo"
        for task in st.session_state.tasks
    )

    progress = sum(
        task["status"] == "In Progress"
        for task in st.session_state.tasks
    )

    review = sum(
        task["status"] == "Review"
        for task in st.session_state.tasks
    )

    done = sum(
        task["status"] == "Done"
        for task in st.session_state.tasks
    )

    return total, todo, progress, review, done


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="header">📋 GitHub Team Task Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create and manage your team tasks, priorities '
    'and deadlines from one place.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # ========================================================
    # APPEARANCE
    # ========================================================

    st.header("🎨 Appearance")

    selected_theme = st.radio(
        "Select Theme",
        ["Dark", "Light"],
        index=(
            0
            if st.session_state.theme == "Dark"
            else 1
        ),
        horizontal=True,
        key="theme_selector"
    )

    if selected_theme != st.session_state.theme:

        st.session_state.theme = selected_theme

        st.rerun()

    st.divider()


    # ========================================================
    # ADD TASK
    # ========================================================

    st.header("➕ Add New Task")

    task_name = st.text_input(
        "Task Title",
        placeholder="Enter task title",
        key="add_task_name"
    )

    member_name = st.text_input(
        "Member Name",
        placeholder="Enter member name",
        key="add_member_name"
    )

    task_status = st.selectbox(
        "Status",
        STATUSES,
        key="add_task_status"
    )

    task_priority = st.selectbox(
        "Priority",
        PRIORITIES,
        key="add_task_priority"
    )

    task_deadline = st.date_input(
        "Deadline",
        min_value=date.today(),
        key="add_task_deadline"
    )

    add_button = st.button(
        "➕ Add Task",
        use_container_width=True,
        type="primary",
        key="add_task_button"
    )


    # ========================================================
    # VALIDATE AND ADD TASK
    # ========================================================

    if add_button:

        if not task_name.strip():

            st.error(
                "Please enter a task title."
            )

        elif not member_name.strip():

            st.error(
                "Please enter a member name."
            )

        else:

            add_task(
                task_name,
                member_name,
                task_status,
                task_priority,
                task_deadline
            )

            st.success(
                f"Task '{task_name}' added successfully."
            )

            st.rerun()


# ============================================================
# DASHBOARD METRICS
# ============================================================

(
    total,
    todo,
    progress,
    review,
    done
) = get_task_counts()


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "Total Tasks",
        total
    )


with col2:
    st.metric(
        "Todo",
        todo
    )


with col3:
    st.metric(
        "In Progress",
        progress
    )


with col4:
    st.metric(
        "Review",
        review
    )


with col5:
    st.metric(
        "Completed",
        done
    )


st.divider()


# ============================================================
# FILTERS
# ============================================================

st.subheader("🔎 Task Management")

filter_col1, filter_col2, filter_col3 = st.columns(3)


with filter_col1:

    status_filter = st.selectbox(
        "Filter by Status",
        ["All"] + STATUSES,
        key="filter_status"
    )


with filter_col2:

    priority_filter = st.selectbox(
        "Filter by Priority",
        ["All"] + PRIORITIES,
        key="filter_priority"
    )


with filter_col3:

    search_text = st.text_input(
        "Search Tasks",
        placeholder="Search task or member...",
        key="search_tasks"
    )


# ============================================================
# FILTER TASKS
# ============================================================

filtered_tasks = list(
    st.session_state.tasks
)


if status_filter != "All":

    filtered_tasks = [
        task
        for task in filtered_tasks
        if task["status"] == status_filter
    ]


if priority_filter != "All":

    filtered_tasks = [
        task
        for task in filtered_tasks
        if task["priority"] == priority_filter
    ]


if search_text.strip():

    search = search_text.lower()

    filtered_tasks = [
        task
        for task in filtered_tasks
        if (
            search in task["title"].lower()
            or
            search in task["member"].lower()
        )
    ]


# ============================================================
# TASK TABLE
# ============================================================

st.subheader("📋 Team Tasks")


if not filtered_tasks:

    st.info(
        "No tasks available. "
        "Add your first task using the sidebar."
    )

else:

    table_data = [

        {
            "ID": task["id"],
            "Task": task["title"],
            "Member": task["member"],
            "Status": task["status"],
            "Priority": task["priority"],
            "Deadline": task["deadline"]
        }

        for task in filtered_tasks
    ]

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# KANBAN BOARD
# ============================================================

st.divider()

st.subheader("🗂️ Kanban Board")

columns = st.columns(4)


for index, status in enumerate(STATUSES):

    with columns[index]:

        st.markdown(
            f"### {status}"
        )

        status_tasks = [
            task
            for task in st.session_state.tasks
            if task["status"] == status
        ]

        if not status_tasks:

            st.caption("No tasks")

        for task in status_tasks:

            # ------------------------------------------------
            # TASK CARD
            # No <strong>, <br> or other HTML in task content
            # ------------------------------------------------

            st.markdown(
                '<div class="task-card">',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="task-title">'
                f'#{task["id"]} — {task["title"]}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="task-info">
                👤 Member: {task["member"]}<br>
                🚦 Priority: {task["priority"]}<br>
                📅 Deadline: {task["deadline"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# ============================================================
# MANAGE TASKS
# ============================================================

st.divider()

st.subheader("⚙️ Manage Tasks")


if not st.session_state.tasks:

    st.info(
        "There are no tasks to manage."
    )

else:

    task_options = {
        f"#{task['id']} - {task['title']}":
        task["id"]
        for task in st.session_state.tasks
    }

    selected_task = st.selectbox(
        "Select Task",
        list(task_options.keys()),
        key="selected_task"
    )

    selected_id = task_options[selected_task]

    selected_data = next(
        task
        for task in st.session_state.tasks
        if task["id"] == selected_id
    )

    manage_col1, manage_col2 = st.columns(2)


    # ========================================================
    # UPDATE STATUS
    # ========================================================

    with manage_col1:

        new_status = st.selectbox(
            "Change Status",
            STATUSES,
            index=STATUSES.index(
                selected_data["status"]
            ),
            key=f"change_status_{selected_id}"
        )

        if st.button(
            "💾 Update Status",
            use_container_width=True,
            key=f"update_status_{selected_id}"
        ):

            selected_data["status"] = new_status

            st.success(
                "Task status updated successfully."
            )

            st.rerun()


    # ========================================================
    # DELETE TASK
    # ========================================================

    with manage_col2:

        if st.button(
            "🗑️ Delete Task",
            use_container_width=True,
            key=f"delete_task_{selected_id}"
        ):

            st.session_state.tasks = [
                task
                for task in st.session_state.tasks
                if task["id"] != selected_id
            ]

            st.success(
                "Task deleted successfully."
            )

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "GitHub Team Task Manager • "
    "Built with Python & Streamlit"
)
