async function getCovidData() {

    res = await fetch("https://disease.sh/v3/covid-19/all");
    covidJson = await res.json();

    console.log(covidJson)

    infoList = document.getElementById("covid-list")
    
    for (const info in covidJson) {
        
        infoListItem = document.createElement("li");

        infoListItem.innerHTML = `${info.toUpperCase()}: ${covidJson[info]}`
    
        infoList.appendChild( infoListItem )
    }

}

getCovidData();
