$(function(){

    var animationDuration = 200;
    var userId;
    var userCompleteName;
    // Get the event when one of the sendEmail buttons has been pressed
    $('.sendEmail').click(function(){
        // Hide all possible messages in the modal popup window
        $('.errorMessageEmail').hide();
        $('.successMessageEmail').hide();
        $('#message-text').val('');

        // Get the user id of the specific contact button pressed
        userId = $(this).attr('id').replace('userContact-','');
        // Get the complete name of the current user and upload the modal title
        userCompleteName = $('#completeName-' + userId).text();
        $('#modalName').text(userCompleteName);

    });

    $('.sendEmailForm').submit(function(e){
        // Hide all messages when the form is submitted
        $('.errorMessageEmail').hide();
        $('.successMessageEmail').hide();

        // Prevent the form from being submitted
        e.preventDefault();
        var form = this;

        // Get the message
        var message = $("textarea[name='message']",form).val().trim();

        // If the message is not empty perform the Ajax request
        if(message.length != 0){
            $.get('/LanguageSwap/sendEmail/', {userId : userId, message : message} , function(data){
                // If the response is True then show success message otherwise show an error message
                if(data){
                    $('.errorMessageEmail').hide();
                    $('.successMessageEmail').fadeIn(animationDuration);
                }else{
                    $('.errorMessageEmail').text("Something occur when sending the email.");
                    $('.successMessageOut').hide();
                    $('.errorMessageEmail').fadeIn(animationDuration);
                }
            });
        }else{
            // Show an error message if it's empty
            $('.errorMessageEmail').text("The message is empty.");
            $('.successMessageOut').hide();
            $('.errorMessageEmail').fadeIn(animationDuration);
        }
    });


});
