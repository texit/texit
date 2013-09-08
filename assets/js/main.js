function renderHandler(){
	var input = (window.location.origin+"/tex/$"+$('#texinput').val()+"$.png");
	$('#texinput').val('');
	$('#stripe').animate({top:'25px'})
	$('#eqdisplay').animate({opacity:1})
	$('#texdisplay').html("<img src='"+input+"'/>");
}
function onCloseTex(){
	$('#stripe').animate({top:'35%'})
	$('#eqdisplay').animate({opacity:0})
}
