$(document).ready(function(){
    $('#seeRelated').click(function(){

        $.ajax({                  
            url: '/homepage/drugDetails.related/' + $('#drugInput').val() +'/',   
               
            }).done(function(data) {
                console.log("done");

              $('#relatedDrugs').html(data);
        })
        .fail(function(data) {
            console.log("failed");

        });


    });
  });