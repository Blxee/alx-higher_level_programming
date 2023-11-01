$(document).ready(() => {
  const div = $('DIV#update_header');
  const header = $('header');

  div.click(() => header.text('New Header!!!'));
});
