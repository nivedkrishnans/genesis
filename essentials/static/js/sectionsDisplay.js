document.body.onload = function(){
    activateAnims();
}

var n = 2;

if (document.documentElement.width >= 760)
    n=3;

var secns = document.getElementsByClassName("home-section");
var locTmp,pos;

function sectionDisplay(){
    for(i=1;i<secns.length;i++){
         locTmp= secns[i].getBoundingClientRect();
         pos=n;
        if(i==(secns.length-1))
            pos=1;
        if(pos*locTmp.top < document.documentElement.clientHeight){
            secns[i].style.webkitFilter = "brightness(100%)";
            secns[i].style.webkitTransform = "scale(1)";
            secns[i].style.filter = "brightness(100%)";
            secns[i].style.transform = "scale(1)";
            if(i==(secns.length-1))
                 window.removeEventListener('scroll', function(){sectionDisplay();}, false);
        }
        pos=n;
    }
}

window.addEventListener('scroll', function(){sectionDisplay();}, false);

function activateAnims(){
    document.querySelector('#title').style.animationPlayState = 'running';
    document.querySelector('#title-caption').style.animationPlayState = 'running';
    document.querySelector('#title-register').style.animationPlayState = 'running';
    document.querySelector('.home-section:first-of-type > svg #dot').style.animationPlayState = 'running';
    document.querySelector('.home-section:first-of-type > svg #v_left').style.animationPlayState = 'running';
    document.querySelector('.home-section:first-of-type > svg #v_right').style.animationPlayState = 'running';
}
