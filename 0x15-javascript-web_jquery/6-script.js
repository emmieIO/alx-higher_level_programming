/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');
  const updateBtn = $('DIV#update_header');

  header.css('color', '#FF0000');
  updateBtn.click(() => {
    header.text('New Header!!!');
  });
});
