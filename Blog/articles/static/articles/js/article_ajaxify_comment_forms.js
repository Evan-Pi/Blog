//COMMENT FORM
$("#createCommentForm").submit(function(e) {
  // prevent from normal form behaviour
  e.preventDefault();
  // serialize the form data
  var serializedData = $(this).serialize();
  $.ajax({
    type: 'POST',
    url: "{% url 'ajaxComments' article.slug %}",
    data: serializedData,
    success: function(data) {
      //reset the form after successful submit
      $("#ajaxCommentsContainer").html(data);
    },
    error: function(response) {
      console.log(response)
    }
  });
  $("#createCommentForm")[0].reset();
  $('#commentsModal').modal('hide');
});

//SUBCOMMENT FORM
$("#createSubCommentForm").submit(function(e) {
  // prevent from normal form behaviour
  e.preventDefault();
  // serialize the form data
  var serializedData = $(this).serialize();
  $.ajax({
    type: 'POST',
    url: "{% url 'ajaxComments' article.slug %}",
    data: serializedData,
    success: function(data) {
      //reset the form after successful submit
      $("#ajaxCommentsContainer").html(data);
    },
    error: function(response) {
      console.log(response)
    }
  });
  $("#createSubCommentForm")[0].reset();

  $('#subcommentsModal').modal('hide');

});

$("#createSubCommentForm")[0].reset();
$("#createCommentForm")[0].reset();
$('.selectComment').click(function() {
  $("#createSubCommentForm")[0].reset();
  btnValue = $(this).val();
  console.log(btnValue);
  $('#id_comment').val(btnValue).trigger('change');
});
