$(document).ready(function() {

  const isFilterApplied = () => {
    let urlParams = new URLSearchParams(window.location.search);
    let filterApplied = false;

    urlParams.forEach(function(value, key) {
      if (key !== "q" && value !== "") {
        filterApplied = true;

      }
    });
    return filterApplied;
  };

  const toggleFilterVisibility = () => {
    let $filters = $(".filterable__filters");
    let urlParams = new URLSearchParams(window.location.search);
    console.log(urlParams);
    if (isFilterApplied()) {
      $filters.show();
    } else {
      $filters.hide();
    }
    $(".row>.right").append("<button id='filterToggleButton' class='button bg-gray-200 text-gray-900 '>Filters</button>");
    $("#filterToggleButton").click(function() {
      $filters.toggle();
    });
  };

  toggleFilterVisibility();
});