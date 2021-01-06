<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Share</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.js"></script>
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='index.css')}}">
</head>

<body>
    <script src="{{url_for('static', filename='index.js')}}"></script>
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Text Share</a>
        <a class="text-sm-left text-white mr-auto">| 24 hours TTL</a>

        </div>
    </nav>

    <div id=copydiv>
        <button class="btn btn-primary btn-lg" onclick="copyLink()" id="savebtn">Copy text</button>
        <input type="text" id="generatedLink" disabled="disabled">
    </div>
</body>
<script>
    var link = '{{ link|safe }}';
    console.log(link)
    document.getElementById("generatedLink").value = link;
</script>

</html>