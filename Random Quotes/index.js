var currentQuote = '',
    currentAuthor = '';
var quotesData;

var colors = [
    '#16a085',
    '#27ae60',
    '#2c3e50',
    '#f39c12',
    '#e74c3c',
    '#9b59b6',
    '#FB6964',
    '#342224',
    '#472E32',
    '#BDBB99',
    '#77B1A9',
    '#73A857'
];
$(".container").css({
    backgroundColor: colors[0],
    color: colors[0],
});
$(".new-quote").css({
    backgroundColor: colors[0],
});

const getQuotes = () => {
    return $.ajax({
        headers: {
            Accept: 'application/json',
        },
        url: 'https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json',
        success: (data) => {
            if (typeof data === 'string') {
                quotesData = JSON.parse(data);
            }
        },
    });
}
const getRandomQuote = () => {
    const randomIndex = Math.floor(Math.random() * quotesData.quotes.length - 1);
    const randomQuoteDetails = quotesData.quotes[randomIndex];
    return randomQuoteDetails;
}

const getQuote = () => {
    const randomQuote = getRandomQuote();
    currentQuote = randomQuote.quote;
    currentAuthor = randomQuote.author;

    $('.tweet-quote').attr('href', 'https://twitter.com/intent/tweet?text=' + encodeURIComponent('"' + currentQuote + '"' + '-' + currentAuthor));
    $('.text').animate({
        opacity: 0
    }, 500, function() {
        $(this).animate({
            opacity: 1
        }, 500);
    });
    $('#quoteText').html(randomQuote.quote);

    $('.author').animate({
        opacity: 0
    }, 500, function() {
        $(this).animate({
            opacity: 1
        }, 500);
    });
    $('#quoteAuthor').html(currentAuthor);

    var color = Math.floor(Math.random() * colors.length - 1);

    $('.tweet-quote').css({
        color: colors[color]
    });
    $('.container').css({
        backgroundColor: colors[color],
        color: colors[color],
    });
    $('.new-quote').css({
        backgroundColor: colors[color]
    });
}

$(document).ready(() => {
    getQuotes().then(() => {
        getQuote();
    });
    $('.new-quote').on('click', getQuote);
})