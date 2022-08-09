# surfs_up

## Overview of the analysis: 
Explain the purpose of this analysis.
W. Avy likes the analysis, however, he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Results: 
Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.
  
  - First point from the analysis deliverables is writing a query to retrieve temperatures for the month of June and December and converting the data into a DataFrame.       The following code is used interchangeably between June and December by replacing the extract value from 6 (June) to 12 (December). 
  ```
  results = session.query(Measurement.date, Measurement.tobs).\
  filter(extract('month', Measurement.date) == 6).all()
  
  June_df = pd.DataFrame(results, columns=['date', 'June Temps'])
  ```
  
  - Second point from the analysis deliverables is looking into the summary statistics for both the June and December temperature to determine the average temperature,         maximum and minimum temperature. 
  
  <img width="108" alt="image" src="https://user-images.githubusercontent.com/106962921/183290844-42258987-bdf4-48aa-b95b-3911a073dbaa.png">
  <img width="130" alt="image" src="https://user-images.githubusercontent.com/106962921/183290891-53272f81-17aa-42f0-a89e-39f736a5c76f.png">

  - Third point from the analysis deliverables is looking into the frequency of temperatrues for June and December in order to determine if the surf and ice cream shop     business is sustainable year-round.
  
  ![image](https://user-images.githubusercontent.com/106962921/183291377-d7cf6232-6ae4-42a2-a95b-b990d7dd0dc4.png)
  ![image](https://user-images.githubusercontent.com/106962921/183291365-46b9a39a-b211-4933-b9fe-3fa7075bee3a.png)

## Summary: 
Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

- Overall, the weather between the months of June and December only differs by 4 degree centigrade. There is a higher frequency of high temperatures observed in the month of June and would expect more customers, however, it does not mean that June is the ideal month for surfing. At best, there would be an increase in ice cream sales. The month of December has higher frequency of low temperatures which may decrease sales in ice cream but higher rental and/or sales of surfboards due to ideal surfing criteria.

- First query that would be performed to gather more weather data is to determine if there is a correlation between temperature and ocean waves. Predicting the ideal wave for surfing and when it would most occur would increase sales and/or rental for surf boards as well as determining the ideal temperature to sell ice cream would also create revenue. The business revolves around surfing and ice cream and in order to sell one or the other, there has to be a demand for them.  

- Second query that would be performed is creating a heat map that would help predict the weather patterns from June to December. Predicting what the weather would be like essentially assist in how to manage the shops during on and off tourist season.
