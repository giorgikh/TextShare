console.log("+++")

  $(document).ready(function() {
    $('#summernote').summernote({
        toolbar: [
          // [groupName, [list of button]]
          ['style', ['bold', 'italic', 'underline', 'clear']],
          ['font', ['strikethrough', 'superscript', 'subscript']],
          ['fontsize', ['fontsize']],
          ['color', ['color']],
          ['para', ['ul', 'ol', 'paragraph']],
          ['view', ['fullscreen']],
        ],
        placeholder: 'write here...',
        dialogsFade: true,
        height: 600
      });
  });


  function save(){
    $("#summernote").summernote("enable");
    var userInputMarkupStr = $('#summernote').summernote('code');
    // var inputText = $($("#summernote").summernote("code")).text();  Plain Text
    console.log(userInputMarkupStr)
    sendDataWithPostRequest(userInputMarkupStr)
    
}


function disableEdit(){

  $("#summernote").summernote("disable");
}


function enableEdit(){

  $("#summernote").summernote("enable");
}

function displaySummerNote(displayOption){
    var summernoteElement =document.getElementsByClassName("note-editor note-frame panel panel-default");
    for (var i = 0; i < summernoteElement.length; i+=1){
        summernoteElement[i].style.display = String(displayOption);  
    }  
    
}


function displayNavbarButtons(displayOption){
    var buttonElements =document.getElementsByClassName("navbar-text");
    for(var i = 0; i<buttonElements.length; i += 1){
        buttonElements[i].style.display = String(displayOption);
    }
}

function sendDataWithPostRequest(data){
    $.ajax({
        type: "POST",
        url: "/",
        data: data,
        success: "success",
        dataType: "text"
      });
}


function test(){
    console.log("---")
}

function copyLink() {
  var copylink = document.getElementById("generatedLink");
  
  copylink.disabled = false;
  /* Select the text field */
  copylink.select();
  copylink.setSelectionRange(0, 99999); /* For mobile devices */
  document.execCommand("copy");

  /* Alert the copied text */
  document.getElementById("savebtn").innerText = "Copied";
  copylink.disabled = true;

}