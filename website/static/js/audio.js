
 	$(function(){
        //end of play
        $('#mp3Btn').on('ended', function() {
            console.log("audio end");
            $('.btn-audio').css({'background':'url("/static/image/play.png") no-repeat center bottom','background-size':'contain'});
        })
        //control function
        var audio = document.getElementById('mp3Btn');
        audio.volume = .3;
        $('.btn-audio').click(function() {
            event.stopPropagation();
            if(audio.paused){ //if pausing
                $('.btn-audio').css({'background':'url("/static/image/stop.png") no-repeat center bottom','background-size':'contain'});
                audio.play(); //play
                return;
            }else{//if playing
                $('.btn-audio').css({'background':'url("/static/image/play.png") no-repeat center bottom','background-size':'contain'});
                audio.pause(); //pause
            }
         
         
        });

    })
    