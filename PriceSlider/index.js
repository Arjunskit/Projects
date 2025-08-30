let minPrize = document.getElementById('minPrize');
let maxPrize = document.getElementById('maxPrize');
let minRangeSlider = document.getElementById('minRangeSlider');
let maxRangeSlider = document.getElementById('maxRangeSlider');
let priceSlider = document.getElementById('priceSlider');




minPrize.addEventListener('input', () => {
    let leftValue = (minPrize.value / 10000) * 100;
    minRangeSlider.value = minPrize.value;
    priceSlider.style.left = `${leftValue}%`;
})

maxPrize.addEventListener('input', () => {
    let rightValue = 100 - (maxPrize.value / 10000) * 100;
    maxRangeSlider.value = maxPrize.value;
    priceSlider.style.right = `${rightValue}%`;
})


minRangeSlider.addEventListener('input', () => {
    console.log('min value', minRangeSlider.value);
    let leftValue = (minRangeSlider.value / 10000) * 100;
    priceSlider.style.left = `${leftValue}%`;
    minPrize.value = minRangeSlider.value;

})


maxRangeSlider.addEventListener('input', () => {
    console.log('max value', maxRangeSlider.value);
    let rightValue = 100 - (maxPrize.value / 10000) * 100;
    priceSlider.style.right = `${rightValue}%`;
    maxPrize.value = maxRangeSlider.value;
})