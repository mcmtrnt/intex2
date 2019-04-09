$(document).ready(function(){
    $('#prescriberBtn').click(function(){

        $.ajax({                  
            url: '/homepage/editPrescribers.prescribers/'+ $('#prescriberInput').val() +'/',   
               
            }).done(function(data) {
              $('#prescriberList').html(data)
        })
        .fail(function(data) {
            console.log("failed");

        });


    });
  });