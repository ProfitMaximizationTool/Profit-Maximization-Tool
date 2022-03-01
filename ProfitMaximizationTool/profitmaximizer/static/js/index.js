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

// using AJAX would be better.
if (authError == "username taken"){
    // document.getElementById("username-taken-cont").style.display = "block";
    alert("Username already taken.")
}
else if (authError == "login fail"){
    alert("Invalid username or password.");
    // document.getElementById("login-fail-cont").style.display = "block";
}
// else {
//     var errorConts = document.getElementsByClassName("error-cont");
//     for (var i = 0; i < errorConts.length; i++){
//         errorConts[i].style.display = "none";
//     }
// }
