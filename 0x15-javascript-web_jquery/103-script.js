$(document).ready(() => {
  const lang = $('INPUT#language_code');
  const submit = $('INPUT#btn_translate');
  const div = $('DIV#hello');

  const baseURL = 'https://hellosalut.stefanbohacek.dev/?lang=';

  const translate = () => {
    const code = lang.val();
    const url = baseURL + code;

    fetch(url)
      .then(res => res.json())
      .then(res => div.html(res.hello))
      .catch(err => alert(err));
  };

  lang.keydown((event) => {
    if (event.key === 'Enter') {
      translate();
    }
  });

  submit.click(translate);
});
