// Default Google Maps places autocomplete script.
// Retrieve the cities and generate an autocomplete drop-down menu depending
// on the user input

$(function(){
    $("#id_picture").change(function(){
        var filename = $('#id_picture').val().replace(/^.*\\/, "");
        $("#id_label_picture").html(filename);
    });
});
