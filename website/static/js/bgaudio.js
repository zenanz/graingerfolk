$('.btn-audio').click(function () {
    var audio = $(this).siblings("audio")[0];
    if (audio.paused) { //if pausing
        $(this).removeClass('fa-play');
        $(this).addClass('fa-pause');
        audio.play(); //play
    } else {//if playing
        $(this).removeClass('fa-pause');
        $(this).addClass('fa-play');
        audio.pause(); //pause
    }
});