$(document).ready(function(){

      $(window).scroll(function() {
        if ($(window).scrollTop() > $('#courseImageDiv').height()) {
          $('#social-share-desktop').css({'position': 'fixed','top': '75px',});
        }else{
          $('#social-share-desktop').css({'position': 'absolute','top': '66vh',});
        }
      });

      

      $('#modules-menu-trigger').click(function(){

        

        if( $('#modules-menu').is(":visible") ){
          $('#modules-menu-wrapper').fadeOut();
          $('#modules-menu').fadeOut();
          $(this).animate({'right':'0'}).css({'background-color':'rgba(255, 255, 255, 0.9)'});
          $('#edit-course').animate({'right':'0'}).css({'background-color':'rgba(255, 255, 255, 0.9)'});
          
          
          $('#modules-menu-trigger').css({'box-shadow':'0px 0px 10px silver'});

          $('#modules-menu-close').hide();
          $('#modules-menu-open').fadeIn();
        }else{
          $('#modules-menu-wrapper').fadeIn();
          $('#modules-menu').fadeIn();
          $(this).animate({'right':$('#modules-menu').width()}).css({'background-color':'#fff'});
          $('#edit-course').animate({'right':$('#modules-menu').width()}).css({'background-color':'#fff'});
          
          $('#modules-menu-trigger').css({'box-shadow':'none'});

          $('#modules-menu-open').hide();
          $('#modules-menu-close').fadeIn();
          
        }
      });

      $('#modules-menu-wrapper').click(function(){
          $('#modules-menu-wrapper, #modules-menu').fadeOut();
          $('#modules-menu-trigger').animate({'right':'0'}).css({'background-color':'rgba(255, 255, 255, 0.9)','box-shadow':'0px 0px 10px silver'});
          $('#edit-course').animate({'right':'0'}).css({'background-color':'rgba(255, 255, 255, 0.9)'});
          $('#modules-menu-close').hide();
          $('#modules-menu-open').fadeIn();
      });
      
      $(window).scroll(function() {
        if ($(window).scrollTop() > $('#courseImageDiv').height()) {
          $('#social-share-desktop').css({'position': 'fixed','top': '75px',});
        }else{
          $('#social-share-desktop').css({'position': 'absolute','top': '66vh',});
        }
      });

  });