function main_size() {
    var h = document.getElementsByTagName('HEADER')[0];
    var f = document.getElementsByTagName('FOOTER')[0];
    var b = document.getElementsByTagName('BODY')[0];
    var m = document.getElementsByTagName('MAIN')[0];
    m.style.height = (b.clientHeight - h.clientHeight - f.clientHeight) + "px";
}

$(document).ready(function () {
    main_size();
});

$(window).resize(function () {
    main_size();
});
