function opensignup() {
    document.getElementById("signupoverlay").style.display = "block";
}

function closesignup() {
    document.getElementById("signupoverlay").style.display = "none";
}

function opensignin() {
    document.getElementById("signinoverlay").style.display = "block";
}

function closesignin() {
    document.getElementById("signinoverlay").style.display = "none";
}

function gotosignup() {
    document.getElementById("signinoverlay").style.display = "none";
    document.getElementById("signupoverlay").style.display = "block";
}

function gotosignin() {
    document.getElementById("signupoverlay").style.display = "none";
    document.getElementById("signinoverlay").style.display = "block";
}
