// Default Google Maps places autocomplete script. 
// Retrieve the cities and generate an autocomplete drop-down menu depending 
// on the user input
var autocomplete = new google.maps.places.Autocomplete((document.getElementById('gMapsAutocomplete')), {types: ['(cities)']});
