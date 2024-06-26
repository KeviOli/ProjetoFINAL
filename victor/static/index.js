firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        window.location.href = "/home";
    }
});


function onChangeEmail() {
    toggleButtonsDisable();
    toggleEmailErrors();
}

function onChangePassword() {
    toggleButtonsDisable();
    togglePasswordErrors();
}

function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    firebase.auth().signInWithEmailAndPassword(email, password)
        .then(response => {
            window.location.href = "/home";
        })
        .catch(error => {
            alert(getErrorMessage(error));
            console.log('error', error);
        });
}

function recoverPassword() {
    const email = document.getElementById("email").value;
    
    if (!validateEmail(email)) {
        alert("Por favor, insira um email válido.");
        return;
    }

    firebase.auth().sendPasswordResetEmail(email).then(() => {
        alert('Email enviado com sucesso');
    }).catch(error => {
        alert(getErrorMessage(error));
        console.log('error', error);
    });
}

function getErrorMessage(error) {
    if (error.code === "auth/user-not-found") {
        return "Usuário não encontrado";
    } if (error.code === "auth/wrong-password") {
        return "Senha incorreta";
    } if (error.code === "auth/invalid-credential") {
        return "Credencial inválida. Por favor, verifique suas informações.";
    } if (error.code === "auth/too-many-requests") {
        return "Muitas tentativas de login. Por favor, tente novamente mais tarde.";
    }
    return error.message;
}

function register() {
    window.location.href = "/register";
}

function validateEmail(email) {
    return /\S+@\S+\.\S+/.test(email);
}

function isEmailValid() {
    const email = document.getElementById("email").value;
    return validateEmail(email);
}

function isPasswordValid() {
    const password = document.getElementById('password').value;
    return password.length > 0;
}

function toggleEmailErrors() {
    const email = document.getElementById('email').value;
    const emailRequiredError = document.getElementById('email-required-error');
    const emailInvalidError = document.getElementById('email-invalid-error');

    if (!email) {
        emailRequiredError.style.display = "block";
        emailInvalidError.style.display = "none";
    } else if (!validateEmail(email)) {
        emailRequiredError.style.display = "none";
        emailInvalidError.style.display = "block";
    } else {
        emailRequiredError.style.display = "none";
        emailInvalidError.style.display = "none";
    }
}

function togglePasswordErrors() {
    const password = document.getElementById('password').value;
    const passwordRequiredError = document.getElementById('password-required-error');

    if (!password) {
        passwordRequiredError.style.display = "block";
    } else {
        passwordRequiredError.style.display = "none";
    }
}

function toggleButtonsDisable() {
    const emailValid = isEmailValid();
    const passwordValid = isPasswordValid();

    document.getElementById('recover-password-button').disabled = !emailValid;
    document.getElementById('login-button').disabled = !emailValid || !passwordValid;
}
