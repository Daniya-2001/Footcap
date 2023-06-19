$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        
        var qty = $(this).closest('.product_data').find('.input-qty').val();
        var value = parseInt(qty,10);
        value = isNaN(value) ? 0 : value;
        if(value <10)
        {
            value ++;
           
            $(this).closest('.product_data').find('.input-qty').val(value);
        } 
    });


    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        
        var qty = $(this).closest('.product_data').find('.input-qty').val();
        var value = parseInt(qty,10);
        value = isNaN(value) ? 0 : value;
        if(value > 0)
        {
            value--;
           
            $(this).closest('.product_data').find('.input-qty').val(value);
        }

        
    });
    
   // AddtoCart-----------------------
   $('.addToCartBtn').click(function (e) { 
    e.preventDefault();
    var product_id=$(this).closest('.product_data').find('.prod_id').val();
    var product_qty=$(this).closest('.product_data').find('.input-qty').val();
    // csrftoken------------------------
    var token=$('input[name=csrfmiddlewaretoken]').val();
    // ajax------------------------------
    $.ajax({
        type: "POST",
        url: "/add-to-cat",
        data: {
            'product_id':product_id,
            'product_qty':product_qty,
            csrfmiddlewaretoken:token

        },
       
        success: function (response) {
            console.log(response)
        alertify.success(response.status)
            
        }
    });
    
   });
       
    
});