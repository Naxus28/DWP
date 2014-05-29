console.log("gabriel's js is working");


$('#arrow').hide();
$('#alert').hide(function(){
     $(this).delay(4000).fadeIn(2000, function(){
        $(this).delay(3000).fadeOut(2000);
     });
});

$('.img-container,.img-container img,.picture_container').draggable({scroll:false});

$(window).load(function(){
    if($('h2').offset()){
        $('html,body').animate({scrollTop: $('h2').offset().top},1800, function(){
             $(window).scroll(function() {
                  var screen = $(window).scrollTop();
                  if ($(this).scrollTop() < $(this).height()+100){
                        $('#arrow').fadeOut();
                  }
                  else{
                        $('#arrow').fadeIn();
                  }
             });
        });
    }

    var counter = 2;
    $('.img-container').mousedown(function(){
         $(this).css('z-index',counter);
         $('form, h1').css('z-index',counter);
         $(this).hover(function(){
                $(this).css('outline','1px solid white');
            }, function(){
                $(this).css('outline','none');
            })
          counter ++
    });
    if($('h2').offset()){
        $('#arrow').click(function(){
            $('html,body').animate({scrollTop: $('h2').offset().top},3000);
        });
    }

    $('.img-container img').mousedown(function(){
         $(this).css('opacity',1);
    });



    var counter_one = 2;
    $('.picture_container').mousedown(function(){
         $(this).css('z-index',counter_one);
         $('#arrow').css('z-index',counter_one);
         counter_one ++
    });
});
