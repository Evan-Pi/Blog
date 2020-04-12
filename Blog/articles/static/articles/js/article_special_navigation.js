$(document).ready(function(){
  $(window).scroll(function() {
      if ($(window).scrollTop() > 0) {
        $('.navbar').css({'background':'white','box-shadow':'0px 0px 2px gray'});
        $('#navbar_mobile').css({'background':'white','box-shadow':'0px 0px 2px gray'});
        $('.navbar-brand').children('i').css({'color':'#44b78b'});
        $('#navbarTrigger').css({'color':'#44b78b'});
        $('.navbar .nav-link').children('span').css({'color':'#44b78b'});
        $('head').append('<style>.navbar .nav-link:hover:after {width: 100%;background: silver;}</style>');
      } else {
        $('.navbar').css({'background':'transparent','box-shadow':'none'});
        $('#navbar_mobile').css({'background':'transparent','box-shadow':'none'});
        $('#navbarTrigger').css({'color':'white'});
        $('.navbar-brand').children('i').css({'color':'white'});
        $('.navbar .nav-link').children('span').css({'color':'white'});
        $('head').append('<style>.navbar .nav-link:hover:after {width: 100%;background: white;}</style>');
      }
    });

    $('#nav-tools-search').click(function() {
      $('#nav-tools').css({'bottom':'0px'});
    });


    $('#nav-tools-trigger').click(function() {

      if ( $(window).width() > 800) {
        $('#pageUp').css({'bottom':'52px'});
        $('#nav-tools').css({'bottom':'0px'});
      }else{
        $('#pageUp').css({'bottom':'100px'});
        $('#nav-tools').css({'bottom':'52px'});
      }

    });

    $('#nav-tools-close').click(function() {
      if ( $(window).width() > 800) {
        $('#pageUp').css({'bottom':'0px'});
      }else{
        $('#pageUp').css({'bottom':'52px'});
      }
    });

    $(window).scroll(function() {
      if ($(window).scrollTop() > $('#articleImageDiv').height() - 75) {
        $('#social-share-desktop').css({'position': 'fixed','top': '75px',});
      }else{
        $('#social-share-desktop').css({'position': 'absolute','top': 'calc(66vh - 50px)',});
      }
      });

});
