# Report Assignment 1

### Point d
<p>
<img src="plot/Figure_1.png" width="150" height="150" align="right" border="0">
1. In the first convolution, in the first 1D Gaussian filter it applies it first on $x$ direction and then on the $y$ direction. That double operation is equivalent to a 2D Gaussian filter. With that filter combination gives us the possibility to apply a smooth on image.
In our example we get a smoothed white point which reflects the bell-shaped fuction viewed from above. Hence applying the first convolution on the rows of the image we get black rows, apart the central row which get smoothed. In the second convolution the central row is smoothed in vertical, propagating the white pixels through all the image obtaining a radial view.
</p>
<p>
2. As for the mechanism explained above, filter.py applies first a normal Gaussian convolution parallel to the horizontal axes, but now the second convolution is the derivative $Dx$ of the Gaussian filter. The derivative filter array has, in the first half, values tending to 1, while in the second half the values tend to 0. This means that applying the filter in vertical ($Dx.T$) the upper part of the image is lighter, while the bottom part is darker.
<img src="plot/Figure_5.png" width="100" height="100" align="right" border="0">
<p>
3. Now the convolution is first applied with $Dx.T$ and then with $Gx$. The resulting image is the same as the second point, this means that the order in which the convolution is applied doesn't matter. Hence it seems that the convolution is commutative. The transformation could be different if the direction in which we apply the kernels changes, like for example ```conv(conv(img, Gx.T), Dx)``` (point 5 and 6).
</p>
<p>
<img src="plot/Double derivative.JPG" width="150" height="150" align="right" border="0">
4. Here the system apply both the convolution with a kernel obtained by the derivative function $Dx$. The first convolution is applied horizontally and we get an image where the first half is white and the second one is darker. The transpose kernel has the brighter pixels in the upper part of the array, while the darker ones in the bottom part.
Applying the filter vertically, in the first half the brighter pixels are brought in the first quadrant and the darker ones in the third quadrant because it is applied on the white ones. In the second half (the darker part), the pixels are brought to the second quadrant because it is applied on the darker ones. In conclusion, the derivative function yelds the pixels on which it's applied in the direction where the function "goes up".
</p>
<p>
5. Similar to the point 2 or 3 the convolution is applied two times: the first application with the filter $Dx$ and the last one with the filter $Gx.T$.
The application of $Dx$ create a situation where in the horizontal axes the left part of the pixels tendig to $1.0$. The right part of the image, with this application, tending to $0.0$ value. With the convolution on filter $Gx.T$ the vertical axes create a specular situation of point 2: the Gaussian filter do a smooth on the lighter part and the dark one, respective.
At the end of computation the situation is a left light smoother part and the respective right part a smoother dark one. At the human vision is similar to 90° rotate of image at the second point.
</p>
<p>
<img src="plot/differentation.JPG" width="150" height="150" align="right" border="0">
</p>
<p>
6. At this point the application is that```conv(conv(img, Gx.T), Dx)```. For the same reason of the point 3 and 2 and also the thesis of the point 5 the result of this application explain the property of commutation and the property of differentation; the inverted application of filter create the situation of rotation.
With $Gx.T$ application the image is smoothed on the vertical axes with the Gaussian filter: the pixels on the centre of arrays are lighted and the pixels at the borders darker.
When $Dx$ do its change the situation is the same of the precedent point: the left part of image is lighted and the right one darker. The derivate of a filter array x has the left part values tending to $1.0$ and the opposite ones tendig to $0.0$.
The diifferentation rule is: [ADD IMAGE OF DIFF: RULE]
That, with the commutative one, create the association in point 2-3 and 5-6.
</p>

### Point e
<p>
The derivative filter is used to detect edges. Ideally we should first smooth the image in order to remove the noise, in fact a smoothed image will remove small details. The effect to apply the derivative filter is to increase the change of colors, so it point out the differences. In our case the derivative filter is applied without smoothing the image first. Therefore in graf.png the filter highlight small details like the antenna of the car.
In our case $\sigma$ is setted at 7.0. Edges are large, less defined and strength. Decreasing $\sigma$ has the effect to decreasing the edges but obtaining more defined lines.
Applying the filter parallel to the $x$ axes, we highlight the vertical edges. For example in gantrycrane.png the central pillar is well defined in imgDx, while it almost disappear in imgDy. On the other hand, applying the filter prallel to the $y$ axes, the horizontal edges are spotted.
The last image is obtained by calculating the magnitude of the gradient. This method highlights the edges in every direction.
[ADD IMAGE on the botttom]In the image there are the two cases of the application of ```gaussderiv``` in two differences images. The left ones is the application on the first dimension, the centered ones the application on the other dimension and, at right, there are the result of merging. The merge of the two image derivate in $x$ and in $y$ explains the power-up of the edge on 2D.
</p>
<img src="plot/Figure_8_upgrade.png" width="150" height="150" align="center" border="0">
