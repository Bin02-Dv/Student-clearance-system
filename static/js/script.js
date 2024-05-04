var btn_open = document.getElementById("open");
var btn_close = document.getElementById("close");
var nav = document.getElementById("nav");

btn_open.addEventListener("click", function(){
    nav.classList.add("show");
});

btn_close.addEventListener("click", function(){
    nav.classList.remove("show");
});