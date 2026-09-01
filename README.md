# 📋 GitHub Team Task Manager

A modern and interactive **Team Task Management Dashboard** built with **Python and Streamlit**.

The GitHub Team Task Manager helps teams create, organize, track, filter, and manage project tasks from a single dashboard. It provides a clean interface with task statistics, status tracking, priority management, search functionality, and a Kanban-style board.

---

## 🚀 Features

### 📊 Dashboard

* Total task count
* Todo task count
* In Progress task count
* Review task count
* Completed task count
* Real-time dashboard statistics

### ➕ Task Creation

Create new tasks with:

* Task title
* Team member name
* Task status
* Task priority
* Deadline

The application validates required fields before creating a task.

### 🚦 Task Status

Tasks can have one of four statuses:

* 📝 Todo
* 🔄 In Progress
* 🔍 Review
* ✅ Done

### ⭐ Task Priority

Tasks can be categorized using:

* 🔴 High
* 🟡 Medium
* 🟢 Low

### 🔎 Task Filtering

Filter tasks by:

* Status
* Priority
* Task title
* Team member

The search system allows users to quickly find specific tasks.

### 🗂️ Kanban Board

Tasks are displayed in a Kanban-style layout with four columns:

```text
Todo → In Progress → Review → Done
```

Each task card displays:

* Task ID
* Task title
* Assigned member
* Priority
* Deadline

### ⚙️ Task Management

Users can:

* Update task status
* Delete tasks
* Select individual tasks for management

### 🎨 Theme Support

The application supports two themes:

* 🌙 Dark Mode
* ☀️ Light Mode

The theme can be changed from the sidebar.

### ✨ Modern UI

The application includes:

* Responsive wide layout
* Custom CSS styling
* Animated task cards
* Hover effects
* Interactive buttons
* Styled metrics
* Custom scrollbar
* Glass-style dashboard cards

---

## 🛠️ Technologies Used

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Application development   |
| Streamlit            | Web application framework |
| HTML/CSS             | Custom UI styling         |
| Python Session State | Temporary task management |
| Datetime             | Deadline management       |

---

## 📁 Project Structure

```text
github-team-task-manager/
│
├── app.py
├── requirements.txt
└── README.md
```

> Rename your Python file to `app.py` if it currently has a different filename.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR-REPOSITORY
```

---

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, install Streamlit:

```bash
pip install streamlit
```

Then create the requirements file:

```bash
pip freeze > requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, Streamlit runs locally at:

```text
http://localhost:8501
```

---

## 🖥️ How to Use

### Step 1 — Open the Application

Run:

```bash
streamlit run app.py
```

### Step 2 — Select a Theme

Use the sidebar to choose:

* Dark
* Light

### Step 3 — Add a Task

Enter:

1. Task Title
2. Member Name
3. Status
4. Priority
5. Deadline

Click:

```text
➕ Add Task
```

### Step 4 — Monitor Tasks

The dashboard displays task statistics at the top of the page.

### Step 5 — Filter Tasks

Use the task-management filters to find tasks by:

* Status
* Priority
* Search keyword

### Step 6 — View the Kanban Board

Review tasks according to their current status.

### Step 7 — Manage Tasks

Select a task from the **Manage Tasks** section.

You can:

* Change its status
* Delete the task

---

## 📊 Dashboard Workflow

```text
                GitHub Team Task Manager
                         │
                         ▼
                  Create New Task
                         │
                         ▼
              ┌─────────────────────┐
              │ Task Information     │
              │                     │
              │ • Title             │
              │ • Member            │
              │ • Status            │
              │ • Priority          │
              │ • Deadline          │
              └──────────┬──────────┘
                         │
                         ▼
                  Task Dashboard
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Filters     Task Table   Kanban
             │           │           │
             └───────────┼───────────┘
                         ▼
                  Manage Tasks
                    /       \
                   ▼         ▼
              Update       Delete
               Status        Task
```

---

## 💾 Data Storage

The current application uses **Streamlit Session State** to store tasks during the active application session.

Tasks are maintained in:

```python
st.session_state.tasks
```

Therefore, tasks are temporary and may be lost when the application session is restarted.

For permanent storage, the project can later be extended with:

* SQLite
* MySQL
* PostgreSQL
* MongoDB
* Firebase

---

## 🔐 Validation

The application checks that:

* Task title is not empty
* Member name is not empty

If required information is missing, an error message is displayed.

---

## 🎨 User Interface

The application provides a modern dashboard experience with:

* Dark/Light themes
* Custom colors
* Animated cards
* Interactive buttons
* Responsive columns
* Styled task cards
* Dashboard metrics

---

## 🌐 Deploy on Streamlit Community Cloud

You can deploy the project online using Streamlit Community Cloud.

### Step 1

Push your project to GitHub.

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Step 2

Open Streamlit Community Cloud.

Create a new application and select your GitHub repository.

### Step 3

Set the main application file:

```text
app.py
```

### Step 4

Deploy the application.

After deployment, Streamlit will provide a public URL for your project.

---

## 📦 Requirements

A basic `requirements.txt` file can contain:

```text
streamlit
```

If you want to use a specific Streamlit version:

```text
streamlit==1.39.0
```

---

## 🔄 Future Enhancements

Possible improvements include:

* 🔐 User authentication
* 👥 Team member accounts
* 💾 Database integration
* 📧 Email notifications
* ⏰ Deadline reminders
* 📈 Advanced analytics
* 📊 Progress charts
* 📤 Export tasks to CSV/Excel
* 🔗 GitHub repository integration
* 🔄 Drag-and-drop Kanban board
* ☁️ Cloud database support
* 📝 Task descriptions and comments

---

## 🎯 Project Objective

The main objective of the GitHub Team Task Manager is to provide teams with a simple and user-friendly platform for organizing project tasks, monitoring progress, managing deadlines, and improving team productivity.

---

## 👨‍💻 Author

**Syed Sadath Ullah Hussaini**

---

## 📜 License

This project is created for **educational and project development purposes**.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### Built With  Using Python & Streamlit

**GitHub Team Task Manager — Organize. Track. Complete.**
