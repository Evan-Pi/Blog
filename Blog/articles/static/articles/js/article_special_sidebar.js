$(document).ready(function(){
  $(window).scroll(function() {
      if ($(window).scrollTop() > 0) {
        $('.navbar').css({'background':'white','box-shadow':'0px 0px 2px gray'});
        $('#navbar_mobile').css({'background':'white','box-shadow':'0px 0px 2px gray'});
        $('.navbar-brand').children('i').css({'color':'#44b78b'});
        $('#navbarTrigger').css({'color':'#44b78b'});
        $('.nav-link').children('span').css({'color':'#44b78b'});
      } else {
        $('.navbar').css({'background':'transparent','box-shadow':'none'});
        $('#navbar_mobile').css({'background':'transparent','box-shadow':'none'});
        $('#navbarTrigger').css({'color':'white'});
        $('.navbar-brand').children('i').css({'color':'white'});
        $('.nav-link').children('span').css({'color':'white'});
      }
    });
});
