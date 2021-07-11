function insert_result(response) {
	 var maintext = document.getElementById("maintext");
	 maintext.innerHTML = response;
}


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