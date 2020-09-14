

let url = 'http://localhost:5000/request';

// const intervalID = window.setInterval(function(){
//     fetch(url).then(response => response.json()).then((json) => {document.getElementById('sample').innerHTML = json['C1']})
// }, 1000);


//fetch(url).then(response => response.json()).then((json) => {console.log(json)})

// const intervalID = window.setInterval(function(){
//     fetch(url).then(response => response.json()).then((json) => {document.getElementById('sample').innerHTML = [json['C1']['year'], json['C1']['month'], ]})
// }, 1000);


// fetch(url).then(response => response.json()).then((json) => {const CE = json})
// console.log(CE)



async function fetch_CE() {
    const response = await fetch(url);
    
    if (response.ok) {
	// если HTTP-статус в диапазоне 200-299
	// получаем тело ответа (см. про этот метод ниже)
	var CE = await response.json();
    } else {
	alert("HTTP error: " + response.status);
    }

    return CE
}

console.log(fetch_CE())
