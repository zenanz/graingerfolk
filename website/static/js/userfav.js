function fadeFavorite(id) {
    favorite(id);
    $("#" + id + "-card").animate({height: "toggle", opacity: 'toggle'}, 500, function () {
        $(this).remove()
    });

}

function changevalue(order) {
    if (order === 0) {
        $('#d').val('-date_added');
    } else {
        $('#d').val('date_added');
    }
    $('#search-form').submit()
}