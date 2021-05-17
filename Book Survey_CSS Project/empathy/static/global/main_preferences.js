$(function () {
    let qvBar = document.getElementById("qv-credits-bar");
    let top = qvBar.offsetTop;
    window.onscroll = function() {
        if (document.getElementById('chardin-mask') === null && window.pageYOffset > top) {
            qvBar.classList.add("sticky");
        } else {
            qvBar.classList.remove("sticky");
        }
    };
});

document.addEventListener('mousedown', function (event) {
  if (event.detail > 1) {
    event.preventDefault();
  }
}, false);
