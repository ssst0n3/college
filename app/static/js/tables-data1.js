var editor;

$(document).ready(function() {

    columns_str = $("#columns").html();
    tableName = $("#tableName").html();
    columns = columns_str.substring(0,columns_str.length-1).split(",");
    var fields = new Array();
    for(var i = 0; i < columns.length; i++){
      column = columns[i].substring(2,columns[i].length-1);
      field = {"label":column+':',"name":column};
      fields[i]=field;
    }
    fields[5]={"label":"Extension:","name":"extn"}

    // console.log(fields);

    editor = new $.fn.dataTable.Editor({
      ajax: "/admin/insert_table/",
      table: "#table",
      fields:fields
    });







    $('#table').dataTable({
      dom: 'Bfrtip',
      // select: true,
      buttons:[
        // 'pageLength', 'copy', 'excel', 'pdf', 'print', 'colvis',
        {extend: 'create', editor: editor},
        {extend: 'edit', editor: editor},
        {extend: 'remove', editor: editor},
      ]
    });
    //
    // $("#table tbody").on("dblclick", "td", function(){
    //   td = $(this);
    //   txt = td.html();
    //   input = $("<input type='text'>")
    //   input.val(txt);
    //   td.html(input);
    //   input.focus();
    // });
    //
    // $("#table tbody").on("blur", "td", function(){
    //   td = $(this);
    //   input = td.children();
    //   txt = input.val();
    //   td.html(txt);
    //
    //   index = td.index();
    //   id = td.parent().children().first().html();
    //   columns_str = $("#columns").html();
    //   tableName = $("#tableName").html();
    //   columns = columns_str.substring(0,columns_str.length-1).split(",");
    //   for(var i = 0; i < columns.length; i++){
    //     columns[i] = columns[i].substring(3,columns[i].length-1);
    //   }
    //
    //   type = columns[index]
    //   console.log(type);
    //   console.log(columns);
    //   data = {"id":id,"type":type,"edit_data":txt,"tableName":tableName};
    //   // $.post("/admin/edit_table/",
    //   // {
    //   //   'd1':'username'
    //   // },
    //   // function(data){
    //   //   alert(data);
    //   // });
    //   $.ajax({
    //     type: "POST",
    //     url: "/admin/edit_table/",
    //     data:data,
    //     success: function(data){
    //       console.log(data.success);
    //     },
    //     dataType: "json",
    //     error: function(){
    //       alert("error");
    //     }
    //   });
    // });
    //
    // // $(".DTE_FROM_Buttons button").on("click",function(){
    // //   alert('yes');
    // // });

});
