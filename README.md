# MapDataProcessor
Assignment of Coreshield
Output 
Valid Points Count Per Type:
restaurant    3
hotel         3
cafe          2
Name: type, dtype: int64

Average Rating Per Type:
type
cafe          4.6
hotel         3.4
restaurant    4.1
Name: rating, dtype: float64

Location with the Highest Number of Reviews:
id                     loc_07
latitude               64.0522
longitude            -108.233
type                     hotel
rating                     2.0
reviews                   900.0
Name: 5, dtype: object

Locations with Incomplete Data:
Empty DataFrame
Columns: [id, latitude, longitude, type, rating, reviews]
Index: []


Explanation of the Output:
Valid Points Count Per Type:

The script counts the number of valid entries for each type (restaurant, hotel, cafe).
Average Rating Per Type:

The script calculates the average rating for each type.
Location with the Highest Number of Reviews:

The location with the highest number of reviews is identified (loc_07 with 900 reviews).
Locations with Incomplete Data:

Since all data entries are complete, the output for incomplete data is an empty DataFrame.
