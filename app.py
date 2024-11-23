import streamlit as st

from routes import create_task, delete_task, get_tasks, update_task

st.title("Task Manager")

menu = ["View Tasks", "Add Task", "Edit Task", "Delete Task"]
choice = "View Tasks"  # Set default view to "View Tasks"

if st.button("View Tasks"):
    choice = "View Tasks"
elif st.button("Add Task"):
    choice = "Add Task"
elif st.button("Edit Task"):
    choice = "Edit Task"
elif st.button("Delete Task"):
    choice = "Delete Task"

if choice == "View Tasks":
    st.subheader("Task List")
    tasks = get_tasks()
    for task in tasks:
        st.write(f"**{task['title']}**")
        st.write(f"Description: {task['description']}")
        st.write(f"Completed: {'Yes' if task['completed'] else 'No'}")
        st.write("---")

elif choice == "Add Task":
    st.subheader("Add a New Task")
    title = st.text_input("Title")
    description = st.text_area("Description")
    completed = st.checkbox("Completed")
    if st.button("Add Task"):
        if create_task(title, description, completed):
            st.success("Task added successfully!")
        else:
            st.error("Failed to add task.")

elif choice == "Edit Task":
    st.subheader("Edit an Existing Task")
    task_id = st.number_input("Task ID", min_value=1, step=1)
    title = st.text_input("New Title")
    description = st.text_area("New Description")
    completed = st.checkbox("Completed")
    if st.button("Update Task"):
        if update_task(task_id, title, description, completed):
            st.success("Task updated successfully!")
        else:
            st.error("Failed to update task.")

elif choice == "Delete Task":
    st.subheader("Delete a Task")
    task_id = st.number_input("Task ID to Delete", min_value=1, step=1)
    if st.button("Delete Task"):
        if delete_task(task_id):
            st.success("Task deleted successfully!")
        else:
            st.error("Failed to delete task.")
