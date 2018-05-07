var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
  $(document).ready(function(){
    $("#datepicker").change(function(){
      var date = $(this).val();
      var userId = $(this).val();
      $.ajax({
        type: "POST",
        url:'/tennis/listRes/',
        data:{
          'date' : '' + date
        },
        dataType: 'json',
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });
  });
  });
  $(document).ajaxComplete(function( event, request, settings ) {
    var resp = JSON.parse(request.responseJSON);
    for(i = 0;i<resp.length;i++){
      $("#resTable").append("<tr class='dataRow'> <td>"+ resp[0].fields.date +"</td> <td>"+ resp[0].fields.time +"</td> </tr>");
    }
  });
