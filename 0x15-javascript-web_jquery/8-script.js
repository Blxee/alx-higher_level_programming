$(document).ready(() => {
  const list = $('UL#list_movies');

  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(res => res.json())
    .then(res => {
      for (const movie of res.results) {
        list.append(`<li>${movie.title}</li>`);
      }
    })
    .catch(err => alert(err));
});
