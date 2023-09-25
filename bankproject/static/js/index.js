window.onload = function(){

    let selector = document.querySelector("#branch");
    selector.addEventListener('change',function(){

        let branch_id = selector.value;
        console.log(branch_id)
        if(branch_id == "0"){
            removeChilds(document.getElementById('city'));
        }
        else{
            ajax_request(branch_id);
        }

    });


function ajax_request(id){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
     res = JSON.parse(this.responseText)
     cities = res.cities;
     removeChilds(document.getElementById('city'));
     for(const prop in cities){
        add_option(prop,cities[prop]);
     }
    }
  };
  xhttp.open("GET", `/ajax_handler/${id}`, true);
  xhttp.send();
}


function add_option(val,text){
    var sel = document.getElementById('city');

// create new option element
var opt = document.createElement('option');

// create text node to add to option element (opt)
opt.appendChild( document.createTextNode(text) );

// set value property of opt
opt.value = val;

// add opt to end of select box (sel)
sel.appendChild(opt);
}

}

var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};