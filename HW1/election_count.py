import mediacloud, datetime
#Default key: The variable 'key' must be edited according to the specific mediacloud user
key = '00'
mc = mediacloud.api.MediaCloud(key)

#Comparison of number of stories written about 'Trump' and 'Clinton' in September 2016 
res = mc.sentenceCount('Trump', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
res2 = mc.sentenceCount('Clinton', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
person = 'Trump' if res['count'] > res2['count'] else 'Clinton'
print 'The US Mainstream Media sources talked more about', person, 'in the September 2016.'
