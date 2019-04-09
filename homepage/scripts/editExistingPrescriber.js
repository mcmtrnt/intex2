$(document).ready(function(){
    $('#prescriberBtn').click(function(){

        $.ajax({                  
            url: '/homepage/editExistingPrescriber.prescribers/'+ $('#prescriberInput').val() +'/',   
               
            }).done(function(data) {
              $('#prescriberList').html(data)
        })
        .fail(function(data) {
            console.log("failed");

        });


    });
  });