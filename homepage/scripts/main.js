
$(document).ready(function(){
    $('#prescriberBtn').click(function(){

        $.ajax({                  
            url: '/homepage/main.prescribers/'+ $('#prescriberInput').val() +'/',   
               
            }).done(function(data) {
              $('#doctorTable').html(data)
        })
        .fail(function(data) {
            console.log("failed");

        });


    });
  });


  $(document).ready(function(){
    $('#drugBtn').click(function(){

        $.ajax({                  
            url: '/homepage/main.drugs/'+ $('#drugInput').val() +'/',  
               
            }).done(function(data) {
              $('#drugTable').html(data)
        })
        .fail(function(data) {

        });

    });
  });


