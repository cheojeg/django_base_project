var map = "";

$(document).ready(function() {
    $('#alert_close').click(function(){
    	console.log('alert_close');
		$( "#alert_box" ).fadeOut( "slow", function() {
		});
	});

<<<<<<< HEAD
	$('#table-events').DataTable( {
		select: true
	} );

    $('select').material_select();
    $('#id_birthdate').datepicker();
    $('#id_phone_number').mask('000-0000000');
});
=======
	$('#agent_select').change(function(){
	    url = $('#agent_select option:selected').data('url')
	    console.log(url, "_self");
	    location.href = url;
	})
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
                            point['fields']['fined']+
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


>>>>>>> 702fff08f649d9d00872cc946836cb113362f218
