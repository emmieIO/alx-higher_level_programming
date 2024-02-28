/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');

  header.css('color', '#FF0000');
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'JSON',
    success: (data) => {
      data.results.forEach(movie => {
        $('UL#list_movies').append(`<li>${movie.title}</li>`);
      });
    },
    error: (xhr, status, error) => {
      console.log(status, error);
    }
  });
});
