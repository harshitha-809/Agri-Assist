
// Age Calculator
document.getElementById('dob').addEventListener('change', function() {
    var ndob = document.getElementById('dob').value;
    var dob = new Date(ndob);  
    var month_diff = Date.now() - dob.getTime();  
    var age_dt = new Date(month_diff);   
    var year = age_dt.getUTCFullYear(); 
    var age = Math.abs(year - 1970);  
    document.getElementById('age').value = age;

});

// Registration Form

const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");


nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        }
    })

})

backBtn.addEventListener("click", () => form.classList.remove('secActive'));

pwShowHide = document.querySelectorAll(".eye-icon");

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
    let password = eyeIcon.parentElement.querySelector("input");
    if(password.type === "password"){
        password.type = "text";
        eyeIcon.classList.replace("bx-hide", "bx-show");
        return;
    }
    password.type = "password";
    eyeIcon.classList.replace("bx-show", "bx-hide");
    })
})      

// Global Variables

let pwdValidate = false;

// Check Password

function validateForm(passwordElem) {
    const username = document.getElementById('username').value;
    
    

    let isValid = true;

    if (!username || !password || !confirmPassword || !pwdValidate) {
        isValid = false;
    }
    return isValid;
}



function validatePassword(){
    const password = document.getElementById('password').value;
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const confirmPassword = confirmPasswordInput.value;
    const errorElement = document.getElementById('passwordError');


    if (password !== confirmPassword) {
        errorElement.textContent = 'Passwords do not match';
        confirmPasswordInput.classList.add('error');
        errorElement.classList.add('error');
        pwdValidate = false;
    } else {
        errorElement.textContent = '';
        confirmPasswordInput.classList.remove('error');
        errorElement.classList.remove('error');
        pwdValidate = true;
    }
}