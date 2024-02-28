/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');
  const list = $('.my_list');
  const addBtn = $('DIV#add_item');
  let count = 1;

  header.css('color', '#FF0000');
  addBtn.click(() => {
    list.append(`<li>item ${count++}</li>`);
  });
});
