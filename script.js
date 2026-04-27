document.addEventListener('DOMContentLoaded', () => {
  // Modal Contactos
  const contactModal = document.getElementById('contact-modal');
  document.getElementById('open-contact')?.addEventListener('click', () => contactModal.classList.add('active'));
  document.getElementById('close-contact')?.addEventListener('click', () => contactModal.classList.remove('active'));
  contactModal?.addEventListener('click', e => {
    if (e.target === contactModal) contactModal.classList.remove('active');
  });

  // Modal Redes Sociais
  const socialModal = document.getElementById('social-modal');
  document.getElementById('open-socials')?.addEventListener('click', () => socialModal.classList.add('active'));
  document.getElementById('close-socials')?.addEventListener('click', () => socialModal.classList.remove('active'));
  socialModal?.addEventListener('click', e => {
    if (e.target === socialModal) socialModal.classList.remove('active');
  });
});
