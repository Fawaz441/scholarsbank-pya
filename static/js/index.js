var mobile_nav = document.querySelector('.mobile_nav');
var backdrop = document.querySelector('.backdrop');
var mobile_nav_exit = document.querySelector('.exit');
var get = document.getElementById("get");
var body = document.querySelector(".cover");
var nav = document.querySelector(".nav");




get.addEventListener("click",function(){
    mobile_nav.style.width="220px";
    backdrop.style.display="block";
})

backdrop.addEventListener("click",function(){
    mobile_nav.style.width="0";
    backdrop.style.display="none";
})

mobile_nav_exit.addEventListener("click",function(){
   
    mobile_nav.style.width = "0";
    backdrop.style.display = "none";
})

// Slide 1
var slideIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  x[slideIndex-1].style.display = "block";
  setTimeout(carousel, 5000); // Change image every 5 seconds
}


// Slide 2
var slideIndex2 = 0;
carousel2();


function carousel2() {
  var i;
  var x = document.getElementsByClassName("mySlides2");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex2++;
  if (slideIndex2 > x.length) {slideIndex2 = 1}
  x[slideIndex2-1].style.display = "block";
  setTimeout(carousel2, 4000); // Change image every 4 seconds
}

// Slide 3
var slideIndex3 = 0;
carousel3();


function carousel3() {
  var i;
  var x = document.getElementsByClassName("mySlides3");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex3++;
  if (slideIndex3 > x.length) {slideIndex3 = 1}
  x[slideIndex3-1].style.display = "block";
  setTimeout(carousel3, 3000); // Change image every 3 seconds
}

// fade in effects
function fadeIn(){
  var scholarships = document.querySelector('.scholarships');
  var scholarshipsY = scholarships.getBoundingClientRect().top;
  var buy = document.querySelector('.buy_and_sell');
  var buyY = buy.getBoundingClientRect().top;
  var materials = document.querySelector('.materials');
  var materialsY = materials.getBoundingClientRect().top;
  var appearingHeight = window.innerHeight/1.3;

  if(buyY < appearingHeight){
    buy.classList.add('appear');
  }
  if(scholarshipsY < appearingHeight){
    scholarships.classList.add('appear');
  }
}


window.addEventListener('scroll',fadeIn);