var csrftoken = Cookies.get('csrftoken');
var skip_count = 1;
var load_button = $('#load-button');
var total = 0;

$(function () {
    load_button.on('click', function () {
        $.ajax({
            url: 'http://'+host+'/collection/load/',
            type: 'POST',
            data: {keyword: $('#keyword').attr('value'), skip: skip_count},
            dataType: 'json',
            headers: {'X-CSRFToken': csrftoken},
            success: function (data) {
                total = data.total;
                var results = data.results;
                for (var i = 0; i < results.length; i++) {
                    var obj = results[i];
                    var creators = obj.creators;
                    var creation_dates = obj.creation_dates;
                    var cards = $('#card-group');
                    var header = '<div class="card new-item my-5  d-flex justify-content-between flex-column">';
                    var body = '<div class="row card-body"><div class="col-sm-4 "><div class="card-img-container">';
                    var footer = '';

                    header += '<div class="card-header"><h4 class="card-title text-center">' + obj.title + '</h4></div>';

                    //add image
                    if (obj.thumbnail_url != null) {
                        body += '<img class="card-img" src="' + obj.thumbnail_url + '" alt="Card image cap">';
                        body += '<h4 class="card-title card-title-overlay">' + obj.title + '</h4>';
                    } else {
                        body += '<img class="card-img" src="/static/image/placeholder.jpg" alt="Card image cap">';
                        body += '<h4 class="card-title card-title-overlay">No Image</h4>';
                    }

                    //add creators
                    body += '</div></div><div class="col-sm-8 d-flex justify-content-between flex-column"><div class="container text-sm-right pt-3 pt-sm-0">'

                    if (authenticated){
                        body += '<a onclick="favorite(this.id)" id="'+obj.slug+'">';
                        if ($.inArray(obj.slug, favs) > -1){
                            body += '<i class="fa fa-star fa-lg fav"></i>'
                        } else {
                            body += '<i class="fa fa-star-o fa-lg fav"></i>'
                        }
                        body += '</a>'
                    }

                    body += '</div><div class="container"><dl class="row py-3 mb-0"><dt class="col-md-6 "><p><i class="fa fa-user pr-2"></i>Creators</p></dt><dd class="col-md-6">';
                    if (creators != null) {
                        for (var j = 0; j < creators.length; j++) {
                            body += '<p>' + creators[j] + '</p>';
                        }
                    }

                    body += '</dd><dt class="col-md-6 "><p><i class="fa fa-calendar pr-2"></i>Creation dates</p></dt><dd class="col-md-6">';

                    if (creation_dates != null) {
                        for (j = 0; j < creation_dates.length; j++) {
                            body += '<p>' + creation_dates[j] + '</p>';
                        }
                    }


                    body += '</dd></dl></div><div class="container"></div></div></div>';
                    if (obj.reference_code != null) {
                        footer = '<div class="card-footer text-muted caption text-center">' + obj.reference_code + '</div></div>';
                    } else {
                        footer = '<div class="card-footer text-muted caption text-center">No reference code avaliable</div></div>';
                    }

                    var d = $(header + body + footer);

                    d.hide().appendTo(cards).show('slow');
                    window.scrollBy({
                        top: $(window).height() * 0.7, // could be negative value
                        left: 0,
                        behavior: 'smooth'
                    });

                }
                skip_count += 1;
                load_button.text('Load more');
                if (skip_count * 10 >= total) {
                    load_button.prop('disabled', true);
                    load_button.text('No more items');

                }
            },
            error: function () {
                alert('boo!');
            }
        });

    });
});