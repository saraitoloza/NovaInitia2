/* eslint-disable no-restricted-globals */
/**
 * This software belongs to the rightful developers of the Nova Initia application being designed at Embry-Riddle Aeronautical University.
 * Emily Nunez, Sarai Taloza, Hailey DeNys, Jacob Gattuso, Yara Alrashadi
 */

const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "1234567890") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})