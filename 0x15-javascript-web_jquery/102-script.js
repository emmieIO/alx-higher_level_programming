/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');
  const code = $('INPUT#language_code');
  const submit = $('INPUT#btn_translate');

  header.css('color', '#FF0000');
  submit.click(()=>{
    if(code.val() !== ""){
        $.ajax({
          url: 'https://hellosalut.stefanbohacek.dev/?lang='+code.val(),
          method: 'GET',
          dataType: 'JSON',
          success: (data) => {
            $('#hello').text(data.hello);
          },
          error: (xhr, status, error) => {
            console.log(status, error);
          }
        });
    }else{
        $('#hello').text("Wrong Language code");
    }
  })
});