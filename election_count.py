import mediacloud, datetime
mc = mediacloud.api.MediaCloud('ed673300791e2d3b3f3f1ddb933da2c11fc57bfded8781d049c95be511d90fcd')
res = mc.sentenceCount('Trump', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
res2 = mc.sentenceCount('Clinton', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
print 'Trump' if res['count'] > res2['count'] else 'Clinton'
