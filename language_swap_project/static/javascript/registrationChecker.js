$(function(){
    /*
    the function checks if the input is empty and 
    depending on the result, will alter the first parameter
    */
    function emptyChecker(errorElement,input){
        $(input).bind("focusout",function(){

            if (!$(input).val()){
               $(errorElement).html("Required Field");
               $(errorElement).css("color","red");
            } else{
               $(errorElement).html("");
            }
        });
    }
    emptyChecker("#first_name_error","#id_first_name");
    emptyChecker("#last_name_error","#id_last_name");
    emptyChecker("#pass1_error","#id_password1");
    emptyChecker("#city_error","#gMapsAutocomplete");
    emptyChecker("#birthday_error","#id_dob");

    /*
    upon focusing out on the email field, checks if the input is empty,
    a valid email format and if it exists in our database
    */
    $("#id_email").bind("focusout",function(){
        var email = $("#id_email").val();
        if (!email){
            $("#email_error").html("Required Field");
            $("#email_error").css("color","red");
        }else{
            var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
            if (pattern.test(email)){
                $.get('/LanguageSwap/emailCheck/',{email:email}, function(data){
                    if (data==1){
                        $("#email_error").html("Email is already taken");
                        $("#email_error").css("color","red");
                    }
                    else{
                        $("#email_error").html("Email Approved");
                        $("#email_error").css("color","green");
                    }
                });
            } else{
                $("#email_error").html("Invalid email");
                $("#email_error").css("color","red");
            }

        }

    });

    /*
    checks if confirm password is empty or if it is equal to the
    main password input
    */
    $("#id_password2").bind("focusout",function(){
        var pass1 = $("#id_password1").val();
        if (!$("#id_password2").val()){
            $("#pass2_error").html("Required Field");
            $("#pass2_error").css("color","red");
        }else{
            if ($("#id_password2").val() != pass1){
                $("#pass2_error").html("Passwords do not match");
                $("#pass2_error").css("color","red");
            }else{
                $("#pass2_error").html("Matching Passwords");
                $("#pass2_error").css("color","green");
            }
        }
    });
});
    