var myVar = setInterval(function(){ get_tweets() }, 5000);

function get_tweets() {
    $.ajax({
        method: 'GET',
        url: '/get_tweets'
    })
    .done(function (jdata) {
        $("#tweets").empty();
        $.each(JSON.parse(jdata), function (i, obj) {
            $("#tweets").append("<p class='tweet'>" + obj + "</p>");
        });
    });
}

$(document).ready(function () {
    get_tweets();
    $('#submission').submit(function () {
        var value = $('#tweettext').val();
    $.ajax({
        type: 'POST',
        url: '/post_tweets'
       })
    });
});