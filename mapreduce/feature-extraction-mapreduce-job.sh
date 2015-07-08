# variables
input=tweets-100k.csv
output=features-output
hadoop_streaming=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar

# remove output folder from hdfs and local fs
rm -r $output
hadoop fs -rm -r $output

# upload input to hdfs and delete if already exists
hadoop fs -rm -r $input
hadoop fs -put data/$input

# initialize start datetime
start_date=$(date)

# mapreduce command
hadoop jar $hadoop_streaming \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input $input -output $output

end_date=$(date)
# print start and end datetime 
echo "start:  $start_date"
echo "finish: $end_date"

#download output to local fs
hadoop fs -get $output
