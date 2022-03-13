function openimportfile(){
    document.getElementById("import-overlay").style.display = "block";
}

function closeimportfile(){
	document.getElementById("import-overlay").style.display = "none";
}

function closeErrorContainers(){
    var errorContainers = document.getElementsByClassName("error");
    for (var i = 0; i < errorContainers.length; i++){
        errorContainers[i].style.display = "none";
    }
}

document.getElementById("sidebar-container").style.left = "0%";
document.getElementById("page-content-container").style.width = "80%";

document.getElementById("toggle-sidebar-btn").addEventListener("click", function(event){
	event.preventDefault();
	var sidebarLeft = document.getElementById("sidebar-container").style.left;
	if (sidebarLeft == "0%"){
		document.getElementById("sidebar-container").style.left = "-20%";
		document.getElementById("page-content-container").style.width = "100%";
	}
	else if (sidebarLeft == "-20%"){
		document.getElementById("sidebar-container").style.left = "0%";
		document.getElementById("page-content-container").style.width = "80%";
	}
});

document.getElementById("go-to-" + page + "-btn").style.backgroundColor = "#fdeff4";

if (prompt == "saved-profile-changes"){
	document.getElementById("saved-profile-prompt").style.display = "inline-block";
}

document.getElementById("open-import").addEventListener("click", function(event){
    event.preventDefault();
    openimportfile();
    closeErrorContainers();
});

document.getElementById("close-import").addEventListener("click", function(event){
    event.preventDefault();
    closeimportfile();
    closeErrorContainers();
});


Array.prototype.slice.call(document.getElementsByClassName("table-btn")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById(element.id + "-container").click();
	});
});
