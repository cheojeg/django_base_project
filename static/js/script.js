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
        // return '<span><i class="material-icons" style="color: green;">check</i></span>'
        return '<span style="color: green;"><b>Valido</b></span>'
    }
    else{
        // return '<span><i class="material-icons" style="color: red;">clear</i></span>'
        return '<span style="color: red;"><b>Multado</b></span>'
    }
}

function renderPoints(dic){
    $.each(dic, function(i,point){
        var agent = '<span><b>Agente: </b></span>' + point['fields']['agent_number'] + ' - ' + point['fields']['agent'] +'</span>'
        var fined = '<br /<span><b>Estado: </b></span>' + fined_icon(point['fields']['fined'])
        var matricula = '<br /><span><b>Matricula: </b>' + point['fields']['license_plate'] + '</span>'
        // Todo: Please, change that split in the created variable in the future (look down)
        var propietario = '<br /><span><b>Propietario: </b>' + point['fields']['owner'] + '</span>'
        var created = '<br /><span><b>Fecha y Hora: </b>' + point['fields']['time'] + '</span>'
        if (point['fields']['capture_img'] == 'http://10.193.0.97:8000/media/'){
          var img = '';
        } else {
          var img = '<br /><center><img src="' + point['fields']['capture_img'] + '" height="180" width="150" style="margin-top: 10px;"></img></center>';
        }
        var contentString = agent + fined + matricula + propietario + created + img;
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
