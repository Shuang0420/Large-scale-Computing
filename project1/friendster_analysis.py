#!/usr/bin/python


# Loads the edges data of the Friendster social network from HDFS storage in an RDD
EdgesRDD=sc.textFile('hdfs:///user/hadoop/input/com-friendster.ungraph.txt')
# Calculates the degree of each node using only the map and reduce functions available for RDDs
calRdd=EdgesRDD.flatMap(lambda x: x.split('\t',1)).map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y)
# Sorts the nodes in decreasing order of their degrees
sortRdd=calRdd.map(lambda x:(x[1],x[0])).sortByKey(ascending=False).map(lambda x:(x[1],x[0]))
# Prints the top-100 nodes which have the highest degrees
sortRdd.take(100)
