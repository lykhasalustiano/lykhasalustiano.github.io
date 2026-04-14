emailjs.init("OdHFi_Pn_k_JDa--S");

function sendEmail() {
  const btn = document.getElementById('send-btn');
  btn.textContent = 'Sending...';
  btn.disabled = true;

  emailjs.sendForm('service_47t8crr', 'template_m7shxqd', '#contact-form')
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