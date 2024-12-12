document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector(".login-form");
    const usernameInput = document.querySelector(".username-input");
    const passwordInput = document.querySelector(".password-input");
    const submitButton = document.querySelector(".login-button");
    const togglePassword = document.querySelector('.toggle-password');

    // Функция для проверки валидности формы
    function checkFormValidity() {
        console.log(usernameInput.value.trim(), passwordInput.value.trim());
        if (usernameInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    }

    usernameInput.addEventListener('input', checkFormValidity);
    passwordInput.addEventListener('input', checkFormValidity);
    checkFormValidity();

    // Функция для обновления стилей плейсхолдера
    function updatePlaceholder(input) {
        const placeholder = input.nextElementSibling;
        if (input.value.trim() !== '') {
            placeholder.style.fontSize = '12px';
            placeholder.style.top = '10px';
            placeholder.style.color = '#747474';
        } else {
            placeholder.style.fontSize = '16px';
            placeholder.style.top = '20px';
            placeholder.style.color = '#747474';
        }
    }

    // Обработчики событий для полей ввода
    usernameInput.addEventListener('input', () => updatePlaceholder(usernameInput));
    passwordInput.addEventListener('input', () => updatePlaceholder(passwordInput));

    // События для фокуса и потери фокуса
    usernameInput.addEventListener('focus', () => updatePlaceholder(usernameInput));
    passwordInput.addEventListener('focus', () => updatePlaceholder(passwordInput));
    usernameInput.addEventListener('blur', () => updatePlaceholder(usernameInput));
    passwordInput.addEventListener('blur', () => updatePlaceholder(passwordInput));

    // Обработчик клика для отображения/скрытия пароля
    togglePassword.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        this.textContent = type === 'password' ? '🙈' : '🙉';
    });
    
});
