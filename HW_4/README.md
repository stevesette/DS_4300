1. First, we take in the file based on filename and get an iterable per line. We split each line by 
   the "," character to get the individual columns using map. The next map brings in another value 
   at every row for null values by testing if the value is "" and giving the empty values a corresponding 1
   and 0 otherwise. Then we take the pairs and reduce them by zipping them together and adding the 
   corresponding values resulting in one value for each column containing the number of nulls
2. binary.scala: toBinary=01001001100101100000001011010010 weight=
3. partition.scala: moved=990600
4. Redis.scala
5. Redis.scala: shortestPath=(x,j,r,y)