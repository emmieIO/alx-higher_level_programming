/* global $ */
const doc = $(document);
doc.ready(function () {
  const header = $('header');
  const list = $('.my_list');
  const addBtn = $('DIV#add_item');
  const delBtn = $('DIV#remove_item')
  const clearBtn = $('DIV#clear_list')
  

  header.css('color', '#FF0000');
  addBtn.click(() => {
    list.append(`<li>item</li>`);
  });
  delBtn.click(()=>{
    $('.my_list li:last').remove()
  });

  clearBtn.click(()=>{
    list.empty()
  })

});
