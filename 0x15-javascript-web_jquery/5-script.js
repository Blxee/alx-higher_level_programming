$(document).ready(() => {
  const div = $('DIV#add_item');
  const list = $('UL.my_list');

  div.click(() => {
    list.append('<li>Item</li>');
  });
});
