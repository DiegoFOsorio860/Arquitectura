function changeBackground(input) {
    var email = input.value;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var isValid = emailRegex.test(email);
  
    if (isValid) {
      input.style.backgroundColor = 'green';
    } else {
      input.style.backgroundColor = 'red';
    }
  }