document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("register-form");
    const loginForm = document.getElementById("login-form");

    function validateUsername(username) {
        return /^[a-zA-Z0-9]+$/.test(username);
    }

    function validatePassword(password) {
        return password.length >= 6;
    }

    function showError(input, message) {
        const formControl = input.parentElement;
        const errorElement = formControl.querySelector("small");
        errorElement.innerText = message;
        formControl.classList.add("error");
    }

    function clearError(input) {
        const formControl = input.parentElement;
        formControl.classList.remove("error");
        const errorElement = formControl.querySelector("small");
        errorElement.innerText = "";
    }

    registerForm.addEventListener("submit", function(event) {
        const usernameInput = document.getElementById("register-username");
        const passwordInput = document.getElementById("register-password");

        if (!validateUsername(usernameInput.value)) {
            showError(usernameInput, "Username can only contain letters and numbers.");
            event.preventDefault();
        } else {
            clearError(usernameInput);
        }

        if (!validatePassword(passwordInput.value)) {
            showError(passwordInput, "Password must be at least 6 characters long.");
            event.preventDefault();
        } else {
            clearError(passwordInput);
        }

        if (!usernameInput.parentElement.classList.contains("error") && 
            !passwordInput.parentElement.classList.contains("error")) {
            const formData = new FormData(registerForm);
            
            fetch('/api/register', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert(data.message); // Display a message to the user
                registerForm.reset(); // Reset the form
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('An error occurred. Please try again.');
            });
        }
    });

    loginForm.addEventListener("submit", function(event) {
        const usernameInput = document.getElementById("login-username");
        const passwordInput = document.getElementById("login-password");

        if (!validateUsername(usernameInput.value)) {
            showError(usernameInput, "Username can only contain letters and numbers.");
            event.preventDefault();
        } else {
            clearError(usernameInput);
        }

        if (!validatePassword(passwordInput.value)) {
            showError(passwordInput, "Password must be at least 6 characters long.");
            event.preventDefault();
        } else {
            clearError(passwordInput);
        }

        if (!usernameInput.parentElement.classList.contains("error") && 
            !passwordInput.parentElement.classList.contains("error")) {
            const formData = new FormData(loginForm);
            
            fetch('/api/login', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert(data.message); // Display a message to the user
                loginForm.reset(); // Reset the form
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('An error occurred. Please try again.');
            });
        }
    });
});
