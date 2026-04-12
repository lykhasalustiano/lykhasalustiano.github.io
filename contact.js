emailjs.init("YOUR_PUBLIC_KEY");

function sendEmail() {
  const btn = document.getElementById('send-btn');
  btn.textContent = 'Sending...';
  btn.disabled = true;

  emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', '#contact-form')
    .then(() => {
      btn.textContent = 'Sent!';
      document.getElementById('contact-form').reset();
      setTimeout(() => {
        btn.textContent = 'Send';
        btn.disabled = false;
      }, 3000);
    })
    .catch((error) => {
      console.error(error);
      btn.textContent = 'Failed. Try again.';
      btn.disabled = false;
    });
}