

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('.img')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$('#profile_upload_button').click(
    function () {
        $("input[id='id_profile_photo']").click();
    }
)
