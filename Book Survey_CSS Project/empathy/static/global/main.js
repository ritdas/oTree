let expandedCardsBars = [];

$(function() {
    window.onscroll = function() {
        const pageYOffset = window.pageYOffset;
        expandedCardsBars.forEach(bar => {
            const card = bar.parentElement.parentElement;

            if (pageYOffset > card.getBoundingClientRect().top + window.scrollY + 50 &&
                pageYOffset < card.getBoundingClientRect().bottom + window.scrollY - 50)
            {
                bar.classList.add("sticky");
            } else {
                bar.classList.remove("sticky");
            }
        })
    }
});

document.addEventListener('mousedown', function (event) {
  if (event.detail > 1) {
    event.preventDefault();
  }
}, false);

$(".collapse").on('show.bs.collapse', function(event) {
    const categoryName = fetchCategoryName(event.target.id);
    const creditsBar = document.getElementsByName(`${categoryName} credits-bar`)[0];
    expandedCardsBars.push(creditsBar);
});

$(".collapse").on('hide.bs.collapse', function(event) {
    const categoryName = fetchCategoryName(event.target.id);
    const creditsBar = expandedCardsBars.find(e => e.attributes.name.value == `${categoryName} credits-bar`);
    creditsBar.classList.remove("sticky");
    expandedCardsBars = expandedCardsBars.filter(e => e !== creditsBar);
});

function fetchCategoryName(str) {
    const lastIndex = str.lastIndexOf(" ");
    return str.substring(0, lastIndex);
}
