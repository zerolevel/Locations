##Introduction
Locations is a simple project to get Geo-Coordinates of Villages, Towns and Cities in India. 
This uses a simple http connection, thus removing all the complexities. 
Ideal for smaller projects. Also note that, this project uses 2001 census.
When we contacted the Census Department for 2011 data they stated that shape files, latitude and longitude are not available for dessimation.

##How to use

* Import Locations package

    ```python
        import Locations as LC
    ```

* Initialize the Location class

    ```python
        lc_i = LC.Location(state=[],district=[])
    ```

* Use Location instance to get coordinates
    ```python
        lc_i.getCoordinates(name=PlaceName)
    ```
 
###Usage Examples
 
* To find coordinates for Mumbai use the following code

    ```python
        import Locations as LC
        
        lc_i = LC.Location()
        mum_cord = lc_i.getCoordinates("Mumbai")
    ```
    
* To find coordinates for Nehdai Village in Jaisalmer District of Rajasthan state use the following code

    ```python
        import Locations as LC
        
        lc_i = LC.Location(state="Rajasthan",district="Jaisalmer")
        nehdai_cord = lc_i.getCoordinates("Nehdai")
    ```

* To find coordinates for Parbatsar in Rajasthan state use the following code

    ```python
        import Locations as LC
        
        lc_i = LC.Location(state="Rajasthan")
        parbatsar_cord = lc_i.getCoordinates("Parbatsar")
    ```

* To get a List of best suited coordinates as per the query arguments add 'listLength' as follows

    ```python
        import Locations as LC
        
        lc_i = LC.Location(state="Rajasthan")
        parbatsar_cord = lc_i.getCoordinates("Parbatsar",listLength=5)
    '''

##Acknowledgements
Thanks to http://india.csis.u-tokyo.ac.jp/default/single for making this possible
