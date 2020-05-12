var search = document.querySelector(".boxing");
var materials = document.querySelectorAll('.material');
var search_btn = document.querySelector('.icon');

search.addEventListener('keyup',filterNames);

function filterNames(){
    let typed = search.value.toUpperCase();
    // looping through schools to see if there is a match
    for(var i = 0;i<materials.length;i++){
        let a = materials[i].getElementsByTagName('p')[0];
        // if theres a match
        if(a.innerHTML.toUpperCase().indexOf(typed) > -1){
            materials[i].style.display = "";
        }
        else{
            materials[i].style.display = "none";
        }
    }
    
    }