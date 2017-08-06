var _gaq = _gaq || [];

var msgSet = new Set();


// Create the XHR object.
function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // XHR for Chrome/Firefox/Opera/Safari.
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // XDomainRequest for IE.
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    // CORS not supported.
    xhr = null;
  }
  return xhr;
}

// Helper method to parse the title tag from the response.
function getTitle(text) {
  return text.match('texto');
}

// Make the actual CORS request.
function makeCorsRequest(text, image = "") {
  // This is a sample server that supports CORS.
  var url = 'https://sheltered-river-24109.herokuapp.com';

  var xhr = createCORSRequest('POST', url);
  if (!xhr) {
    alert('CORS not supported');
    return;
  }

  // Response handlers.
  xhr.onload = function() {
    var text = xhr.responseText;
    var title = getTitle(text);
    console.log('Response from CORS request to ' + url + ': ' + text);
  };

  xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
  };

  // xhr.setRequestHeader("Content-type", "application/json");
  // xhr.setRequestHeader("Authorization", "Basic " + Nzg0Zjk5MjMtMDA4Ny00NDFjLWIxMzEtNDgwYjIwMDBiM2E2OjFFUjZNUVU3NFFzQg==);
  var data = JSON.stringify({"text": text}, {"imageURL":image});

  xhr.send(data);
}


const facebook_clickbait = function(node) {

  const images = [...node.getElementsByClassName('clearfix _o46 _3erg _29_7 direction_ltr text_align_ltr')];
  // console.log(images)

  images.forEach(function(el) {
    var msgCurta = [...el.getElementsByClassName('_3oh- _58nk')];
    var msgLonga = [...el.getElementsByClassName('_3058 _ui9 _hh7 _s1- _52mr _3oh-')];
    var msgs = msgCurta.concat(msgLonga);

    msgs.forEach(function(i) {
      if(!msgSet.has(i.textContent)){
        console.log(i.baseURI +" " + i.textContent)
        msgSet.add(i.textContent)

        makeCorsRequest(i.textContent)
      //   var xhr = new XMLHttpRequest();
      //   var url = "https://posttestserver.com/post.php";
      //   xhr.open("POST", url, true);
      //   xhr.setRequestHeader("Content-type", "application/json");
      //   xhr.setRequestHeader("Authorization", "Basic ");
      //   xhr.onreadystatechange = function () {
      //       if (xhr.readyState === 4 && xhr.status === 200) {
      //           var json = JSON.parse(xhr.responseText);
      //           console.log(json);
      //       }
      //   };
      //   var data = JSON.stringify({"text": i.textContent});
      //   xhr.send(data);
      // }
      }
    });
  });
};

const observer = new MutationObserver(function(mutations) {
      facebook_clickbait(document.body);
});

const config = { attributes: true, childList: true, characterData: false, subtree: true }

observer.observe(document.body, config);

facebook_clickbait(document.body);
