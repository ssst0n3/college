var editor;

columns_str = $("#columns").html();
tableName = $("#tableName").html();
columns = columns_str.substring(0,columns_str.length-1).split(",");
var fields = new Array();
for(var i = 0; i < columns.length; i++){
  column = columns[i].substring(3,columns[i].length-1);
  field = {"label":column+':',"name":column};
  fields[i]=field;
}

$(document).ready(function() {
    editor = new $.fn.dataTable.Editor({
      ajax: "/admin/edit_table/users",
      table: "#table",
      fields:fields
    });

    $('#table').on('click', 'tbody td:not(:first-child)', function(e){
      editor.inline(this,{
        buttons:{label:'&gt;', fn:function(){this.submit();}}
      });
    });

    $('#table').DataTable({
      dom: 'Bfrtip',
      ajax: "/admin/load_data/users",
      columns:[
        {
          data:null,
          defaultContent: '',
          className: 'select-checkbox',
          orderable: false
        },
        {data:'id'},
        {data:'username'},
        {data:'password'},
        {data:'email'},
        {data:'role'}
      ],
      select: {
        style:  'os',
        selector: 'td:first-child'
      },
      buttons:[
        'copy','excel','pdf',
        {extend: 'create', editor: editor},
        {extend: 'edit', editor: editor},
        {extend: 'remove', editor: editor},
      ]
    });


});
