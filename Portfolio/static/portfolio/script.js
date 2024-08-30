document.addEventListener('DOMContentLoaded', function () {
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  document.querySelector("#contact-form").onsubmit = () => {
      const name = document.querySelector('#name').value;
      const email = document.querySelector('#email').value;
      const message = document.querySelector('#message').value;
      fetch("/contact", {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token
          },
          body: JSON.stringify({
              name: name,
              email: email,
              message: message
          })
      })
      .then(response => {
          if (response.ok) {
              return response.json();
          } else {
              return response.text().then(text => { throw new Error(text); });
          }
      })
      .then(result => {
          document.querySelector('#name').value = '';
          document.querySelector('#email').value = '';
          document.querySelector('#message').value = '';
          console.log(result);
      })
      .catch(error => console.error('Error:', error));

      return false;
  }
});
