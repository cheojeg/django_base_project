$(document).ready(function() {
    $('#alert_close').click(function(){
    	console.log('alert_close');
		$( "#alert_box" ).fadeOut( "slow", function() {
		});
	});

	$('#table-events').DataTable( {
		select: true
	} );

    $('select').material_select();
    $('#id_birthdate').datepicker();
    $('#id_phone_number').mask('000-0000000');
});