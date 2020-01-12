 //Jquery for action buttons
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
})   