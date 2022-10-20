from tqdm import tqdm
import requests
import time

chunk_size=1024
try:
	url=input("enter the pdf url: ")

	r=requests.get(url,stream=True)

	total_size = int(r.headers['content-length'])
	with open("IBM.pdf","wb") as f:
		for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total = total_size/chunk_size, unit='KB'):
			f.write(data)
	print("Download completed!")
except:
	print("try another url!!")	
