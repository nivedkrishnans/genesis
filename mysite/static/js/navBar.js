var navBar = document.getElementById("navBar");
var navMobile = document.getElementById('navBarMobile');
var homeNav = document.getElementById("homeNav");
var ham = document.getElementById('hamburgerButton');
var navDisplay = false;     //whether or not nav menu is displayed on mobile
var navSets = document.getElementsByClassName("navLinkSet");

window.onresize = function(){
    toggleNavMobile(false);
    if(document.documentElement.clientWidth >= 760){
        navSets[0].style.flex = "4 0 0";
        navSets[1].style.flex = "1 0 0";
        navSets[2].style.flex = "4 0 0";
        navBar.style.top = "0";
    }
    else{
        navSets[0].style.flex =  "1 0 100%";
        navSets[1].style.flex =  "1 0 100%";
        navSets[2].style.flex =  "1 0 100%";
    }
};

window.onload = function(){
    toggleNavMobile(false);
    if(document.documentElement.clientWidth >= 760){
        navBar.style.top = "0";
        navSets[0].style.flex = "4 0 0";
        navSets[1].style.flex = "1 0 0";
        navSets[2].style.flex = "4 0 0";
    }
    else{
        navSets[0].style.flex =  "1 0 100%";
        navSets[1].style.flex =  "1 0 100%";
        navSets[2].style.flex =  "1 0 100%";
    }
};

function toggleNavMobile(disp){         //shows nav menu for mobile if argument is true, otherwise hides

    if(!disp){
        navMobile.style.borderBottom = "#ffee9c solid 1px";
        navBar.style.top = "-280px";
        ham.classList.remove('is-active');
        homeNav.style.opacity= "0";
    }
    else{
        navMobile.style.borderBottom = "#000000 solid 1px";
        navBar.style.top = "44px";
        ham.classList.add('is-active');
        homeNav.style.opacity= "1";
    }
    navDisplay = !navDisplay;
}

ham.addEventListener("click", function() {
    toggleNavMobile(!navDisplay);
    }, true);
