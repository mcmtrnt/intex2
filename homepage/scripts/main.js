

  $(document).ready(function(){
    $('#drugBtn').click(function(){

        $.ajax({                  
            url: '/homepage/main.get_drugs/'+ $('#drugInput').val() +'/',  
               
            }).done(function(data) {
                console.log(data)
        })
        .fail(function(data) {
            console.log(data);
        });


      alert($('#drugInput').val());
    });
  });


  
  $(document).ready(function(){
    $('#prescriberBtn').click(function(){

        $.ajax({                  
            url: '/homepage/main.get_prescribers/'+ $('#prescriberInput').val() +'/',   
               
            }).done(function(data) {
                var json = jQuery.parseJSON(data);
                console.log(json)
        })
        .fail(function(data) {
            console.log("failed");
            var json = jQuery.parseJSON(data);
            console.log(json);
        });


      alert($('#prescriberInput').val());
    });
  });


