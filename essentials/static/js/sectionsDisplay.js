document.body.onload = function(){
    activateAnims();
}

var n = 2;

if (document.documentElement.width >= 760) 
    n=3;

var secns = document.getElementsByClassName("home-section");

window.addEventListener('scroll', function (){
    var secns = document.getElementsByClassName("home-section");
    
    for(i=1;i<secns.length;i++){
        locTmp = secns[i].getBoundingClientRect();
        if(n*locTmp.top < document.documentElement.clientHeight){
            secns[i].style.webkitFilter = "brightness(100%)";
            secns[i].style.webkitTransform = "scale(1)";
            secns[i].style.filter = "brightness(100%)";
            secns[i].style.transform = "scale(1)";
        }
        if(window.innerHeight + window.scrollY >= document.body.offsetHeight){
            secns[i].style.webkitFilter = "brightness(100%)";
            secns[i].style.webkitTransform = "scale(1)";
            secns[i].style.filter = "brightness(100%)";
            secns[i].style.transform = "scale(1)";
        }
    }
}, false);

function activateAnims(){
    document.querySelector('#title').style.animationPlayState = 'running';
    document.querySelector('#title-caption').style.animationPlayState = 'running';
    document.querySelector('#title-register').style.animationPlayState = 'running';
    document.querySelector('.home-section:first-of-type > svg #dot').style.animationPlayState = 'running';
    document.querySelector('.home-section:first-of-type > svg #v_left').style.animationPlayState = 'running';
    document.querySelector('.home-section:first-of-type > svg #v_right').style.animationPlayState = 'running';
}