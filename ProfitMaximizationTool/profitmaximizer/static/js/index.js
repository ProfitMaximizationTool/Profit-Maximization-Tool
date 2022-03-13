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

function closeErrorContainers(){
    var errorContainers = document.getElementsByClassName("error");
    for (var i = 0; i < errorContainers.length; i++){
        errorContainers[i].style.display = "none";
    }
}

// Event handlers
// open sign up
document.getElementById("opensignup-btn").addEventListener("click", function(event){
    event.preventDefault();
    opensignup();
    closeErrorContainers();
});

// close sign up
document.getElementById("closesignup-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignup();
    closeErrorContainers();
});


// open sign in
document.getElementById("opensignin-btn").addEventListener("click", function(event){
    event.preventDefault();
    opensignin();
    closeErrorContainers();
});


// close sign in
document.getElementById("closesignin-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignin();
    closeErrorContainers();
});

// go to sign up
document.getElementById("gotosignup-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignin();
    opensignup();
    closeErrorContainers();
});


// go to sign in
document.getElementById("gotosignin-btn").addEventListener("click", function(event){
    event.preventDefault();
    closesignup();
    opensignin();
    closeErrorContainers();
});


if (authError == "username taken"){
    opensignup();
    document.getElementById("username-taken-container").style.display = "block";
}
else if (authError == "passwords don't match"){
    opensignup();
    document.getElementById("passwords-mismatch-container").style.display = "block";
}
else if (authError == "login fail"){
    opensignin();
    document.getElementById("login-fail-container").style.display = "block";
}
else {
    closesignin();
    closesignup();
    closeErrorContainers();
}
