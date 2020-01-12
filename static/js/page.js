 //Jquery for list action buttons
$( document ).ready(function(){
    $(".list-action-btn").hover(function(){
        $(this).toggleClass("list-action-btn-active");
    });

    $(".action-btn").hover(function(){
        $(this).toggleClass("action-btn-active");
    });
//JQuery for list-row
    $(".lists-list-row").hover(function(){
        $(this).toggleClass("lists-list-row-active");
        $(this).children("div").children("a").toggleClass("list-item-active");
    });
  
     //Jquery for 'back to lists' button
    $(".action-btn-back").hover(function(){
        $(this).toggleClass("action-btn-back-active");
    });
})
