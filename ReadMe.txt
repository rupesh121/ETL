Mini-project for Data Engineering Job at Unison Investment Management
-----------------------------------------------------------------------
Project:
--------
Automated ETL Script

Description:
Information below explains the source code in python
------------
Line(8-13) Imported libraries like pymysql, pandas, time, datetime required for the project

Line 16= Intiatilized current_length to zero

Line (17-24) created Ouput table statistics

Line 39: intialized new_length to the number of rows in the input table

I have selected the data required( “lot_size_sqft”, “total_building_sqft”, “yr_built”, “bedrooms”, “total_rooms”, “bath_total”, “final_value”) from input table (raw_data)
and fetched it into the DataFrame.

I have pulled out the column headers using dataframe and assigned it to the variable columns

I have traversed through each column header in the columns variable using for loop and computed statistics for them respectively.This loop will execute only if new_length is greater than current_length, this means if no rows are added to the input table. Statistics will not be performed. Point to be noted here is that the new_length will be assigned to current_length in the loop.

For the given scenario, Input table has 10,000 rows.current_length=0 and new length=10,000. if condition satisfies as new_length is greater than current_length, during the loop we assign new_length to the current_length. It means current_length will be equal to 10,000. condition fails in the next attempt as if condition fails.

If more rows are added to the input table. source code will detect the changes in the input table and changes the new_length variable accordingly. Now, new_length will be greater than current_length, so statistics will be computed for new timestamp and gets appended to the old rows without deletion.

While loop is set to true, because it will run the source code for every 2 min and detect the changes made to the input table










_
