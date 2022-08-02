console.log("Hello");


links = document.querySelectorAll('a');
console.log(links);
links.forEach(element => {
    element.addEventListener('click', (e) => {
        console.log(e.target.id);
        document.querySelector('.active').classList.remove('active');
        e.target.classList.add('active');
    });
});
