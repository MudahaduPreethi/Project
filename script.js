function navigateTo(page) {
    window.location.href = page;
}
/*function navigateTo(page) {
    // Change the navigation to match Flask routes
    if (page === 'login.html') {
        window.location.href = '/login';
    } else {
        window.location.href = page;
    }
}*/


function handleLogin(event) {
    event.preventDefault(); // Prevent the default form submission
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'admin' && password === 'a123') {
        alert('Login successful!');
        window.location.href = 'index.html'; // Redirect to another page after successful login
    } else {
        alert('Invalid username or password.');
    }
}
