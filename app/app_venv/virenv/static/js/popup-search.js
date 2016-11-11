$('#search').keyup(function () {
    get_items();
});

function get_items() {
    $.ajax({
            method: 'GET',
            url: '/get_items',
            search: $('#search').val()
        })
        .done(function (jdata) {
            $("#cart").empty();
            $.each(JSON.parse(jdata), function (i, obj) {
                $("#cart").append("<p class='item'>" + obj + "</p>");
            });
        });
}

//$(document).ready(function () {
//    get_tweets();
//    $('#submission').submit(function () {
//        var value = $('#tweettext').val();
//        $.ajax({
//            type: 'POST',
//            url: '/post_tweets'
//        })
//    });
//});