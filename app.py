import streamlit as st

from routes import create_task, delete_task, get_tasks, update_task

st.title("Task Manager")

# Add Task button on top of the page
if st.button("Add Task"):
    st.subheader("Add a New Task")
    title = st.text_input("Title")
    description = st.text_area("Description")
    completed = st.checkbox("Completed")
    if st.button("Submit Task"):
        if create_task(title, description, completed):
            st.success("Task added successfully!")
        else:
            st.error("Failed to add task.")

st.subheader("Task List")
tasks = get_tasks()
for task in tasks:
    st.write(f"**{task['title']}**")
    st.write(f"Description: {task['description']}")
    st.write(f"Completed: {'Yes' if task['completed'] else 'No'}")
    if st.button(f"Edit {task['id']}"):
        with st.dialog(f"Edit Task {task['id']}"):
            title = st.text_input("New Title", value=task["title"])
            description = st.text_area("New Description", value=task["description"])
            completed = st.checkbox("Completed", value=task["completed"])
            if st.button("Update Task"):
                if update_task(task["id"], title, description, completed):
                    st.success("Task updated successfully!")
                else:
                    st.error("Failed to update task.")
    if st.button(f"Delete {task['id']}"):
        with st.dialog(f"Delete Task {task['id']}"):
            st.write(f"Are you sure you want to delete the task: {task['title']}?")
            if st.button("Confirm Delete"):
                if delete_task(task["id"]):
                    st.success("Task deleted successfully!")
                else:
                    st.error("Failed to delete task.")
    st.write("---")
