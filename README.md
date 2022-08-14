# UncannyEdgeDetection

<p>
I wanted to learn more about how edge-detection programs work so I followed the wikipedia page on Canny Edge Detection to make my own in python. I won't bother going over how the program works here; read the <a href="https://en.wikipedia.org/wiki/Canny_edge_detector">Wikipedia Page</a> on canny edge detection if you're interested.
</p>

<p>
It's not great, but it's also not too bad. It does a decent job at picking up edges while ignoring noise and another non-edge color changes but is quite slow (although I havn't actually compared it to other programs). I also added the option to edge trace GIFs by parsing and tracing each frame individually then combining them back into a new gif. 
</p>

<h2>Some Examples:</h2>

<p float="left">

<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/kitchen.jpg" width="333">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/kitchenGrayscale.PNG" width="333">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/kitchenGaussian.PNG" width="333">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/kitchenIntensityGradient.PNG" width="333">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/kitchenEdgeThinning.PNG" width="333">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/kitchen%20trace%202.PNG" width="333">
  
</p>

<p float="left">

<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/Shockinggif.gif" width="500">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/shockinggif%20traced.gif" width="500">
  
</p>

</p>

<p float="left">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/car.PNG" width="500">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/car%20trace.PNG" width="500">
</p>


<p float="left">

<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/engine.png" width="500">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/engine%20trace2.PNG" width="500">
  
</p>

<p float="left">

<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/insane.jpg" width="500">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/insane%20trace.PNG" width="500">
  
</p>

<p float="left">

<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/asuna.jpg" width="500">
<img src="https://github.com/Wowe-Peanut/UncannyEdgeDetection/blob/main/Images/asunatrace.PNG" width="500">
  
</p>


<h2>Citations:</h2>

Python Libraries Used: PIL, numpy, imageio, random

Sources:<br>
<a href="https://en.wikipedia.org/wiki/Canny_edge_detector">Canny Edge Detection Wiki</a><br>
<a href="https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html">OpenCV Algorithm Steps</a><br>
<a href="https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm">Gaussain Smoothing Explanation</a><br>
<a href="https://en.wikipedia.org/wiki/Sobel_operator">Sobel Operator Wiki</a><br>
<a href="https://en.wikipedia.org/wiki/Otsu%27s_method">Otsu's Method Wiki</a><br>






