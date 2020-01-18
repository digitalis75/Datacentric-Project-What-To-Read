$( document ).ready(function(){
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
