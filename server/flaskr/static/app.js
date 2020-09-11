

let url = 'http://localhost:5000/request';

// const intervalID = window.setInterval(function(){
//     fetch(url).then(response => response.json()).then((json) => {document.getElementById('sample').innerHTML = json['C1']})
// }, 1000);


fetch(url).then(response => response.json()).then((json) => {console.log(json)})
