$(document).ready(function(){
    $('#seeRelated').click(function(){

        $.ajax({                  
            url: '/homepage/prescriberDetails.related/' + $('#prescriberInput').val() +'/',   
               
            }).done(function(data) {
                console.log("done");

              $('#relatedDoctors').html(data);
        })
        .fail(function(data) {
            console.log("failed");

        });


    });
  });