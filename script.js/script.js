/* Melhorias de interação: tema, menu móvel e scroll suave */
const body = document.body;

// Tema (persistência)
const botao = document.getElementById('botao-tema');
function setTema(escuro){
  if (!botao) return;
  body.classList.toggle('escuro', escuro);
  botao.innerHTML = escuro ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
  botao.setAttribute('aria-pressed', escuro ? 'true' : 'false');
}
const temaSalvo = localStorage.getItem('tema');
setTema(temaSalvo === 'escuro');
if (botao) {
  botao.addEventListener('click', () => {
    const agoraEscuro = body.classList.toggle('escuro');
    setTema(agoraEscuro);
    localStorage.setItem('tema', agoraEscuro ? 'escuro' : 'claro');
  });
}

// Menu móvel
const navToggle = document.getElementById('nav-toggle');
const navList = document.querySelector('.nav-list');
if (navToggle && navList){
  navToggle.addEventListener('click', () =>{
    const aberto = navList.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', aberto ? 'true' : 'false');
  });
  // Fechar ao clicar em um link
  navList.querySelectorAll('a').forEach(a => a.addEventListener('click', ()=> navList.classList.remove('open')));
}

// Scroll suave para âncoras internas
document.querySelectorAll('a[href^="#"]').forEach(anchor =>{
  anchor.addEventListener('click', function(e){
    const href = this.getAttribute('href');
    if (!href || href === '#') return;
    const target = document.querySelector(href);
    if (target){
      e.preventDefault();
      const header = document.querySelector('header');
      const offset = header ? header.offsetHeight + 12 : 0;
      const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});
