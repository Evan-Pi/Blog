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
      $('#pageUp').css({'opacity': '0'});
    }else {
      $('#pageUp').css({'opacity': '1',});
    }
  });


  $('#pageUp').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 800);
  });

});
