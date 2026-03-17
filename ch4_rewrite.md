Experimental Setup 

Our evaluation platform is AMD RyzenTM 9 9950X CPU @ 4.3GHz, 192GB memory, ZHIATAI Ti7100 4TB NVMe SSD, and Ubuntu 22.04.1 LTS. We code the above three schemes in the Go (version 1.23) language with the Go standard cryptographic libraries2, which provides AES-256, HMAC-SHA256, and SHA256. We employ AES-256 in CBC mode, HMAC-SHA256, and SHA-256 to realize symmetric encryption, PRFs, and hash functions, respectively, use the Go bloom filter library3 to realize the bloom filter, and adopt the Type A parings in Gopbc library4 to implement the group operations. We store all ciphertexts CDB in MySQL and employ a bloom filter to construct XSET. We extract the following three real datasets to test FDXT, ODXT, and SDSSE-CQ. 

Chicago Crimes Reports [41]. The Crime dataset contains 7,989,987 pairs drawn from the incident reports dated 1 Jan 1999 to 2 Apr 2024, where street names serve as searchable keywords mapped to IUCR codes. Finally, there are 63,659 distinct keywords, and the highest keyword volume is 16,644. 

Wikipedia [42]. We extract keywords from the processed data using Wikipedia Extractor [43] and the Python NLTK package [44]. Each Wikipedia article serves as a single document, and let the article’s number be the corresponding document’s identifier. Finally, there are 4,565,948 pairs of keyworddocument-identifiers, including 10,000 distinct keywords, and the highest keyword volume is 9,738.

Enron [45]. The Enron email dataset contains 5,190,199 keyword-email pairs index entries generated through NLP preprocessing using NLTK with Porter stemming [46]. Finally, there are 16,241 distinct keywords, and the highest keyword volume is 26,946. 

Moreover, we configure the document deletion rate to be 10% and the rate of the updated-but-unsearched documents to be 10% for all the above compared schemes. We employ the bloom filter of thirteen hash functions and the false positive rate p = 10−4 to realize SDSSE-CQ.