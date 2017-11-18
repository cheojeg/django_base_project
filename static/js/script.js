var map = "";

$(document).ready(function() {
    $('#alert_close').click(function(){
    	console.log('alert_close');
		$( "#alert_box" ).fadeOut( "slow", function() {
		});
	});
});

function setPointOnMap(lat,lng, infowindow){
    console.log(lat, lng);
    var latlng = {lat:lat, lng:lng}
    var marker = new google.maps.Marker({
        position: latlng,
        map: map
    });
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });
}

function renderPoints(dic){
    $.each(dic, function(i,point){
        var contentString = '<span>'+
                            point['fields']['marbete_id']+
                            '</span>'
        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });

        setPointOnMap(point['fields']['latitude'], point['fields']['longitude'], infowindow)
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


