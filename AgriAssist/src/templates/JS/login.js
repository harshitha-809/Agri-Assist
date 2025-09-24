const forms = document.querySelector(".forms");
pwShowHide = document.querySelectorAll(".eye-icon");

pwShowHide.forEach(eyeIcon => {
eyeIcon.addEventListener("click", () => {
  let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
  
  pwFields.forEach(password => {
      if(password.type === "password"){
          password.type = "text";
          eyeIcon.classList.replace("bx-hide", "bx-show");
          return;
      }
      password.type = "password";
      eyeIcon.classList.replace("bx-show", "bx-hide");
  })
  
})
})      

function showErr(show, elem) {
    if (show) {
        elem.classList.add("invalid");
        elem.parentNode.querySelector("p.errTxt").style.display = "block";
        return false
    } else {
        elem.classList.remove("invalid");
        elem.parentNode.querySelector("p.errTxt").style.display = "none";
        return true
    }
}

function validate(elem) {

    if (elem.value == "") {
        return showErr(true, elem);  
    } else {
        if (elem.checkValidity()) {
            return showErr(false, elem);
        } else {
            return showErr(true, elem);
        }
    }
}

function validateForm(form) {
    let inputs = form.querySelectorAll(".required");
    for (let i = 0; i < inputs.length; i++) {
        const input = inputs[i];
        if (validate(input) == false) {
            return false;
        }
    }
}