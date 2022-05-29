$(document).ready(function(){
    var output_file = document.getElementById('output_file');
    $(document).on('change', '#output_file', function(e){
        var fr = new FileReader();
        fr.onload = function(){
            document.getElementById('output_id').textContent = fr.result;
            }
       fr.readAsText(output_file.files[0]);

    })

    // Click event for Log file analyze button
    $(document).on('click', '#btn_log_analyze', function(e){
        e.preventDefault();

        var log_file_name = document.getElementById('log_file_name').value;
        var span_analysis_id = document.getElementById('span_analysis_result');

        if (log_file_name.length == 0){
            alert('Invalid log file name!');
            return;
        }
        var form_data = {'log_file_name':log_file_name}

        $.ajax({
            url : '/analyze_log_file',
            type : 'POST',
            data : form_data,
            success : function(result){
                json_result = JSON.parse(result);
                result_value = json_result['result']
                if (result_value == 'success'){
                    console.log(json_result['data']);
                    result_data = JSON.parse(json_result['data']);
                    inner_html_text = '<table class="table table-striped">';
                    for (var key in result_data){
                        inner_html_text += `
                            <tr>
                            <td>${key}</td>
                            <td>${result_data[key]}</td>
                            </tr>`
                    }
                    span_analysis_id.innerHTML = inner_html_text;


                }else{
                    // TODO : Error formatting required.
                    alert(json_result['data'])
                }
            }
        });
    })
});