##Introduction
Locations is a simple project to get Geo-Coordinates of Villages, Towns and Cities in India. 
This uses a simple http connection, thus removing all the complexities. 
Ideal for smaller projects. Also note that, this project uses 2001 census.
When we contacted the Census Department for 2011 data they stated that shape files, latitude and longitude are not available for dessimation.

##How to use
To find coordinates for Mumbai use the following code

```python
import Locations as LC

lc_i = LC.Location()
mum_cord = lc_i.getCoordinates("Mumbai")
```

##Acknowledgements
Thanks to http://india.csis.u-tokyo.ac.jp/default/single for making this possible
