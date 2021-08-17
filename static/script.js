function clearModal(){
    $('#jokeTitle').show();
    $('#errorTitle').hide();
    $('#jokeText').val("");
    $('#errorText').val("");
}

function showError($text){
    $('#jokeModal').modal('show');
    $('#jokeTitle').hide();
    $('#errorTitle').show();
    $('#errorText').val($text);
}

function showJoke($text){
    $('#jokeModal').modal('show');
    $('#jokeTitle').show();
    $('#errorTitle').hide();
    $('#jokeText').val($text);
}

$(document).ready(function (){
    clearModal();

    $('#submitBtn').click(function(e){
        e.preventDefault();
        clearModal();
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