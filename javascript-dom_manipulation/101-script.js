document.addEventListener('DOMContentLoaded', (event) => {
  const btnTranslate = document.querySelector('#btn_translate');
  const languageCodeInput = document.querySelector('#language_code');

  function translate () {
    const languageCode = languageCodeInput.value;
    // Updated API URL as per instructions
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
    fetch(url)
      .then(response => response.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      })
      .catch(error => console.error('Error:', error));
  }

  btnTranslate.addEventListener('click', translate);
});
