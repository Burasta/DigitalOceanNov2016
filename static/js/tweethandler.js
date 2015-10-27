$(document).ready(function () {
    $("#getrdun").click(function () {
        $("#tweets").empty();
        $.ajax({
            method: "GET",
            url: "/get_tweets"
        })
        .done(function (jdata) {
            var items = [];
            $.each(JSON.parse(jdata), function (i, obj) {
                items.push("<p>" + obj.content + "</p>");
            });
            $("#tweets").append(items);
        });
    });
});

$(document).ready(function () {
    $("#submission").submit(function () {
        var value = $("#tweettext").val();
    $.ajax({
        type: "POST",
        url: "/post_tweets",
       });
    });
});