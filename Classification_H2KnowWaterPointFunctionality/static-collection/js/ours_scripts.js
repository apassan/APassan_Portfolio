document.addEventListener('DOMContentLoaded', function() {
  // Retrieve the dropdown element
  var countryDropdown = document.getElementById('country-dropdown');
  
  // Event listener for country dropdown change
  countryDropdown.addEventListener('change', function() {
    var country = countryDropdown.value;

    // Make an AJAX request to the backend
    fetch('/search/?country=' + country)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        // Handle the response data
        var resultContainer = document.getElementById('result-container');
        resultContainer.textContent = 'Result: ' + data.result;
      })
      .catch(function(error) {
        console.log('An error occurred:', error);
      });
  });
  
  // Event listener for form submission
  document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    var country = countryDropdown.value;

    // Make an AJAX request to the backend
    fetch('/search/?country=' + country)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        // Handle the response data
        var resultContainer = document.getElementById('result-container');
        resultContainer.textContent = 'Result: ' + data.result;
      })
      .catch(function(error) {
        console.log('An error occurred:', error);
      });
  });

  // Retrieve the dropdown data from the cached file or any other source
  // Modify the following lines to fetch the data as per your specific requirements
  fetch('/static/h2know/dropdown_data.json')
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      // Populate the country dropdown menu
      populateDropdown(countryDropdown, data.countries);
    })
    .catch(function(error) {
      console.log('An error occurred:', error);
    });

  // Function to populate the country dropdown menu
  function populateDropdown(dropdown, data) {
    data.forEach(function(item) {
      var option = document.createElement('option');
      option.value = item;
      option.textContent = item;
      dropdown.appendChild(option);
    });
  }
});