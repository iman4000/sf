var $table = $('#table')


function initTable() {
    $table.bootstrapTable('destroy').bootstrapTable()
}
$(function () {
    initTable()

    $('#locale').change(initTable)
})