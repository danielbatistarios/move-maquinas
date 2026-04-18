
(function(){
  /* IntersectionObserver — scroll reveal */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function(el) { io.observe(el); });
  } else {
    reveals.forEach(function(el) { el.classList.add('is-visible'); });
  }

  /* Sticky CTA — show after scrolling past hero */
  var stickyCta = document.querySelector('.sticky-cta');
  var hero = document.querySelector('.hero');
  if (stickyCta && hero) {
    function checkSticky() {
      var heroBottom = hero.getBoundingClientRect().bottom;
      if (heroBottom < 0) {
        stickyCta.classList.add('is-visible');
      } else {
        stickyCta.classList.remove('is-visible');
      }
    }
    window.addEventListener('scroll', checkSticky, { passive: true });
    checkSticky();
  }

  /* Form submit handler — handle both desktop and mobile forms */
  function handleQuoteForm(e) {
    e.preventDefault();
    var form = e.target;
    var altura = form.querySelector('[name="altura"]').value;
    var combustivel = form.querySelector('[name="combustivel"]').value;
    var prazo = form.querySelector('[name="prazo"]').value;
    var qtd = form.querySelector('[name="qtd"]').value;
    var urgencia = form.querySelector('[name="urgencia"]').value;
    var cidade = form.querySelector('[name="cidade"]').value;
    var msg = 'Olá, quero orçamento de plataforma articulada em Goiânia.\n\n';
    msg += 'Altura: ' + altura + '\n';
    msg += 'Combustível: ' + combustivel + '\n';
    msg += 'Prazo: ' + prazo + '\n';
    msg += 'Unidades: ' + qtd + '\n';
    msg += 'Urgência: ' + urgencia + '\n';
    msg += 'Cidade: ' + cidade;
    window.open('https://wa.me/5562982637300?text=' + encodeURIComponent(msg), '_blank', 'noopener,noreferrer');
  }
  var forms = document.querySelectorAll('#quoteForm, #quoteFormMobile');
  forms.forEach(function(f) { f.addEventListener('submit', handleQuoteForm); });

  /* Expandable "Ver mais" */
  document.querySelectorAll('.expand-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var target = document.getElementById(this.dataset.target);
      var isOpen = target.classList.contains('expandable--open');
      target.classList.toggle('expandable--open');
      this.classList.toggle('expand-btn--open');
      this.setAttribute('aria-expanded', !isOpen);
      if (isOpen) {
        this.innerHTML = 'Ver mais sobre plataforma articulada <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>';
      } else {
        this.innerHTML = 'Ver menos <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>';
      }
    });
  });

  /* Fleet Carousel */
  var carousel = document.getElementById('fleetCarousel');
  if (carousel) {
    var slides = carousel.querySelectorAll('.fleet-carousel__slide');
    var tabs = carousel.querySelectorAll('.fleet-carousel__tab');
    var dots = carousel.querySelectorAll('.fleet-carousel__dot');
    var current = 0;

    function goTo(index) {
      if (index < 0) index = slides.length - 1;
      if (index >= slides.length) index = 0;
      slides[current].classList.remove('fleet-carousel__slide--active');
      slides[current].hidden = true;
      tabs[current].classList.remove('fleet-carousel__tab--active');
      tabs[current].setAttribute('aria-selected', 'false');
      dots[current].classList.remove('fleet-carousel__dot--active');
      current = index;
      slides[current].classList.add('fleet-carousel__slide--active');
      slides[current].hidden = false;
      tabs[current].classList.add('fleet-carousel__tab--active');
      tabs[current].setAttribute('aria-selected', 'true');
      dots[current].classList.add('fleet-carousel__dot--active');
    }

    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() { goTo(parseInt(this.dataset.index)); });
    });
    dots.forEach(function(dot) {
      dot.addEventListener('click', function() { goTo(parseInt(this.dataset.index)); });
    });
    carousel.querySelector('.fleet-carousel__arrow--prev').addEventListener('click', function() { goTo(current - 1); });
    carousel.querySelector('.fleet-carousel__arrow--next').addEventListener('click', function() { goTo(current + 1); });

    /* Swipe support for mobile */
    var startX = 0;
    var body = carousel.querySelector('.fleet-carousel__body');
    body.addEventListener('touchstart', function(e) { startX = e.touches[0].clientX; }, { passive: true });
    body.addEventListener('touchend', function(e) {
      var diff = startX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) { goTo(diff > 0 ? current + 1 : current - 1); }
    }, { passive: true });
  }

  /* Scroll progress bar */
  var progressBar = document.querySelector('.scroll-progress');
  if (progressBar) {
    window.addEventListener('scroll', function() {
      var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
      var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var progress = (scrollTop / scrollHeight) * 100;
      progressBar.style.width = progress + '%';
    }, { passive: true });
  }
})();
