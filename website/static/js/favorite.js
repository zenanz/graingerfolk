var csrftoken = Cookies.get('csrftoken');

function favorite(id) {
    $.ajax({
        url: 'http://'+host+'/collection/favorites/',
        type: 'POST',
        data: {keyword: id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrftoken},
        success: function (data) {
            var icon = $('#' + id).children()[0];
            if (icon.className.includes('fa-star-o')) {
                icon.className = 'fa fa-star fa-lg fav';
            } else {
                icon.className = 'fa fa-star-o fa-lg fav';
            }

        },

        error: function (data) {
            console.log(data)
        }

    })
}