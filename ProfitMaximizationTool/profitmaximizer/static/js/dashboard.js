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

// upload prompts
if (prompt == "successful-ingredient-import-prompt"){
	document.getElementById("successful-ingredient-import-prompt").style.display = "inline-block";
}
if (prompt == "successful-product-import-prompt"){
	document.getElementById("successful-product-import-prompt").style.display = "inline-block";
}
if (prompt == "unsuccessful-ingredient-import-prompt"){
	document.getElementById("unsuccessful-ingredient-import-prompt").style.display = "inline-block";
}
if (prompt == "unsuccessful-product-import-prompt"){
	document.getElementById("unsuccessful-product-import-prompt").style.display = "inline-block";
}

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

if (page == "inventory"){
	// Adding new ingredient record
	document.getElementById("ingr-overlay-btn").addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("add-ingredient-overlay").style.display = "block";
	})

	if (prompt == "successful-ingredient-add-prompt"){
		document.getElementById("successful-ingredient-add-prompt").style.display = "block";
	}

	// Edit ingredient record
	Array.prototype.slice.call(document.getElementsByClassName("edit-ingredient")).forEach(function(element){
		element.addEventListener("click", function(event){
			event.preventDefault();
			document.getElementById("edit-ingredient-overlay").style.display = "block";
			var recordID = event.target.parentElement.parentElement.children[0].innerText;
			var recordName = event.target.parentElement.parentElement.children[1].innerText;
			var recordCost = event.target.parentElement.parentElement.children[2].innerText;
			var recordTotalUnits = event.target.parentElement.parentElement.children[3].innerText;
			var recordDailyUnits = event.target.parentElement.parentElement.children[4].innerText;
			document.getElementById("edit-ingredient-text").innerText = "Edit IngredientRecord " + recordID;
			document.getElementById("edit-ingredient-record-id").value = recordID;
			document.getElementById("edit-ingredient-name").value = recordName;
			document.getElementById("edit-ingredient-cost").value = recordCost;
			document.getElementById("edit-ingredient-total-units").value = recordTotalUnits;
			document.getElementById("edit-ingredient-daily-units").value = recordDailyUnits;
		});
	});

	if (prompt == "successful-ingredient-edit-prompt"){
		document.getElementById("successful-ingredient-edit-prompt").style.display = "block";
	}

	// Delete ingredient record
	Array.prototype.slice.call(document.getElementsByClassName("delete-ingredient")).forEach(function(element){
		element.addEventListener("click", function(event){
			event.preventDefault();
			document.getElementById("delete-ingredient-overlay").style.display = "block";
			var recordID = event.target.parentElement.parentElement.children[0].innerText;
			document.getElementById("delete-ingredient-text").innerText = "Are you sure you want to delete IngredientRecord " + recordID + "?";
			document.getElementById("delete-ingredient-record-id").value = recordID;
		});
	});

	if (prompt == "successful-ingredient-delete-prompt"){
		document.getElementById("successful-ingredient-delete-prompt").style.display = "block";
	}

}


var nameQtyInputRowID = 0;
if (page == "products"){
	
	// Adding new product record
	document.getElementById("product-overlay-btn").addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("add-product-overlay").style.display = "block";
		clearNameQtyInputTable(document.getElementById("add-overlay-name-qty-input-table"));
	})

	if (prompt == "invalid-product-ingredients-input"){
		document.getElementById("invalid-product-ingredients-input").style.display = "block";
	}

	if (prompt == "successful-product-add-prompt"){
		document.getElementById("successful-product-add-prompt").style.display = "block";
	}

	// Edit product record
	Array.prototype.slice.call(document.getElementsByClassName("edit-product")).forEach(function(element){
		element.addEventListener("click", function(event){
			event.preventDefault();
			document.getElementById("edit-product-overlay").style.display = "block";
			var recordID = event.target.parentElement.parentElement.children[0].innerText;
			var recordName = event.target.parentElement.parentElement.children[1].innerText;
			var recordIngredients = JSON.parse(document.getElementById("product-" + recordID + "-ingredients").value.replaceAll("'", '"'));
			var recordPrice = event.target.parentElement.parentElement.children[3].innerText;

			document.getElementById("edit-product-text").innerText = "Edit ProductRecord " + recordID;
			document.getElementById("edit-product-record-id").value = recordID;
			document.getElementById("edit-product-name").value = recordName;
			document.getElementById("edit-product-price").value = recordPrice;

			var nameQtyInputTable = document.getElementById("edit-overlay-name-qty-input-table");

			clearNameQtyInputTable(nameQtyInputTable);


			for (var ingredientName of Object.keys(recordIngredients)){
				var name = ingredientName;
				var qty = recordIngredients[ingredientName];
				addNameQtyInputRow(nameQtyInputTable, name, qty);
			}


			

		});
	});

	if (prompt == "successful-product-edit-prompt"){
		document.getElementById("successful-product-edit-prompt").style.display = "block";
	}

	// Delete product record
	Array.prototype.slice.call(document.getElementsByClassName("delete-product")).forEach(function(element){
		element.addEventListener("click", function(event){
			event.preventDefault();
			document.getElementById("delete-product-overlay").style.display = "block";
			var recordID = event.target.parentElement.parentElement.children[0].innerText;
			document.getElementById("delete-product-text").innerText = "Are you sure you want to delete ProductRecord " + recordID + "?";
			document.getElementById("delete-product-record-id").value = recordID;
		});
	});

	if (prompt == "successful-product-delete-prompt"){
		document.getElementById("successful-product-delete-prompt").style.display = "block";
	}

}


if (page == "sales"){
	// Adding new sales record
	document.getElementById("sales-overlay-btn").addEventListener("click", function(event){
		event.preventDefault();
		document.getElementById("add-sales-overlay").style.display = "block";
		clearNameQtyInputTable(document.getElementById("add-overlay-name-qty-input-table"));
	})


	// Edit sales record
	Array.prototype.slice.call(document.getElementsByClassName("edit-sales")).forEach(function(element){
		element.addEventListener("click", function(event){
			event.preventDefault();
			document.getElementById("edit-sales-overlay").style.display = "block";
			var saleID = event.target.parentElement.parentElement.children[0].innerText;
			var saleDate = event.target.parentElement.parentElement.children[1].innerText;
			var saleReport =  JSON.parse(document.getElementById("sales-report-" + recordID).value.replaceAll("'", '"'));
			var saleProfit = event.target.parentElement.parentElement.children[3].innerText;

			document.getElementById("edit-sales-text").innerText = "Edit SalesRecord " + saleID;
			document.getElementById("edit-sales-record-date").value = saleID;

			var nameQtyInputTable = document.getElementById("edit-overlay-name-qty-input-table");

			clearNameQtyInputTable(nameQtyInputTable);


			for (var name of Object.keys(saleReport)){
				var qty = recordIngredients[name];
				addNameQtyInputRow(nameQtyInputTable, name, qty);
			}

		});
	});

	// Delete sales record
	Array.prototype.slice.call(document.getElementsByClassName("delete-sales")).forEach(function(element){
		element.addEventListener("click", function(event){
			event.preventDefault();
			document.getElementById("delete-sales-overlay").style.display = "block";
			var recordID = event.target.parentElement.parentElement.children[0].innerText;
			document.getElementById("delete-sales-text").innerText = "Are you sure you want to delete SalesRecord " + recordID + "?";
			document.getElementById("delete-sales-record-id").value = recordID;
		});
	});
}




Array.prototype.slice.call(document.getElementsByClassName("add-name-qty-input-row")).forEach(function(element){

	element.addEventListener("click", function(event){
		event.preventDefault();
		addNameQtyInputRow(element.previousElementSibling);

	});
});


Array.prototype.slice.call(document.getElementsByClassName("delete-name-qty-row")).forEach(function(element){
	element.addEventListener("click", function(event){
		event.preventDefault();
		deleteNameQtyInputRow(event.target);
	});
});


function addNameQtyInputRow(nameQtyInputTable, name, qty){
	var nameQtyInputRow = document.getElementsByClassName("name-qty-input-row")[0].cloneNode(true);
	nameQtyInputTable.appendChild(nameQtyInputRow);

	// delete-name-qty-input-row button
	nameQtyInputRow.children[2].addEventListener("click", function(event){
		event.preventDefault();
		deleteNameQtyInputRow(event.target);
	});
	var nameInput = nameQtyInputRow.children[0].children[0];
	var qtyInput = nameQtyInputRow.children[1].children[0].children[0].children[0];
	nameInput.name = "name-input-row-" + nameQtyInputRowID;

	var nameExists = false;
	for (var i in nameInput.children){
		var options = nameInput.children[i];
		if (options.value == name){
			nameExists = true;
			break;
		}
	}

	if (!nameExists){
		var ingrOption = nameInput.firstElementChild.cloneNode(true);
		ingrOption.value = name;
		ingrOption.innerText = name;
		nameInput.appendChild(ingrOption);
	}
	nameInput.value = name;
	qtyInput.name = "qty-input-row-" + nameQtyInputRowID;
	qtyInput.value = qty;
	nameQtyInputRowID += 1;
}

function clearNameQtyInputTable(nameQtyInputTable){
	var nameQtyInputRow = nameQtyInputTable.lastElementChild;

	while (nameQtyInputTable.children.length != 1){
		nameQtyInputTable.removeChild(nameQtyInputRow);
		nameQtyInputRow = nameQtyInputTable.lastElementChild;
	}
}

function deleteNameQtyInputRow(removeButton){
	var nameQtyInputTable = removeButton.parentElement.parentElement.parentElement;
	var nameQtyInputRow = removeButton.parentElement.parentElement;
	nameQtyInputTable.removeChild(nameQtyInputRow);
}
