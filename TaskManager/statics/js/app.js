const appDiv = document.getElementById('app');
appDiv.innerHTML = '<h2>Task Manager App</h2>';

const taskForm = document.getElementById('task-form');

taskForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    
    try {
        const response = await fetch('/api/tasks/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`, // You'll need to implement token retrieval
            },
            body: JSON.stringify({ title, description }),
        });
        
        if (response.ok) {
            alert('Task created successfully');
            // Refresh tasks or update UI as needed
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Error creating task:', error);
    }
});

const taskListDiv = document.getElementById('task-list');

// Fetch and display tasks
async function fetchTasks() {
    try {
        const response = await fetch('/api/tasks/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,
            },
        });

        if (response.ok) {
            const tasks = await response.json();
            const tasksHTML = tasks.map(task => `
                <div class="task">
                    <h3>${task.title}</h3>
                    <p>${task.description}</p>
                    <p>Status: ${task.status}</p>
                    <button class="update-status" data-task-id="${task.id}">Update Status</button>
                </div>
            `).join('');
            taskListDiv.innerHTML = tasksHTML;

            const updateButtons = document.querySelectorAll('.update-status');
            updateButtons.forEach(button => {
                button.addEventListener('click', async (e) => {
                    const taskId = e.target.getAttribute('data-task-id');
                    try {
                        const updateResponse = await fetch(`/api/tasks/${taskId}/`, {
                            method: 'PATCH',
                            headers: {
                                'Content-Type': 'application/json',
                                'Authorization': `Bearer ${token}`,
                            },
                            body: JSON.stringify({ status: 'completed' }), // Update status here
                        });

                        if (updateResponse.ok) {
                            alert('Task status updated');
                            fetchTasks(); // Refresh task list
                        } else {
                            const errorData = await updateResponse.json();
                            alert(`Error: ${errorData.detail}`);
                        }
                    } catch (error) {
                        console.error('Error updating task status:', error);
                    }
                });
            });
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Error fetching tasks:', error);
    }
}

fetchTasks();
