function openimportfile(){
    document.getElementById("import-overlay").style.display = "block";
}

function closeimportfile(){
	document.getElementById("import-overlay").style.display = "none";
}

function closeOverlay(){
	Array.prototype.slice.call(document.getElementsByClassName("overlay")).forEach(function(element){
		element.style.display = "none";
	});
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


Array.prototype.slice.call(document.getElementsByClassName("close")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		closeOverlay();
	})
});


// Handlers for the import data buttons

Array.prototype.slice.call(document.getElementsByClassName("card")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		element.style.backgroundColor = "#fdeff4";
		document.getElementById(element.id + "-container").click();
	});
});

if(page == "inventory")
{
// Adding new ingredient record
document.getElementById("ingr-overlay-btn").addEventListener("click", function(event){
	event.preventDefault();
	document.getElementById("add-ingredient-overlay").style.display = "block";
})


// Edit ingredient record
Array.prototype.slice.call(document.getElementsByClassName("edit-ingredient")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("edit-ingredient-overlay").style.display = "block";
		var recordID = event.target.parentElement.parentElement.children[0].innerText;
		var recordName = event.target.parentElement.parentElement.children[1].innerText;;
		var recordCost = event.target.parentElement.parentElement.children[2].innerText;;
		var recordTotalUnits = event.target.parentElement.parentElement.children[3].innerText;;
		var recordDailyUnits = event.target.parentElement.parentElement.children[4].innerText;;
		document.getElementById("edit-ingredient-text").innerText = "Edit IngredientRecord " + recordID;
		document.getElementById("edit-ingredient-record-id").value = recordID;
		document.getElementById("edit-ingredient-name").value = recordName;
		document.getElementById("edit-ingredient-cost").value = recordCost;
		document.getElementById("edit-ingredient-total-units").value = recordTotalUnits;
		document.getElementById("edit-ingredient-daily-units").value = recordDailyUnits;

	});
});

// Delete ingredient record
Array.prototype.slice.call(document.getElementsByClassName("delete-ingredient")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("delete-ingredient-overlay").style.display = "block";
		var recordID = event.target.parentElement.parentElement.children[0].innerText;
		document.getElementById("delete-ingredient-text").innerText = "Are you sure you want to delete IngredientRecord " + recordID + " ?";
		document.getElementById("delete-ingredient-record-id").value = recordID;
	});
});

}

if(page == "products")
{
// Adding new product record
document.getElementById("product-overlay-btn").addEventListener("click", function(event){
	event.preventDefault();
	document.getElementById("add-product-overlay").style.display = "block";
})


// Edit product record
Array.prototype.slice.call(document.getElementsByClassName("edit-product")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("edit-product-overlay").style.display = "block";
		var recordID = event.target.parentElement.parentElement.children[0].innerText;
		var recordName = event.target.parentElement.parentElement.children[1].innerText;;
		var recordIngredients = event.target.parentElement.parentElement.children[2].innerText;;
		var recordPrice = event.target.parentElement.parentElement.children[3].innerText;;
		document.getElementById("edit-product-text").innerText = "Edit ProductRecord " + recordID;
		document.getElementById("edit-product-record-id").value = recordID;
		document.getElementById("edit-product-name").value = recordName;
		document.getElementById("edit-product-ingredients").value = recordIngredients;
		document.getElementById("edit-product-price").value = recordPrice;

	});
});

// Delete ingredient record
Array.prototype.slice.call(document.getElementsByClassName("delete-product")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("delete-product-overlay").style.display = "block";
		var recordID = event.target.parentElement.parentElement.children[0].innerText;
		document.getElementById("delete-product-text").innerText = "Are you sure you want to delete ProductRecord " + recordID + " ?";
		document.getElementById("delete-product-record-id").value = recordID;
	});
});
}