function submit() {
    var url = "/api/v1/get/posts";
    var data = document.getElementById("post_txt").value;
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", url);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
       if (xhr.readyState === 4) {
          var Myelement = document.querySelector('textarea[name="post_txt"]');
          Myelement.value = "";
          console.log(xhr.status);
          console.log(xhr.responseText);
          location.reload();
       }};

    xhr.send(data);
}