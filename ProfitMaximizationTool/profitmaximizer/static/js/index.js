function opensignup(){
    document.getElementById("signupoverlay").style.display = "block";
}

function closesignup(){
    document.getElementById("signupoverlay").style.display = "none";
}

function opensignin(){
    document.getElementById("signinoverlay").style.display = "block";
}

function closesignin(){
    document.getElementById("signinoverlay").style.display = "none";
}

function closeErrorConts(){
    var errorConts = document.getElementsByClassName("error-cont");
    for (var i = 0; i < errorConts.length; i++){
        errorConts[i].style.display = "none";
    }
}

// Event handlers
// open sign up
document.getElementById("opensignup-btn").addEventListener("click", function(event){
    event.preventDefault();
    opensignup();
    closeErrorConts();
});

// close sign up
document.getElementById("closesignup-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignup();
    closeErrorConts();
});


// open sign in
document.getElementById("opensignin-btn").addEventListener("click", function(event){
    event.preventDefault();
    opensignin();
    closeErrorConts();
});


// close sign in
document.getElementById("closesignin-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignin();
    closeErrorConts();
});

// go to sign up
document.getElementById("gotosignup-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignin();
    opensignup();
    closeErrorConts();
});


// go to sign in
document.getElementById("gotosignin-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignup();
    opensignin();
    closeErrorConts();
});


if (authError == "username taken"){
    opensignup();
    document.getElementById("username-taken-cont").style.display = "block";
}
else if (authError == "passwords don't match"){
    opensignup();
    document.getElementById("passwords-mismatch-cont").style.display = "block";
}
else if (authError == "login fail"){
    opensignin();
    document.getElementById("login-fail-cont").style.display = "block";
}
else {
    closesignin();
    closesignup();
    closeErrorConts();
}
