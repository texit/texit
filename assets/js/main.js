function renderHandler(){
	var input = (window.location.origin+"/tex/$"+$('#texinput').val()+"$.png");
	$('#texinput').val('');
	$('#stripe').animate({top:'25px'})
	$('#eqdisplay').animate({opacity:1})
	$('#texdisplay').html("<span><strong><a href='"+input+"'>"+input+"</a></strong></span><br/><br/><br/><br/><img id='teximg' src='"+input+"'/>");
}
function graphHandler(){
	var input = (window.location.origin+"/graph/"+$('#texinput').val()+".png");
	$('#texinput').val('');
	$('#stripe').animate({top:'25px'})
	$('#eqdisplay').animate({opacity:1})
	$('#texdisplay').html("<span><strong><a href='"+input+"'>"+input+"</a></strong></span><br/><br/><br/><br/><img id='teximg' width=400px hegith=400px src='"+input+"'/>");
}
function onCloseTex(){
	$('#stripe').animate({top:'35%'})
	$('#eqdisplay').animate({opacity:0})
}
