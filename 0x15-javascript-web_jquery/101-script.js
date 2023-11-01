$(document).ready(() => {
  const list = $('UL.my_list');

  const fun = function () {
    switch ($(this).attr('id')) {
      case 'add_item':
        list.append('<li>Item</li>');
        break;

      case 'remove_item':
        list.find('li:last').remove();
        break;

      case 'clear_list':
        list.html('');
        break;
    }
  };

  $('DIV#add_item').click(fun);
  $('DIV#remove_item').click(fun);
  $('DIV#clear_list').click(fun);
});
