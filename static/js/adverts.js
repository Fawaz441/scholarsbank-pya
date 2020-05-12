
// Slide 5
var slideIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides5");
  var y = document.getElementsByClassName("index_h1");
  var z = document.getElementsByClassName("index_h2");
  var a = document.getElementsByClassName("redirectors");

  for (i = 0; i < x.length; i++){
    x[i].style.display = "none";
    y[i].style.display = "none";
    z[i].style.display = "none";
    a[i].style.display = "none";

  }

  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  x[slideIndex-1].style.display = "block";
  y[slideIndex-1].style.display = "block";
  z[slideIndex-1].style.display = "block";
  a[slideIndex-1].style.display = "block";



  setTimeout(carousel, 5000); // Change image every 5 seconds
}