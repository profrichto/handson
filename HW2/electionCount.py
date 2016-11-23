import mediacloud, datetime, logging

logging.basicConfig(filename='electionCount.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)

class ElectionCount:

	def __init__(self, key):
		#Intitalise function with actual key value
		self.key = key
		logging.info('Accessing MediaCloud')
		self.mc = mediacloud.api.MediaCloud(self.key)
		logging.info('Finished Accessing MediaCloud')

	def getSentenceCount(self, person1, person2, start_date, end_date):

		logging.debug('Inputs to getSentenceCount: ' + person1 + ',' + person2 + ',' + str(start_date) + ',' + str(end_date))
		mc = self.mc
		res = mc.sentenceCount(person1, solr_filter=[self.mc.publish_date_query( datetime.date(start_date[2], start_date[1], start_date[0]), datetime.date(end_date[2], end_date[1], end_date[0]) ), 'tags_id_media:1' ])
		res2 = mc.sentenceCount(person2, solr_filter=[mc.publish_date_query( datetime.date(start_date[2], start_date[1], start_date[0]), datetime.date(end_date[2], end_date[1], end_date[0]) ), 'tags_id_media:1' ])

		return res['count'], res2['count']
