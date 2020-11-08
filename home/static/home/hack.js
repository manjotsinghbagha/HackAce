// sticky navigation 

let navbar = $(".navbar");

$(window).scroll(function () {
  // get the complete hight of window
  let oTop = $(".section-2").offset().top - window.innerHeight;
  if ($(window).scrollTop() > oTop) {
    navbar.addClass("sticky");
  } else {
    navbar.removeClass("sticky");
  }
});

  function showPreview(event){
    if(event.target.files.length > 0){
      var src = URL.createObjectURL(event.target.files[0]);
      var preview = document.getElementById("file-ip-1-preview");
      preview.src = src;
      preview.style.display = "block";

      var paragraph = document.getElementById("p");
      var text = document.createTextNode("Submit")

      paragraph.appendChild(text);
      // console.log(src)
          // Notice there is no 'import' statement. 'mobilenet' and 'tf' is
    // available on the index-page because of the script tag above.
  
    // var img = document.getElementById('file-ip-1-preview');
    var img = src;
    // resize 
    let mp = tf.tensor(img)
    console.log(mp)
    // Load the model.
    tf.loadLayersModel("/media/model/cat/model.json").then(model => {
      // Classify the image.
      model.predict([tf.fromPixels(loadedImage).resizeBilinear([150,150]).array().then(predictions => {
        console.log('Predictions: ');
        console.log(predictions);
      });
    });

       
    }
  }

  
  
