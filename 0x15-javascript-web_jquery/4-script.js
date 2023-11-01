$(document).ready(() => {
  const div = $('div#toggle_header');

  div.click(() => {
    const header = $('header');
    if (header.attr('class') === 'green') {
      header.attr('class', 'red');
    } else {
      header.attr('class', 'green');
    }
  });
});
