$(document).ready(function(){

    // Click event for Log file analyze button
    $(document).on('click', '#btn_log_analyze', function(e){
        e.preventDefault();

        var log_file_name = document.getElementById('log_file_name').value;

        if (log_file_name.length == 0){
            alert('Invalid log file name!');
            return;
        }
        var form_data = $(this).serialize();
        $.ajax({
            url : '/analyze_log_file',
            type : 'POST',
            data : form_data,
            success : function(result){
                alert('returned to JS');
            }
        });
    })
});