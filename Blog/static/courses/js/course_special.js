$(document).ready(function(){

      $(window).scroll(function() {
        if ($(window).scrollTop() > $('#courseImageDiv').height()) {
          $('#social-share-desktop').css({'position': 'fixed','top': '75px',});
        }else{
          $('#social-share-desktop').css({'position': 'absolute','top': '66vh',});
        }
        });
  
  });