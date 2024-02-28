/* global $ */
const doc = $(document);
doc.ready(function () {
  const redHeader = $('div#red_header');
  const header = $('header');
  redHeader.click(() => {
    header.css('color', '#FF0000');
  });
});
