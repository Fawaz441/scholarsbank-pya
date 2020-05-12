var searchbox = document.querySelector(".search_school");
var schools = document.querySelectorAll(".school");
var footer = document.querySelector(".footer");

searchbox.addEventListener("keyup",filterNames);


function filterNames(){
let typed = searchbox.value.toUpperCase();
// looping through schools to see if there is a match
for(var i = 0;i<schools.length;i++){
    let a = schools[i].getElementsByTagName('a')[0];
    // if theres a match
    if(a.innerHTML.toUpperCase().indexOf(typed) > -1){
        schools[i].style.display = "";
    }
    else{
        schools[i].style.display = "none";
    }
}

}

var schools = document.querySelectorAll(".school");
for(var i=0;i<schools.length;i+=1){
    schools[i].style.backgroundColor = "#FFF7A7";
}




