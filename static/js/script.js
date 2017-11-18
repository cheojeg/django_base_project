$(document).ready(function() {
    $('#alert_close').click(function(){
    	console.log('alert_close');
		$( "#alert_box" ).fadeOut( "slow", function() {
		});
	});
});