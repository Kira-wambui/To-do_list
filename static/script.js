document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("register-form");
    const loginForm = document.getElementById("login-form");
    const errorMessageContainer = document.getElementById("error-message");

    // Function to validate username
    function validateUsername(username) {
        return /^[a-zA-Z0-9]+$/.test(username);
    }

    // Function to validate password
    function validatePassword(password) {
        return password.length >= 6;
    }

    // Function to show error message
    function showError(input, message) {
        const formControl = input.parentElement;
        const errorElement = formControl.querySelector(".error-message");
        errorElement.innerText = message;
        formControl.classList.add("error");
    }

    // Function to clear error message
    function clearError(input) {
        const formControl = input.parentElement;
        formControl.classList.remove("error");
        const errorElement = formControl.querySelector(".error-message");
        errorElement.innerText = "";
    }

    // Function to display global error message
    function showGlobalError(message) {
        errorMessageContainer.innerText = message;
        errorMessageContainer.style.display = "block";
    }

    // Function to clear global error message
    function clearGlobalError() {
        errorMessageContainer.innerText = "";
        errorMessageContainer.style.display = "none";
    }

    // Event listener for form submission - Register
    registerForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Validate username
        const usernameInput = document.getElementById("register-username");
        if (!validateUsername(usernameInput.value)) {
            showError(usernameInput, "Username can only contain letters and numbers.");
            return;
        } else {
            clearError(usernameInput);
        }

        // Validate password
        const passwordInput = document.getElementById("register-password");
        if (!validatePassword(passwordInput.value)) {
            showError(passwordInput, "Password must be at least 6 characters long.");
            return;
        } else {
            clearError(passwordInput);
        }

        // Perform form submission with fetch API
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
            showGlobalError('An error occurred. Please try again.');
        });
    });

    // Event listener for form submission - Login
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Validate username
        const usernameInput = document.getElementById("login-username");
        if (!validateUsername(usernameInput.value)) {
            showError(usernameInput, "Username can only contain letters and numbers.");
            return;
        } else {
            clearError(usernameInput);
        }

        // Validate password
        const passwordInput = document.getElementById("login-password");
        if (!validatePassword(passwordInput.value)) {
            showError(passwordInput, "Password must be at least 6 characters long.");
            return;
        } else {
            clearError(passwordInput);
        }

        // Perform form submission with fetch API
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
            showGlobalError('An error occurred. Please try again.');
        });
    });
});

