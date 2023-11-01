$(document).ready(function () {
  const div = $('div#red_header');
  const header = $('header');

  div.click(() => header.addClass('red'));
});
