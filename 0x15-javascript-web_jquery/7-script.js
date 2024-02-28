/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');

  header.css('color', '#FF0000');
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'JSON',
    success: (data) => {
      $('DIV#character').text(data.name);
    },
    error: (xhr, status, error) => {
      console.log(status, error);
    }
  });
});
