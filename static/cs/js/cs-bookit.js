



href="javascript:(function(){window.open('http://localhost:8000/people/user-resources/add?url='+encodeURI(window.location.href),'height=200,width=150')}())">

href="javascript:(function(){var request = new XMLHttpRequest();request.open("GET", 'http://localhost:8000/resources/get-json/tag-set/for-user/',true);request.onreadystatexchange=function(){var done=4,ok=200;if(request.readyState==done&&request.status==ok){if(request.responseTest){alert(request.responseText);}}};request.send(null);})"


    <a id="csbookmarklet"
           href="javascript:(function () { 
      var s = document.createElement('script');
      var e = encodeURI(window.location.href);
      var u = 'http://localhost:8000/people/user-resources/add?url=' + e;
    s.setAttribute('src', u );  
    document.body.appendChild(s);  
    }());">
           OC+</a>