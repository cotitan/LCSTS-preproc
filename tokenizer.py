from stanfordcorenlp import StanfordCoreNLP
# from tqdm import tqdm
import re
import sys

corenlp = StanfordCoreNLP('/home/kirk/Downloads/stanford-corenlp-full-2018-10-05', lang='zh', memory='5g')

def tokenize(filein, fileout):
	fin = open(filein)
	fout = open(fileout, 'w')
	for idx, line in enumerate(fin):
		if (idx+1) % 20000 == 0:
			print('processing the %d th instance' % (idx + 1))
		line = re.sub('[0-9]', 'x', line.strip())
		words = corenlp.word_tokenize(line)
		fout.write(' '.join(words) + '\n')
	fin.close()
	fout.close()

if __name__ == '__main__':
	tokenize(sys.argv[1], sys.argv[2])

