var requestURL = '/api/v1/get/posts';
        var request = new XMLHttpRequest();
        request.open('GET', requestURL);
        request.responseType = 'json';
        request.send();
        request.onload = function() {
          var data = request.response;
          data_func(data);
        }
        function data_func(jsonObj) {
          var myH1 = document.createElement('h1');
          myH1.textContent = jsonObj['posts'];
          var posts_str = jsonObj['posts'];
          var div = document.querySelector('div');
          for (var i = 0; i < posts_str.length; i++) {
            var myList = document.createElement('form');
            var ID = document.createElement('a');
            var id_placehoard = document.createElement('a');
            var text = document.createElement('span');
            var p = document.createElement('p');
            var tmp = document.createElement('tmp');
            tmp.textContent = posts_str[i]['text'];
            ID.classList.add('title');
            text.classList.add('title');
            myList.classList.add('form');
            ID.href = '#' + posts_str[i]['id'];
            text.classList.add('bold');
            ID.setAttribute('id', posts_str[i]['id']);
            ID.textContent = '#' + posts_str[i]['id'];
            id_placehoard.textContent = 'ID - '
            text.innerHTML = marked.parse(tmp.innerHTML);
            myList.appendChild(id_placehoard);
            myList.appendChild(ID);
            myList.appendChild(p);
            myList.appendChild(text);
            div.appendChild(myList);
          }
        }