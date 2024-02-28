/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');

  header.css('color', '#FF0000');
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'JSON',
    success: (data) => {
      $('#hello').text(data.hello);
    },
    error: (xhr, status, error) => {
      console.log(status, error);
    }
  });
});
