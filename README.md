#Introduction
Locations is a simple project to get Cordinates of Village, Towns and Cities in India. 
This uses a simple http connection, thus removing all the complexities. Ideal for smaller projects. Also this uses the 2001 census.
When we contacted the Census Department for 2011 data they stated that shape files, latitude and longitude are not available for dessimation.

#How to use

To find coordinates for Mumbai use the following code

```python
import Locations as LC

lc_i = LC.Location()
mum_cord = lc_i.getCoordinates("Mumbai")
```