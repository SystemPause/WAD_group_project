$(function(){

    // Check if a rating form has been submitted
    $(".ratingForm").submit(function(e){

        // Prevent the submit event from being triggered
        e.preventDefault();

        // Get the reference to the current form
        var form = this;

        // Select the content of the fields userId and rating of the submitted form
        var ratedUserId = $("input[name='ratedUserId']",form).val();
        var rating = $("select[name='rating']",form).val();

        // Perform an Ajax request by accessing to the resource in /LanguageSwap/rating/ and
        // by passing to it the values ratedUserId and rating
        $.get('/LanguageSwap/rating/', {ratedUserId: ratedUserId, rating: rating} , function(data){
            // Convert the result in a JSON object
            var JsonObj = jQuery.parseJSON(data);

            // If the result is False, then an error occured while executing the request hence show an alert.
            // Otherwise just update the score in the view
            if(JsonObj.result){
                $('#scoreId' + ratedUserId).html(JsonObj.score.toFixed(1)  + '&#9733;');
            }else{
                alert("Something wrong happen when rating the current user");
            }
        });
    });
});
