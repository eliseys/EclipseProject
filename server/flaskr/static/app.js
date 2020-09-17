

let url = 'http://localhost:5000/request';




// const intervalID = window.setInterval(function(){
//     fetch(url).then(response => response.json()).then((json) => {document.getElementById('sample').innerHTML = json})
// }, 1000);


//fetch(url).then(response => response.json()).then((json) => {document.getElementById('sample').innerHTML = json['c1']['year']})



const intervalID = window.setInterval(function(){
fetch(url)
    .then(response => response.json())
    .then(function(ec)
	  {
	      document.getElementById("latitude").innerHTML = `${ec['gps']['latitude']}`
	      document.getElementById("longitude").innerHTML = `${ec['gps']['longitude']}`
	      document.getElementById("altitude_m").innerHTML = `${ec['gps']['elevation_m']}`
	      document.getElementById("date_now").innerHTML = `${ec['now']['year']}/${('0'+ec['now']['month']).slice(-2)}/${('0'+ec['now']['day']).slice(-2)}`
	      document.getElementById("time_now").innerHTML = `${('0'+ec['now']['hour']).slice(-2)}:${('0'+ec['now']['minute']).slice(-2)}:${('0'+(ec['now']['second']).toFixed(0)).slice(-2)}`
	      document.getElementById("date_c1").innerHTML = `${ec['c1']['year']}/${('0'+ec['c1']['month']).slice(-2)}/${('0'+ec['c1']['day']).slice(-2)}`
	      document.getElementById("time_c1").innerHTML = `${('0'+ec['c1']['hour']).slice(-2)}:${('0'+ec['c1']['minute']).slice(-2)}:${('0'+(ec['c1']['second']).toFixed(1)).slice(-4)}`
	      document.getElementById("date_c2").innerHTML = `${ec['c2']['year']}/${('0'+ec['c2']['month']).slice(-2)}/${('0'+ec['c2']['day']).slice(-2)}`
	      document.getElementById("time_c2").innerHTML = `${('0'+ec['c2']['hour']).slice(-2)}:${('0'+ec['c2']['minute']).slice(-2)}:${('0'+(ec['c2']['second']).toFixed(1)).slice(-4)}`
	      document.getElementById("date_mid").innerHTML = `${ec['mid']['year']}/${('0'+ec['mid']['month']).slice(-2)}/${('0'+ec['mid']['day']).slice(-2)}`
	      document.getElementById("time_mid").innerHTML = `${('0'+ec['mid']['hour']).slice(-2)}:${('0'+ec['mid']['minute']).slice(-2)}:${('0'+(ec['mid']['second']).toFixed(1)).slice(-4)}`
	      document.getElementById("date_c3").innerHTML = `${ec['c3']['year']}/${('0'+ec['c3']['month']).slice(-2)}/${('0'+ec['c3']['day']).slice(-2)}`
	      document.getElementById("time_c3").innerHTML = `${('0'+ec['c3']['hour']).slice(-2)}:${('0'+ec['c3']['minute']).slice(-2)}:${('0'+(ec['c3']['second']).toFixed(1)).slice(-4)}`
	      document.getElementById("date_c4").innerHTML = `${ec['c4']['year']}/${('0'+ec['c4']['month']).slice(-2)}/${('0'+ec['c4']['day']).slice(-2)}`
	      document.getElementById("time_c4").innerHTML = `${('0'+ec['c4']['hour']).slice(-2)}:${('0'+ec['c4']['minute']).slice(-2)}:${('0'+(ec['c4']['second']).toFixed(1)).slice(-4)}`
	      document.getElementById("countdown_c1").innerHTML = `${ec['countdown_c1'].days}d ${ec['countdown_c1'].hours}h ${ec['countdown_c1'].minutes}m ${ec['countdown_c1'].seconds.toFixed(1)}s`
	      document.getElementById("countdown_c2").innerHTML = `${ec['countdown_c2'].days}d ${ec['countdown_c2'].hours}h ${ec['countdown_c2'].minutes}m ${ec['countdown_c2'].seconds.toFixed(1)}s`
	      document.getElementById("countdown_mid").innerHTML = `${ec['countdown_mid'].days}d ${ec['countdown_mid'].hours}h ${ec['countdown_mid'].minutes}m ${ec['countdown_mid'].seconds.toFixed(1)}s`
	      document.getElementById("countdown_c3").innerHTML = `${ec['countdown_c3'].days}d ${ec['countdown_c3'].hours}h ${ec['countdown_c3'].minutes}m ${ec['countdown_c3'].seconds.toFixed(1)}s`
	      document.getElementById("countdown_c4").innerHTML = `${ec['countdown_c4'].days}d ${ec['countdown_c4'].hours}h ${ec['countdown_c4'].minutes}m ${ec['countdown_c4'].seconds.toFixed(1)}s`
	  }
	 )
}, 100);
