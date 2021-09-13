const seeMoreButton = document.querySelectorAll('.see-details');
const seeMoreButtons = Array.from(seeMoreButton)

const toggleExtraInfo = (e) => {

    const article = e.target.closest('article')

    const seeMoreSection = article.querySelector('.more-info')
   
    if (seeMoreSection.style.height == '0px' || !seeMoreSection.style.height) {
        seeMoreSection.style.height = 'auto'
    } else {
        seeMoreSection.style.height = '0px'
    }
}

seeMoreButtons.forEach(button => {
    button.addEventListener('click', toggleExtraInfo)
});
