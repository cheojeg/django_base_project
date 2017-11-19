var map = "";

$(document).ready(function() {
    $('#alert_close').click(function(){
    	console.log('alert_close');
		$( "#alert_box" ).fadeOut( "slow", function() {
		});
	});

	$('#table-events').DataTable( {
		select: true
	} );
  $("#table-events_length").remove();

  $('#id_sex').material_select();
  $('#id_phone_number').mask('000-0000000');

	$('#agent_select').change(function(){
	    url = $('#agent_select option:selected').data('url')
	    console.log(url, "_self");
	    location.href = url;
	});

  $('#id_birthdate').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Hoy',
    clear: 'Limpiar',
    close: 'Aceptar',
    closeOnSelect: false // Close upon selecting a date,
  });
});

function setPointOnMap(lat,lng, infowindow){
    var latlng = {lat:lat, lng:lng}
    var marker = new google.maps.Marker({
        position: latlng,
        map: map
    });
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });
}

function fined_icon(fined){
    if(fined == true){
        return '<span>Multado: <i class="material-icons" style="color: green;">check</i></span>'
    }
    else{
        return '<span>Multado: <i class="material-icons" style="color: red;">clear</i></span>'
    }
}

function renderPoints(dic){
    $.each(dic, function(i,point){
        var fined = fined_icon(point['fields']['fined'])
        var matricula = '<br /><span>' + point['fields']['marbete_id'] + '</span>'
        // Todo: Please, change that split in the created variable in the future (look down)
        var created = '<br /><span>' + point['fields']['created'].split('T')[0] + '</span>'
        var contentString = fined +
                            matricula +
                            created;
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
