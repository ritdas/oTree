let pointsLeft = js_vars.totalVotes;


function btn(qId, type) {
    const row = document.getElementById(qId);
    const previousVotesCount = +row.getElementsByClassName(`real_value`)[0].value;
    const newVotesCount = type === 'agree' ? previousVotesCount + 1  : previousVotesCount - 1
    const squaredNewVotesCount = Math.pow(newVotesCount, 2);
    const absSquareDifference = squaredNewVotesCount - Math.pow(previousVotesCount, 2);

    if (isOtherDirection(newVotesCount, type) || enoughPoints(absSquareDifference)) {
        updateInnerCircleSize(row, Math.abs(newVotesCount));

        if (newVotesCount !== 0) {
            const realVotesPositive = newVotesCount >= 0;
            const nameType = realVotesPositive ? "agree" : "disagree";
            const backgroundColor = realVotesPositive ? '#53bb33' : 'orangered'
            updateCircleStyles(row, nameType, backgroundColor);
        } else {
            resetCircleStyles(row);
        }

        row.getElementsByClassName(`real_value`)[0].value = newVotesCount;
        row.getElementsByClassName('nvote')[0].value = Math.abs(newVotesCount);
        updateVotesHtmls(row, squaredNewVotesCount, absSquareDifference);
    } else {
        $('#qv-no-credits').modal('show');
    }
}

function isOtherDirection(newVotesCount, type) {
    return newVotesCount > 0 && type === 'disagree' || newVotesCount < 0 && type === 'agree';
}

function enoughPoints(absSquareDifference) {
    return pointsLeft - absSquareDifference >= 0;
}

function updateVotesHtmls(row, squaredNewVotesCount, absSquareDifference) {
    row.getElementsByClassName('ncost')[0].innerHTML = squaredNewVotesCount;
    pointsLeft -= absSquareDifference;
    document.getElementById("qv-credits-left").innerHTML = pointsLeft;
    setBarWidth(pointsLeft);
}

function updateInnerCircleSize(row, newVotesCount) {
    let diam = 51 + 5.45 * (newVotesCount - 1);
    let topLeft = (100 - diam) / 2;
    diam += '%';
    topLeft += '%';
    let innerCircle = row.getElementsByClassName('vote-inner-circle')[0]
    innerCircle.style.width = diam;
    innerCircle.style.height = diam;
    innerCircle.style.top = topLeft;
    innerCircle.style.left = topLeft
}

function updateCircleStyles(row, type, backgroundColor) {
    row.getElementsByClassName('nvote')[0].style.background = backgroundColor;
    row.getElementsByClassName('vote-inner-circle')[0].style.background = backgroundColor;
    row.getElementsByClassName(`qv-${type}`)[0].style.visibility = 'visible';
}

function resetCircleStyles(row) {
    row.getElementsByClassName('nvote')[0].style.background = '#e8e8e8'
    row.getElementsByClassName('qv-agree')[0].style.visibility ='hidden';
    row.getElementsByClassName('qv-disagree')[0].style.visibility = 'hidden';
}

function setBarWidth(w) {
    if (w >= 0) {
        let creditsLeftBar = document.getElementById(`qv-credits-left-bar`)
        creditsLeftBar.style.width= w + '%';
        creditsLeftBar.style.background = '#f7cf2f';
    }
}

document.addEventListener('mousedown', function (event) {
    if (event.detail > 1) {
        event.preventDefault();
    }
}, false);
