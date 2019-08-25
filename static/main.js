function getImageUrl(){
    console.log("button clicked")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("poster").src = this.responseText;
        }
    };
  xhttp.open("GET", "get-image", true);
  xhttp.send();
}

function getQuote(){
    console.log("button clicked")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            
            var jsonData = JSON.parse(this.responseText);
            document.getElementById("quote-text").innerText = jsonData[0]; // Manipulating DOM 
            document.getElementById("author-text").innerText = ' - ' +jsonData[1];
        }
    };
  xhttp.open("GET", "get-quote", true);
  xhttp.send();
}

function draw(){
    var canvas = document.getElementById("poster-canvas")
    var context = canvas.getContext("2d")
    var imgobj = new Image()
    imgobj.onload = function(){
        context.drawImage(imgobj,0,0)
        canvas.width = imgobj.width
        canvas.height = imgobj.height
        context.font = "40pt Calibri"
        context.fillStyle = "White"
        context.fillText("Hello",50,50)
        var dataurl = canvas.toDataURL();
        downloadCanvas(dataurl);
    }
    imgobj.setAttribute("crossOrigin","anonymous")
    imgobj.src = document.getElementById("poster").src
    
}

function downloadImage(){
    document.getElementById('download').click();
  }

  function downloadCanvas(dataUrl){
    const a = document.createElement('a');
    
    a.href = dataUrl
    a.download = "image.png"
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    
  }