$(document).ready(function(){

  $(document).on("click",'#chose_new_product',function (e) {
        $('#chose').modal('toggle');
        e.preventDefault();
    });

    $(document).on("click",'#chose_inp',function () {
          name_product = $("#id_name_product option:selected").val();
          amount_food = $('#id_amount_food').val();
          data_time_add_product = $('#id_data_time_add_product').val();
          count_calories = $('#id_count_calories').val();
          Chose_Prod(name_product,amount_food,data_time_add_product,count_calories);
        });

    function Chose_Prod(name, amount, date, cnt_cal)
	{
		$.ajax({
			url:     "",
			type:     "post",
			dataType: "html",
			data: {
			  id_name_product: name,
              amount_food:	amount,
              data_time_add_product:date,
              count_calories:cnt_cal,
              csrfmiddlewaretoken: "{{ csrf_token }}",
              state:"inactive"
			},
			success: function(data) {
        	  $('#product_user').html(response);
        	  $('#chose').modal('hide');
    	},
    	    error: function(response) {
              console.log(response)
    	}
		});
    }

});