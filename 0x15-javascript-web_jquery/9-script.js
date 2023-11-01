$(document).ready(() => {
  const div = $('DIV#hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(res => res.json())
    .then(res => div.text(res.hello))
    .catch(err => alert(err));
});
