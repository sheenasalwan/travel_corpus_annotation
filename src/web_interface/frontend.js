function insert_result(response) {

	 var maintext = document.getElementById("maintext");
	 maintext.innerHTML = response;
}

function insert_result2(response) {

	var maintext2 = document.getElementById("maintext2");
	maintext2.innerHTML = response;
}


// function insert_dropdown(response) {

// 	var maintext = document.getElementById("dropdown");
// 	maintext.innerHTML = response;
// }

function update_page() {
	var form = document.getElementById("form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest( )
	xmlHttpRqst.onload = function(e) {insert_result(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/pos/?" + queryString);
	xmlHttpRqst.send();
	
}

function update_page_annotations() {
	var form = document.getElementById("dropdown");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest( )
	xmlHttpRqst.onload = function(e) {insert_result2(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/pos_annot/?" + queryString);
	xmlHttpRqst.send();
	
}