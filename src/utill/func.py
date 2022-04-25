def is_none_empty(value:str = None):
	'''
	引数がnoneまたは0-Lengthかどうかをチェックする
	'''
	return value is None or len(value) <= 0