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
    }else if($('#nav-tools-trigger').is(":hidden")){
      $('#pageUp').css({'opacity': '1','bottom':'52px'});
    }else {
      $('#pageUp').css({'opacity': '1','bottom':'0px'});
    }
  });

  $('#nav-tools-trigger').click(function() {
    $(this).fadeOut(200);
    $('#nav-tools').css({'visibility':'visible'}).animate({'height':'52px'},400);
    $('#nav-tools-close, #nav-tools-login ,#nav-tools-search').css({'display':'flex'});

    $('#pageUp').css({'bottom':'52px'});
  });

  $('#nav-tools-close').click(function() {
    $('#nav-tools').animate({'height':'0%'},400);
    $('#nav-tools-close, #nav-tools-login ,#nav-tools-search').fadeOut(200);
    $('#nav-tools-trigger').delay(400).fadeIn(400);

    $('#search-articles-form').css({'visibility': 'hidden'}).delay(400).animate({'width':'0%'});
    $('#nav-tools-searchInput').css({'visibility': 'hidden'});

    $('#pageUp').css({'bottom':'0px'});
  });


  $('#nav-tools-search').click(function() {
    $('#search-articles-form').css({'visibility': 'visible',}).animate({'width':'100%'});
    $('#nav-tools-searchInput').css({'visibility': 'visible',}).focus();
  });


  $('#pageUp').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 400);
  });


});
