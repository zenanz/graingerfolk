$(document).ready(function () {
    $('[data-toggle=popover]').popover({
        html: true,
        container: "body",
        trigger: "click",
        placement: "bottom",
        content: function () {
            return $('#popover-content').html()
        },
    });

});

$(function () {
    $('.pop').on('click', function () {
        var caption = $(this).find("p")[0].innerHTML;
        $('.imagepreview').attr('src', $(this).find("img").attr('src'));
        $('.imagecaption').html(caption);
        $('#imagemodal').modal('show');
    });
});
