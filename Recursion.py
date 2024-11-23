def schedule_tasks(task_hierarchy):
    scheduled_tasks = []

    def traverse_and_schedule(task):
        # Add the task to the scheduled list
        scheduled_tasks.append({
            "id": task["id"],
            "name": task["name"],
            "priority": task.get("priority", 0)
        })

        # Recursively schedule subtasks if any
        for subtask in sorted(task.get("subtasks", []), key=lambda x: x.get("priority", 0), reverse=True):
            traverse_and_schedule(subtask)

    traverse_and_schedule(task_hierarchy)
    return scheduled_tasks

# Example usage:
task_hierarchy = {
    "id": 1,
    "name": "Main Project",
    "priority": 3,
    "subtasks": [
        {
            "id": 2,
            "name": "Task 1",
            "priority": 2,
            "subtasks": [
                {
                    "id": 4,
                    "name": "Subtask 1.1",
                    "priority": 1
                },
                {
                    "id": 5,
                    "name": "Subtask 1.2",
                    "priority": 2
                }
            ]
        },
        {
            "id": 3,
            "name": "Task 2",
            "priority": 1,
            "subtasks": []
        }
    ]
}

scheduled = schedule_tasks(task_hierarchy)
print("Scheduled Tasks:")
for task in scheduled:
    print(task)
