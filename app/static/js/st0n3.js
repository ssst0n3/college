$(document).ready(function(){
  $(".pull-down").click(function(){
    $(".navi").slideToggle("slow");
    // console.log($(".navi").attr("style"));
    if ($(".navi").css("height")=="1px"){
      $(".pull-down img").attr("style","transform:rotate(180deg);-ms-transform:rotate(180deg); /* IE 9 */-moz-transform:rotate(180deg); /* Firefox */-webkit-transform:rotate(180deg); /* Safari 和 Chrome */-o-transform:rotate(180deg); /* Opera */");
    }else {
      $(".pull-down img").attr("style","transform:rotate(0deg);-ms-transform:rotate(0deg); /* IE 9 */-moz-transform:rotate(0deg); /* Firefox */-webkit-transform:rotate(0deg); /* Safari 和 Chrome */-o-transform:rotate(0deg); /* Opera */");
    }
  });
});
