# Flatten Images of a Candle by way of Circumference

The purpose of this project was to take four images of the same candle and produce four flattened images.  First, I set thresholds for an erosion to locate the edges by way of Canny edge detection.  This produced four cropped images of the candle.  

Then, I determined the points along what should be the arclength of the candle in order to flatten the candle by its circumference.  I distributed the minimum of each arclength to the previous pixel in order to fill in the gaps.  

The main goal for the project originally was to flatten the candle images and then stitch them together as a panoramic.  However, this proved difficult because of the lack of detail in the candle images that made it difficult to find key points to stitch together.  



