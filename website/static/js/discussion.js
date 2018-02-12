var csrftoken = Cookies.get('csrftoken');

$('#commentModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var recipient = button.data('username');// Extract info from data-* attributes
    var cid = button.data('cid');// Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('.modal-title').text('Reply to: @' + recipient);
    modal.find('.modal-body #recipient-name').attr('value', recipient);
    modal.find('.modal-body #reply-to-id').attr('value', cid);
});

$('#reply-submit').on('click', function () {
    $('#reply-form').submit();
});

function like(cid) {
    $.ajax({
        url: 'http://' + host + '/collection/comment/like/' + cid + '/',
        type: 'GET',
        data: {},
        dataType: 'json',
        headers: {'X-CSRFToken': csrftoken},
        success: function (data) {
            var icon = $('#like-icon-' + cid)[0];
            var count = $('#like-count-' + cid)[0];
            if (icon.className.includes('fa-thumbs-up')) {
                icon.className = 'fa fa-thumbs-o-up fa-lg animate_btn';
            } else {
                icon.className = 'fa fa-thumbs-up fa-lg animate_btn';
            }
            count.innerHTML = data.count + ' |'

        },

        error: function () {
        }

    })

}
