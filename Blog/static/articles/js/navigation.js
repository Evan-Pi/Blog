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
    }else{
      $('#pageUp').css({'opacity': '1'});
    }
    });

  $('#nav-tools-trigger').click(function() {
    $(this).fadeOut(200);
    $('#nav-tools').css({'visibility':'visible'}).animate({'height':'52px'},500);
    $('#nav-tools-close, #nav-tools-login ,#nav-tools-search').css({'display':'flex'});
    $('#pageUp').css({'bottom':'52px'});
  });

  $('#nav-tools-close').click(function() {
    $('#search-articles-results').fadeOut();
    $('#exit-search-articles-results').fadeOut();
    $('#search-articles-form')[0].reset();

    $('#search-articles-form').css({'visibility': 'hidden'}).animate({'width':'0%'},500);
    $('#nav-tools').animate({'height':'0%'},500);
    $('#nav-tools-close, #nav-tools-login ,#nav-tools-search').fadeOut(200);
    $('#nav-tools-trigger').fadeIn(500);
    $('#nav-tools-searchInput').css({'visibility': 'hidden'});
    $('#pageUp').css({'bottom':'0px'});

    $('html').css({'margin': '0',  'height': '100%',  'overflow': 'auto'});
  });

  $("#nav-tools-searchInput").keyup(function() {
    $("#searchButton").click();
  });


  $('#exit-search-articles-results').click(function() {
    $('html').css({'margin': '0',  'height': '100%',  'overflow': 'auto'});
    $('#search-articles-results').fadeOut();
    $(this).fadeOut();
  });




  $('#nav-tools-search').click(function() {
    $('#search-articles-results').fadeIn().css({'display':'flex'});
    $('#exit-search-articles-results').fadeIn().css({'display':'flex'});

    $('#search-articles-form').css({'visibility': 'visible'}).animate({'width':'100%'},500);
    $('#nav-tools-searchInput').css({'visibility': 'visible'}).focus();

    $('html').css({'margin': '0',  'height': '100%',  'overflow': 'hidden'});
  });

  $('#pageUp').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 500);
  });


});
