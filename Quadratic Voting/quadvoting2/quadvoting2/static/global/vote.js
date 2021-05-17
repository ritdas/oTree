let pointsLeft = js_vars.totalVotes;

function btn(qName, type, category) {
    const row = document.getElementById(qName);
    const previousVotesCount = +row.getElementsByClassName(`real_value`)[0].value;
    const newVotesCount = type === 'agree' ? previousVotesCount + 1  : previousVotesCount - 1
    const card = document.getElementById(`${category} card`);

    if (isOtherDirection(newVotesCount, type) | checkPoints(card, qName)) {
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
        UpdateCost(card);
    } else {
        $('#qv-no-credits').modal('show');
    }
}

function isOtherDirection(newVotesCount, type) {
    return newVotesCount > 0 && type === 'disagree' || newVotesCount < 0 && type === 'agree';
}

function checkPoints(card, qName) {
    let pointCost = 0;
    let votes = card.getElementsByClassName('real_value');
    for (let vote of votes) {
        let value = Math.abs(parseInt(vote.value));
        if (vote.name == qName) { value += 1 }
        pointCost += value * value;
    }
    return pointsLeft - pointCost >= 0;

}

function UpdateCost(card) {
    let totalCost = 0;
    let CostLabels = card.getElementsByClassName('ncost');
    let voteCounts = card.getElementsByClassName('nvote');
    for (let index = 0; index < CostLabels.length; index++) {
        const voteCount = voteCounts[index].value
        const squaredCount = voteCount * voteCount
        CostLabels[index].innerHTML = squaredCount;
        totalCost += squaredCount;
    }
    card.getElementsByClassName("qv-credits-left")[0].innerHTML = pointsLeft - totalCost;
    setBarWidth(pointsLeft - totalCost, card);
}

function updateInnerCircleSize(row, voteCount) {
    let diam = 51 + 5.45 * (voteCount - 1);
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

function setBarWidth(w, card) {
    if (w >= 0) {
        let creditsLeftBar = card.getElementsByClassName(`credits-left-bar`)[0]
        creditsLeftBar.style.width= w + '%';
        creditsLeftBar.style.background = '#f7cf2f';
    }
}