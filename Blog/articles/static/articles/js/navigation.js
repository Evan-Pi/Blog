$(document).ready(function() {
  $('#navbarTrigger').click(function() {
    $('#sidebarWrapper , #sidebar').fadeIn(600);
    $('html').css({'margin': '0',  'height': '100%',  'overflow': 'hidden'});
  });

  $('#sidebarWrapper').click(function() {
    $('#sidebarWrapper , #sidebar').fadeOut(600);
    $('html').css({'margin': '0',  'height': '100%',  'overflow': 'auto'});
  });

  $('#closeSidebar').click(function() {
    $('#sidebarWrapper , #sidebar').fadeOut(600);
    $('html').css({'margin': '0',  'height': '100%',  'overflow': 'auto'});
  });


  $(window).scroll(function() {
    if ($(window).scrollTop() < $(window).height()) {
      $('#pageUp').css({'opacity': '0','bottom':'52px'});
    }else if($('#mobile-navigation-tools-trigger').is(":hidden")){
      $('#pageUp').css({'opacity': '1','bottom':'52px'});
    }else {
      $('#pageUp').css({'opacity': '1','bottom':'0px'});
    }
  });

  $('#mobile-navigation-tools-trigger').click(function() {
    $(this).fadeOut(200);
    $('#mobile-navigation-tools').css({'visibility':'visible'}).animate({'height':'52px'},400);
    $('#mobile-navigation-tools-close, #mobile-navigation-tools-login ,#mobile-navigation-tools-search').css({'display':'flex'});

    $('#pageUp').css({'bottom':'52px'});
  });

  $('#mobile-navigation-tools-close').click(function() {
    $('#mobile-navigation-tools').animate({'height':'0%'},400);
    $('#mobile-navigation-tools-close, #mobile-navigation-tools-login ,#mobile-navigation-tools-search').fadeOut(200);
    $('#mobile-navigation-tools-trigger').delay(400).fadeIn(400);

    $('#pageUp').css({'bottom':'0px'});
  });


  $('#pageUp').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 400);
  });


});
