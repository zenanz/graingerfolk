// Get the video
var video = document.getElementById("background_video");

// Get the button
var btn = document.getElementById("video_control");

var btn_mute = document.getElementById("btn_mute");

// Pause and play the video, and change the button text
function myFunction() {
    if (video.paused) {
        video.play();
        btn.className = "fa fa-pause fa-2x animate_btn mr-3";
    } else {
        video.pause();
        btn.className = "fa fa-play fa-2x animate_btn mr-3";
    }
}

function mute() {
    if (video.muted) {
        video.muted = false;
        btn_mute.className = "fa fa-volume-up fa-2x animate_btn"
    } else {
        video.muted = true;
        btn_mute.className = "fa fa-volume-off fa-2x animate_btn"
    }
}