document.addEventListener('DOMContentLoaded',function(){

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length == 2) return parts.pop().split(';').shift();
    }

    document.querySelector("#contact-form").onsubmit = () =>{
        const name = document.querySelector('#name').value;
        const email = document.querySelector('#email').value;
        const message = document.querySelector('#message').value;
         fetch("/contact",{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
              name: name,
              email: email,
              message: message
            })
         })
         .then(response => response.json())
         .then(result => {
            document.querySelector('#name').value = '';
            document.querySelector('#email').value = '';
            document.querySelector('#message').value = '';
            console.log(result);
         })
        return false;
      }
    });