const fs = require('fs');

function getTemperatures(filename) {
  let file = fs.readFileSync(filename, 'utf-8');
  let rows = file.split('\n');

  let headerParts = rows[0].split(' ');

  let countries = [];

  // The last element of headerParts is skipped from the loop
  // (it's "Year" and not a country name)
  for (let countryIndex = 0; countryIndex < headerParts.length - 1; countryIndex++) {
    countries[countryIndex] = { name: headerParts[countryIndex] };
  }

  // The 1st row is skipped from the loop (it's the header)
  for (let rowIndex = 1; rowIndex < rows.length; rowIndex++) {
    let rowParts = rows[rowIndex].split(' ');

    // The last column contains the year
    let currentYear = rowParts[rowParts.length - 1];

    // The last element of rowParts is skipped from the loop (it's the current year)
    for (let countryIndex = 0; countryIndex < rowParts.length - 1; countryIndex++) {
      let currentCountry = countries[countryIndex];
      let currentTemperature = rowParts[countryIndex];

      if (currentCountry.warmest === undefined ||
          currentCountry.warmest.temperature < currentTemperature) {
        currentCountry.warmest = {
          temperature: currentTemperature,
          year: currentYear,
        };
      }

      if (currentCountry.coldest === undefined ||
          currentCountry.coldest.temperature > currentTemperature) {
        currentCountry.coldest = {
          temperature: currentTemperature,
          year: currentYear,
        };
      }
    }
  }

  let outputLines = countries.map(country =>
    `${country.name} => ${country.coldest.year}, ${country.warmest.year}`);
  return outputLines.join('\n');
}

console.log(getTemperatures('2.txt'));
