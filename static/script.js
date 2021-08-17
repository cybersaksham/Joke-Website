// Function to clear modal
function clearModal(){
    $('#jokeTitle').show();
    $('#errorTitle').hide();
    $('#jokeText').text("");
    $('#errorText').text("");
}

// Function to show errors
function showError($text){
    $('#jokeModal').modal('show');
    $('#jokeTitle').hide();
    $('#errorTitle').show();
    $('#errorText').text($text);
}

// Function to show jokes
function showJoke($text){
    $('#jokeModal').modal('show');
    $('#jokeTitle').show();
    $('#errorTitle').hide();
    $('#jokeText').text($text);
}

//Starting Point
$(document).ready(function (){
    // Clearing modal initially
    clearModal();

    // Clicking submit button
    $('#submitBtn').click(function(e){
        e.preventDefault();
        clearModal();
        // Sending request to get jokes
        $.ajax({
            url: "/get_joke",
            method: "POST",
            data: $('#jokeForm').serialize(),
            success: function(res){
                if(res["error"] == null){
                    showJoke(res["joke"]);
                }
                else{
                    showError(res["error"]);
                }
            },
            error: function(){
                showError("Network Error");
            }
        });
    });
});