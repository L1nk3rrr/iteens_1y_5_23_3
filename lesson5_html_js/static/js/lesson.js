window.onload = function () {
    let outDiv = document.getElementById("out");
    let dogAge = prompt("How old is your dog?");
    let dogYears = dogAge * 7;
    console.log(dogYears)
    let result = "Your dog is " + dogYears + " dog years old";
    outDiv.innerHTML=`<h1>${result}</h1>`;
}