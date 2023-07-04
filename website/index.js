const counter = document.querySelector('.counternumber')
async function updateCounter() {
    let response = await fetch('https://yqfiuzhtjegpcxguljv3nf3oxi0ilbry.lambda-url.us-east-1.on.aws/');
    let data = await response.json();
    counter.innerHTML = ` views: ${data}`;
}

updateCounter()