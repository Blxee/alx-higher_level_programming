$(document).ready(() => {
  const div = $('DIV#character');

  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(res => res.json())
    .then(res => div.text(res.name))
    .catch(err => alert(err));
});
