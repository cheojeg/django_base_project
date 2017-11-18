var map = "";

$(document).ready(function() {
    $('#alert_close').click(function(){
    	console.log('alert_close');
		$( "#alert_box" ).fadeOut( "slow", function() {
		});
	});
});

function setPointOnMap(lat,lng){
    console.log(lat, lng);
    var latlng = {lat:lat, lng:lng}
    var marker = new google.maps.Marker({
        position: latlng,
        map: map
    });
}

function renderPoints(dic){
    $.each(dic, function(i,point){
        setPointOnMap(point['fields']['latitude'], point['fields']['longitude'])
    });
}

function initMap() {
    var center = {lat:18.47, lng:-69.9}
    map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: center
    });
    renderPoints(detections);
}


