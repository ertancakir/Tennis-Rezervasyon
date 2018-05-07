var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
  $(document).ready(function(){
    $(".btnRes").click( function(){
      $(".dataRow").remove();
      var userId = $(this).val();
      $.ajax({
        type: "POST",
        url:'/tennis/admin/',
        data:{
          'userId' : '' + userId
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
      console.log(resp[0].fields);
      $("#resTable").append("<tr class='dataRow'> <td>"+ resp[0].fields.date +"</td> <td>"+ resp[0].fields.time +"</td></tr>");
    }
  });
