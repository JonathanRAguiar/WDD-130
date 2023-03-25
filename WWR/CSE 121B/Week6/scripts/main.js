// toggle menu in small view
const toggleMenu = () => {
    document.querySelector('#menu').classList.toggle('open');
}

document.querySelector('#toggleMenu').addEventListener('click', toggleMenu);

const currentDate = new Date();
document.querySelector('#year').textContent = currentDate.getFullYear();