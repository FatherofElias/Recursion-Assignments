# Assignment Task 1 & 2


def schedule_tasks(task_hierarchy):
    scheduled_tasks = []

    def traverse_and_schedule(task):
        # Schedule the current task
        scheduled_tasks.append({
            "id": task["id"],
            "name": task["name"],
            "priority": task.get("priority", 0)
        })

        # Sort subtasks by priority in descending order and recursively schedule them
        for subtask in sorted(task.get("subtasks", []), key=lambda x: x.get("priority", 0), reverse=True):
            traverse_and_schedule(subtask)

    traverse_and_schedule(task_hierarchy)

    # Sort the final scheduled tasks by their priority
    scheduled_tasks = sorted(scheduled_tasks, key=lambda x: x["priority"], reverse=True)
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
            "priority": 1
        }
    ]
}

scheduled = schedule_tasks(task_hierarchy)
print("Scheduled Tasks:")
for task in scheduled:
    print(task)

# Task 3 Tests

# Test Case 1 Simple Hierarchy

task_hierarchy1 = {
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
            "priority": 1
        }
    ]
}

scheduled1 = schedule_tasks(task_hierarchy1)
print("Test Case 1: Basic Nested Hierarchy")
for task in scheduled1:
    print(task)

# Test Case 2 Varying priorty subtasks

task_hierarchy2 = {
    "id": 1,
    "name": "Main Task",
    "priority": 3,
    "subtasks": [
        {
            "id": 2,
            "name": "Subtask A",
            "priority": 1,
            "subtasks": [
                {
                    "id": 4,
                    "name": "Subtask A1",
                    "priority": 2
                },
                {
                    "id": 5,
                    "name": "Subtask A2",
                    "priority": 3
                }
            ]
        },
        {
            "id": 3,
            "name": "Subtask B",
            "priority": 2
        }
    ]
}

scheduled2 = schedule_tasks(task_hierarchy2)
print("\nTest Case 2: Multiple Subtasks with Different Priorities")
for task in scheduled2:
    print(task)


# Test Case 3 No Subtasks

task_hierarchy3 = {
    "id": 1,
    "name": "Single Task",
    "priority": 5
}

scheduled3 = schedule_tasks(task_hierarchy3)
print("\nTest Case 3: No Subtasks")
for task in scheduled3:
    print(task)

# Running all Tests
print("Scheduled Tasks for Test Case 1:")
for task in scheduled1:
    print(task)

print("\nScheduled Tasks for Test Case 2:")
for task in scheduled2:
    print(task)

print("\nScheduled Tasks for Test Case 3:")
for task in scheduled3:
    print(task)


# Task 4 Analysis of Time and Space Complexity

# Time Complexity
# The time complexity of the schedule_tasks function can be broken down into the following components:
# Traversal of Task Hierarchy:
# The function traverse_and_schedule is called recursively for each task and subtask in the hierarchy.
# If there are n tasks in total (including all subtasks), the function will visit each task exactly once.
# Therefore, the traversal itself has a time complexity of 𝑂(𝑛).

# Sorting Subtasks:
# For each task, its subtasks are sorted by priority using the sorted function.
# In the worst case, each task could have up to n subtasks (which is highly unlikely, but considering the worst case for analysis).
# Sorting the subtasks for each task has a time complexity of 𝑂(𝑚log⁡𝑚), where m is the number of subtasks.
# Across all tasks, the sorting process would aggregate to 𝑂(𝑛log⁡𝑛).

# Final Sorting of Scheduled Tasks:
# After traversing and collecting all tasks, the final sorting of the scheduled_tasks list by priority is performed.
# Sorting n tasks has a time complexity of 𝑂(𝑛log⁡𝑛).
# Combining these components, the overall time complexity of the schedule_tasks function is: 𝑂(𝑛)+𝑂(𝑛log⁡𝑛)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)


# Space Complexity
# The space complexity of the schedule_tasks function includes:

# Recursive Call Stack:
# In the worst case, the recursion depth can be equal to the depth of the task hierarchy.
# If the hierarchy is highly unbalanced, the maximum recursion depth can be n (in a single chain of tasks).
# Therefore, the space required for the call stack is 𝑂(𝑛).

#Scheduled Tasks List:
# The list scheduled_tasks stores all the tasks, which requires 𝑂(𝑛) space.

# Sorting Space:
# The space complexity for the sorting operations (both during traversal and final sorting) is 𝑂(𝑛) due to the need to store temporary data during the sorting process.

# Combining these components, the overall space complexity of the schedule_tasks function is: 𝑂(𝑛)+𝑂(𝑛)+𝑂(𝑛)=𝑂(𝑛)
#Insights and Potential Optimizations

# Efficiency:
# The function is efficient for a reasonable number of tasks due to its 𝑂(𝑛log⁡𝑛) time complexity.
# The space complexity 𝑂(𝑛) is also acceptable given that it scales linearly with the number of tasks.

# Optimization Opportunities:
# Avoiding Redundant Sorting: Since subtasks are sorted during traversal, the final sorting step might be optimized by ensuring that only necessary adjustments are made.
# Iterative Approach: Converting the recursive approach to an iterative one can help avoid potential stack overflow issues for very deep hierarchies.
