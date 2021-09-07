# Your imports go here
import logging
import os
import regex as re2
logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:
    os.chdir(dirpath + '/')
    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    matches=[re2.findall(r'(?<=Text.*?)([0-9]?[-+.,]?[0-9]+[.][0-9]+)',line)
            for line in open('./ocr.json')]
    maxim=-1
    for m in matches:
        for n in m:
            n1 = re2.sub(',','', n)
            if float(n1)> maxim:
                maxim=float(n1)
    print(maxim)
    os.chdir('../..')
    return maxim