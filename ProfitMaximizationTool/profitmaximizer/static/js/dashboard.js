
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

document.getElementById("go-to-" + page + "-btn").style.backgroundColor = "#AEFEFF";