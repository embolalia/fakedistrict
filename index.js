var urlParams = new URLSearchParams(window.location.search);

var district = urlParams.get('district');
console.log(district);
if (district && district in districtData){
    var result = districtData[district];
    party = result[0]
    wonWith = result[1]
    console.log(wonWith)


    document.querySelector("#results").hidden = false;
    document.querySelector("#party").innerHTML = party;
    document.querySelector("#district").innerHTML = district;
    document.querySelector("#wonWith").innerHTML = wonWith;

    if (wonWith > .90){
        console.log("fake")
        document.querySelector("#fake").hidden = false;
    }
    else if (wonWith > .75){
        console.log("sketchy")
        document.querySelector("#sketchy").hidden = false;
    }
    else {
        console.log("real")
        document.querySelector('#real').hidden = false;
    }
} else {
    console.log(district + " is invalid")
}