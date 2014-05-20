console.log('working');



  $('#fox #the_image').hide();
    $('#wolf #my_bad').hide();
    $('#rabbit #my_bad').hide();
    $('#fox #my_bad').hide();

$(window).load(function(){
    $('#fox #my_bad').delay(1800).fadeIn(1000).delay(1500).fadeOut(800);
    $('#fox #the_fox').delay(4500).slideUp(1500, function(){
      $('#fox #the_image').slideDown(1500);
    })
});