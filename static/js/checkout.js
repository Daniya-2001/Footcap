











//////////////////////////////


$(document).ready(function () {
    $('.pay').click(function (e) { 
        e.preventDefault();
        var name = $("[name='name']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var pincode = $("[name='pincode']").val();
        var Address = $("[name='Address']").val();
        var country = $("[name='country']").val();
        //var state = $("[name='state']").val();
        var city = $("[name='city']").val();
        var token=$("[name='csrfmiddlewaretoken']").val();
        if(name == "" || email == "" || phone == ""  || pincode == "" || Address == ""  ||  city == ""  ||  country == "" )
        {
         
           swal("Alert!", "All fields are mandatory!", "error");
            return false
        }
        else
        {
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                
                success: function (response) {
                 
                    var options = {
                        "key": "rzp_test_HahvLMhcczzyHG", // Enter the Key ID generated from the Dashboard
                        "amount": "10000000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Daniya", //your business name
                        "description": "Test Transaction",
                        "image": "https://example.com/your_logo",
                       // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data = {
                                 "name" : name,
                                 "email" : email,
                                 "phone" : phone,
                                 "pincode" :pincode,
                                 "Address" : Address,
                                 "country" : country,
                                 //"state " : state,
                                //  "city" :city,
                                 "payment_mode" : "Paid by Razorpay",
                                 "payment_id" : responseb.razorpay_payment_id,
                                 csrfmiddlewaretoken:token
                            }
                            $.ajax({
                                method: "POST",
                                url: "/placeorder",
                                data: data,
                               
                                success: function (responsec) {
                                swal("Success!",responsec.status , "success").then((value) => {
                                  window.location.href='/my-orders'
                                  });
                                }
                            });                            
                        },
                        "prefill": {
                            "name": name, //your customer's name
                            "email": email,
                            "contact": phone,
                        },

                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                    
                }
            });
           
        }
       
    });
});


//////////

/////////
