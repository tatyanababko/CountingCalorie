$(document).ready(function(){

  $(document).on("click",'#chose_new_product',function (e) {
		$('#chose').modal('toggle');
		e.preventDefault();
	});

});