document.addEventListener('DOMContentLoaded', () => {
    // Инициализация AOS для анимаций при скролле
    AOS.init({
      duration: 1000, // Длительность анимации в миллисекундах
      once: true, // Анимация проигрывается только один раз
    });
  
    // FAQ Аккордеон: обработка кликов по вопросам
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      const question = item.querySelector('.faq-question');
      question.addEventListener('click', () => {
        // Закрываем все открытые ответы
        faqItems.forEach(i => {
          if (i !== item) {
            i.classList.remove('active');
          }
        });
        // Переключаем состояние текущего вопроса
        item.classList.toggle('active');
      });
    });
  
    // Модальные окна для секции "Функции"
    window.openModal = (modalId) => {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.style.display = 'block'; // Открываем модальное окно
      }
    };
  
    window.closeModal = (modalId) => {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.style.display = 'none'; // Закрываем модальное окно
      }
    };
  
    // Чат-бот: открытие и закрытие окна
    window.openChat = () => {
      const chatWindow = document.querySelector('.chat-window');
      if (chatWindow) {
        chatWindow.style.display = 'block'; // Открываем окно чат-бота
      }
    };
  
    window.closeChat = () => {
      const chatWindow = document.querySelector('.chat-window');
      if (chatWindow) {
        chatWindow.style.display = 'none'; // Закрываем окно чат-бота
      }
    };
  
    // Валидация формы логина
    const loginForm = document.querySelector('.login-form');
    if (loginForm) {
      loginForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Предотвращаем отправку формы (для демонстрации)
        const email = loginForm.querySelector('input[type="email"]').value;
        const password = loginForm.querySelector('input[type="password"]').value;
  
        // Простая проверка email и пароля
        if (!email.includes('@') || email.length < 5) {
          alert('Пожалуйста, введите корректный email.');
          return;
        }
        if (password.length < 6) {
          alert('Пароль должен содержать минимум 6 символов.');
          return;
        }
        alert('Вход выполнен успешно! (демо)');
      });
    }
  
    // Валидация формы регистрации
    const registerForm = document.querySelector('.register-form');
    if (registerForm) {
      registerForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Предотвращаем отправку формы (для демонстрации)
        const name = registerForm.querySelector('input[type="text"]').value;
        const email = registerForm.querySelector('input[type="email"]').value;
        const password = registerForm.querySelector('input[type="password"]').value;
  
        // Проверка полей
        if (name.length < 2) {
          alert('Имя должно содержать минимум 2 символа.');
          return;
        }
        if (!email.includes('@') || email.length < 5) {
          alert('Пожалуйста, введите корректный email.');
          return;
        }
        if (password.length < 6) {
          alert('Пароль должен содержать минимум 6 символов.');
          return;
        }
        alert('Регистрация выполнена успешно! (демо)');
      });
    }
  
    // Плавный скролл к секциям при клике на навигацию
    const navLinks = document.querySelectorAll('.nav a');
    navLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href.startsWith('#')) {
          e.preventDefault();
          const sectionId = href.substring(1);
          const section = document.getElementById(sectionId);
          if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
          }
        }
      });
    });
  });