/* global $ */
const doc = $(document);
doc.ready(function () {
  $('div#red_header').click(() => {
    $('header').addClass('red');
  });
});
