Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


======= RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py =======
Traceback (most recent call last):
  File "C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py", line 5, in <module>
    data = pd.read_CSV("C:/Users/Desktop/APDP PYTHON CODE/Books.CSV")
AttributeError: module 'pandas' has no attribute 'read_CSV'. Did you mean: 'read_csv'?

======= RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py =======
Traceback (most recent call last):
  File "C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py", line 5, in <module>
    data = pd.read_csv("C:/Users/Desktop/APDP PYTHON CODE/Books.CSV")
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/Desktop/APDP PYTHON CODE/Books.CSV'

=========================================================== RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py ===========================================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py", line 5, in <module>
    data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV")
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV'

=========================================================== RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py ===========================================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py", line 5, in <module>
    data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.csv")
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/user/Desktop/APDP PYTHON CODE/Books.csv'

=========================================================== RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py ===========================================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py", line 5, in <module>
    data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV")
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/user/Desktop/APDP PYTHON CODE/Books.CSV'

=========================================================== RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py ===========================================================
Traceback (most recent call last):
  File "C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py", line 5, in <module>
    data = pd.read_csv("C:/Users/user/Desktop/APDP PYTHON CODE/Books.csv")
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/user/Desktop/APDP PYTHON CODE/Books.csv'

=========================================================== RESTART: C:/Users/user/Desktop/APDP PYTHON CODE/FIRST PROJECT.py ===========================================================

--- Books Published Per Year ---
publication date
2011      8
2012     61
2013      8
2014     51
2015     32
2016     17
2017     28
2018     47
2019     24
2020     58
2021    128
2022     65
2023     77
Name: count, dtype: int64

--- Top 5 Authors by Number of Books ---
author
Zuri Day           26
Valerie Jackson    22
Jenni Fagan        12
Jeffrey Haynes     12
Matt Jones         10
Name: count, dtype: int64

--- Language Distribution ---
language
English     153
German      150
French      129
Chinese      93
Italian      56
Japanese     23
Name: count, dtype: int64

--- Books Per Publisher ---
book publisher
Routledge                        61
Elsevier/Masson                  41
SpringerGabler                   18
Peter Lang                       16
Chartered Insurance Institute    15
Mills&Boon                       14
: Springer                       13
Wiley-VCH                        12
Dafina                            7
Luyi Publishing                   6
Name: count, dtype: int64

--- Missing ISBN Analysis ---
Missing ISBN count: 9
Missing ISBN percentage: 1.49%

--- Books Published Per Year by Language ---
language          Chinese  English  French  German  Italian  Japanese
publication date                                                     
2019                  0.0     13.0     0.0     0.0      8.0       3.0
2020                 14.0      9.0     0.0     0.0     27.0       8.0
2021                 43.0     11.0     0.0    45.0     17.0      12.0
2022                 23.0     11.0     0.0    27.0      4.0       0.0
2023                 13.0     30.0    20.0    14.0      0.0       0.0
