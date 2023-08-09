const registerForm = document.getElementById('register-form');

registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/auth/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            alert('Registration successful. Please log in.');
            window.location.href = '/login/'; // Redirect to login page
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Error registering user:', error);
    }
});

const ws = new WebSocket('ws://' + window.location.host + '/ws/task_notifications/');

ws.onmessage = function (event) {
    const notification = JSON.parse(event.data);
    // Handle the notification, e.g., display an alert
    alert(notification);
};

// Don't forget to handle WebSocket connection errors, closures, etc.
