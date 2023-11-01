$(document).ready(() => {
  const lang = $('INPUT#language_code');
  const submit = $('INPUT#btn_translate');
  const div = $('DIV#hello');

  const baseURL = 'https://hellosalut.stefanbohacek.dev/?lang=';

  submit.click(() => {
    const code = lang.val();
    const url = baseURL + code;

    fetch(url)
      .then(res => res.json())
      .then(res => div.html(res.hello))
      .catch(err => alert(err));
  });
});
