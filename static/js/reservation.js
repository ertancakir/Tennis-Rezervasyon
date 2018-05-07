var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
  $(document).ready(function(){

    

    $("#datepicker").change(function(){
      document.getElementById("timepicker").options.length = 0;
      var date = $(this).val();
      $("#dateFormPicker").val(date);
      $.ajax({
        type: "POST",
        url:'datePick/',
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
  $( document ).ajaxComplete(function( event, request, settings ) {

    for(i = 8;i < 20;i++){
      var tmp = "";
      if(i < 10){
        tmp = "0" + i + ":" + "00";
      }
      else{
        tmp = i + ":00";
      }
      var resp = JSON.parse(request.responseJSON);
      resp.forEach(function(r){
        if(r.time == tmp){
          tmp = 'n';
        }
      });
      if(tmp != 'n'){
        $("#timepicker").append("<option value = "+ tmp +">" + tmp + "</option>");
      }
    }
  });
