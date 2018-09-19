from pyspark import SparkContext
sc =SparkContext()
print('ONE')
rdd = sc.textFile("s3a://venmo-data/2010_12/venmo_2010_12_10.json")
print('TWO')
A = rdd.flatMap(lambda element: element.split(','))
print('THREE')
linesWithMessage = A.filter(lambda line: "message" in line)
print('FOUR')
linesWithMessage.count()
print('FIVE')
linesWithMessage.first()
print('SIX')
