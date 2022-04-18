HOST_URL = "http://127.0.0.1:8000/"
$('#click_me').on('click', function(){


    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: HOST_URL + 'home/run/',
        data: {
          'input_user_name': "AbdulHesen",
        },
        success: (response_data) => {
            console.log("cavab= ",response_data['answer'])
            $('#hello_text').text("Hello world!")
        
        },
        error: function (err) {
           console.log('xetali: ', err)
        },
    
      });
         

})
