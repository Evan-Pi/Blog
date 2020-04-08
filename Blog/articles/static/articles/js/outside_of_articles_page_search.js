
  $('#nav-tools-search').click(function() {
    $('#search-articles-results').css({'display':'flex'});
    var initialSerializedData = $("#search-articles-form").serialize();
    $.ajax({
      type: 'POST',
      url: "{% url 'ajaxArticles' %}",
      data: initialSerializedData,
      success: function(data) {
        //reset the form after successful submit
        $("#search-articles-results").html(data);
      },
      error: function(response) {
        console.log(response)
      }
    });
  });

  $('#nav-tools-close').click(function() {
    $('#search-articles-results').fadeOut();
  });

  $("#nav-tools-searchInput").keyup(function() {
    $("#searchButton").click();
  });
  $("#search-articles-form").submit(function(e) {
    // prevent from normal form behaviour
    e.preventDefault();
    // serialize the form data
    var serializedData = $(this).serialize();

    $.ajax({
      type: 'POST',
      url: "{% url 'ajaxArticles' %}",
      data: serializedData,
      success: function(data) {
        //reset the form after successful submit
        $("#search-articles-results").html(data);
      },
      error: function(response) {
        console.log(response)
      }
    });
  });
