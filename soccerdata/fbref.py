Last login: Thu Nov 30 12:02:45 on console
(base) fishermarks@Fishers-MBP ~ % ssh ftm3@node.zoo.cs.yale.edu
Warning: Permanently added the ED25519 host key for IP address '10.66.2.196' to the list of known hosts.
Enter passphrase for key '/Users/fishermarks/.ssh/id_rsa': 
Last login: Fri Oct 13 02:00:48 2023 from 172.27.215.133
                                  Welcome!


                  If you are missing a course directory, create it with
                  $ sudo register csXYZ
                  Please report any issues to cs.support@yale.edu.

                  REBOOT CYCLE:  Every Monday ~07:00
[ftm3@rhino ~]$ ls
api.py                  cs421             pset2_test
-cs201-20220531.tar.gz  cs437             soccerdata
cs202                   enigma-simulator  soccerdata-master
-cs223-20220531.tar.gz  hw2-solution      transfermarkt-scraper-main
cs323                   hw5-skeleton      tutorial
cs365                   pset1_test
[ftm3@rhino ~]$ cd transfermarkt-scraper-main/
[ftm3@rhino transfermarkt-scraper-main]$ ls
appearances.json   confederations.json  old_players.json  pyproject.toml  tfmkt
clubs.json         Dockerfile           players.json      README.md
competitions.json  games.json           poetry.lock       scrapy.cfg
[ftm3@rhino transfermarkt-scraper-main]$ rm old_players.json 
[ftm3@rhino transfermarkt-scraper-main]$ cd tfmkt
[ftm3@rhino tfmkt]$ ls
__init__.py  __pycache__  settings.py  spiders  utils.py
[ftm3@rhino tfmkt]$ cd ..
[ftm3@rhino transfermarkt-scraper-main]$ exit
logout
Connection to node.zoo.cs.yale.edu closed.
(base) fishermarks@Fishers-MBP ~ % cd Downloads                 
(base) fishermarks@Fishers-MBP Downloads % scp ftm3@node.zoo.cs.yale.edu:~/transfermarkt-scraper-main . 
Enter passphrase for key '/Users/fishermarks/.ssh/id_rsa': 
scp: /home/accts/ftm3/transfermarkt-scraper-main: not a regular file
(base) fishermarks@Fishers-MBP Downloads % scp -r ftm3@node.zoo.cs.yale.edu:~/transfermarkt-scraper-main . 
Enter passphrase for key '/Users/fishermarks/.ssh/id_rsa': 
.release-it.json                              100%   42     8.2KB/s   00:00    
Dockerfile                                    100%  322    27.6KB/s   00:00    
confederations.py                             100%  534    62.7KB/s   00:00    
__init__.py                                   100%  161    13.7KB/s   00:00    
games.py                                      100% 7457   354.4KB/s   00:00    
game_lineups.py                               100% 6306   573.7KB/s   00:00    
common.py                                     100% 3543   500.8KB/s   00:00    
players.py                                    100% 4562   390.0KB/s   00:00    
appearances.py                                100% 5324   532.8KB/s   00:00    
clubs.py                                      100% 4196   443.3KB/s   00:00    
competitions.py                               100% 6125   879.2KB/s   00:00    
__init__.cpython-311.pyc                      100%  178    30.0KB/s   00:00    
appearances.cpython-311.pyc                   100% 7764   944.0KB/s   00:00    
common.cpython-311.pyc                        100% 5706   415.3KB/s   00:00    
clubs.cpython-311.pyc                         100% 6875   731.0KB/s   00:00    
competitions.cpython-311.pyc                  100% 7630   648.0KB/s   00:00    
confederations.cpython-311.pyc                100% 1214   151.0KB/s   00:00    
game_lineups.cpython-311.pyc                  100% 8219   756.4KB/s   00:00    
games.cpython-311.pyc                         100%   11KB   1.4MB/s   00:00    
players.cpython-311.pyc                       100% 7387   894.4KB/s   00:00    
players3.cpython-311.pyc                      100% 7776   480.7KB/s   00:00    
old_players.cpython-311.pyc                   100% 7780   736.4KB/s   00:00    
old_players.py                                100% 5156   653.6KB/s   00:00    
__init__.py                                   100%    0     0.0KB/s   00:00    
utils.py                                      100% 1605   234.2KB/s   00:00    
settings.py                                   100% 1039   156.3KB/s   00:00    
__init__.cpython-311.pyc                      100%  170    21.7KB/s   00:00    
settings.cpython-311.pyc                      100%  860   108.5KB/s   00:00    
utils.cpython-311.pyc                         100% 2549   280.9KB/s   00:00    
pyproject.toml                                100%  453    56.7KB/s   00:00    
README.md                                     100% 4265    52.4KB/s   00:00    
confederations.json                           100%   57     7.3KB/s   00:00    
.gitignore                                    100%   33     2.7KB/s   00:00    
scrapy.cfg                                    100%  223    29.4KB/s   00:00    
FUNDING.yml                                   100%   19     2.5KB/s   00:00    
scrapy-checks.yml                             100%  947   105.6KB/s   00:00    
dockerhub.yml                                 100% 1140   140.3KB/s   00:00    
poetry.lock                                   100%   43KB 755.2KB/s   00:00    
meta                                          100%  180    11.1KB/s   00:00    
pickled_meta                                  100%  131    19.0KB/s   00:00    
response_headers                              100%  525    50.8KB/s   00:00    
response_body                                 100%  131    20.5KB/s   00:00    
request_headers                               100%  246    40.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  158    21.0KB/s   00:00    
pickled_meta                                  100%  120    20.1KB/s   00:00    
response_headers                              100%  690    80.5KB/s   00:00    
response_body                                 100%  445KB   2.1MB/s   00:00    
request_headers                               100%  246    17.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  179    19.2KB/s   00:00    
pickled_meta                                  100%  131    12.3KB/s   00:00    
response_headers                              100%  525    51.8KB/s   00:00    
response_body                                 100%  131    12.0KB/s   00:00    
request_headers                               100%  246    35.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  196    17.0KB/s   00:00    
pickled_meta                                  100%  139    17.1KB/s   00:00    
response_headers                              100%  706    54.0KB/s   00:00    
response_body                                 100%  263KB   3.0MB/s   00:00    
request_headers                               100%  246    34.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    23.0KB/s   00:00    
pickled_meta                                  100%  157     8.9KB/s   00:00    
response_headers                              100%  563    69.3KB/s   00:00    
response_body                                 100%  282KB   3.1MB/s   00:00    
request_headers                               100%  358    49.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  228    31.7KB/s   00:00    
pickled_meta                                  100%  155    22.0KB/s   00:00    
response_headers                              100%  581    49.7KB/s   00:00    
response_body                                 100%  284KB   2.3MB/s   00:00    
request_headers                               100%  358    47.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    32.6KB/s   00:00    
pickled_meta                                  100%  157    18.6KB/s   00:00    
response_headers                              100%  581    99.7KB/s   00:00    
response_body                                 100%  287KB   4.2MB/s   00:00    
request_headers                               100%  358    44.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  195    22.0KB/s   00:00    
pickled_meta                                  100%  139    20.7KB/s   00:00    
response_headers                              100%  706   107.3KB/s   00:00    
response_body                                 100%  295KB   2.5MB/s   00:00    
request_headers                               100%  246    13.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  196    27.5KB/s   00:00    
pickled_meta                                  100%  140    12.1KB/s   00:00    
response_headers                              100%  634    56.0KB/s   00:00    
response_body                                 100%  232KB   1.6MB/s   00:00    
request_headers                               100%  246     2.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  228    37.7KB/s   00:00    
pickled_meta                                  100%  155    20.9KB/s   00:00    
response_headers                              100%  582    95.9KB/s   00:00    
response_body                                 100%  290KB   1.9MB/s   00:00    
request_headers                               100%  358    56.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  194    25.4KB/s   00:00    
pickled_meta                                  100%  138     5.7KB/s   00:00    
response_headers                              100%  706    13.4KB/s   00:00    
response_body                                 100%  305KB   1.5MB/s   00:00    
request_headers                               100%  246    30.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  228    17.5KB/s   00:00    
pickled_meta                                  100%  156    24.8KB/s   00:00    
response_headers                              100%  582    71.9KB/s   00:00    
response_body                                 100%  276KB   2.2MB/s   00:00    
request_headers                               100%  358    44.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  231    26.3KB/s   00:00    
pickled_meta                                  100%  157    22.9KB/s   00:00    
response_headers                              100%  582    79.7KB/s   00:00    
response_body                                 100%  284KB   3.9MB/s   00:00    
request_headers                               100%  358    45.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    13.0KB/s   00:00    
pickled_meta                                  100%  156    13.8KB/s   00:00    
response_headers                              100%  584    27.4KB/s   00:00    
response_body                                 100%  283KB   4.1MB/s   00:00    
request_headers                               100%  357    44.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    34.9KB/s   00:00    
pickled_meta                                  100%  157    23.8KB/s   00:00    
response_headers                              100%  582    89.2KB/s   00:00    
response_body                                 100%  287KB   3.7MB/s   00:00    
request_headers                               100%  358    32.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    21.1KB/s   00:00    
pickled_meta                                  100%  156    20.9KB/s   00:00    
response_headers                              100%  582    20.7KB/s   00:00    
response_body                                 100%  304KB   4.8MB/s   00:00    
request_headers                               100%  358    54.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  229    26.8KB/s   00:00    
pickled_meta                                  100%  157    22.7KB/s   00:00    
response_headers                              100%  582    84.1KB/s   00:00    
response_body                                 100%  285KB   1.7MB/s   00:00    
request_headers                               100%  357    19.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    17.1KB/s   00:00    
pickled_meta                                  100%  157    20.6KB/s   00:00    
response_headers                              100%  582    63.4KB/s   00:00    
response_body                                 100%  283KB   1.9MB/s   00:00    
request_headers                               100%  357    22.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    28.0KB/s   00:00    
pickled_meta                                  100%  156    14.5KB/s   00:00    
response_headers                              100%  582    61.2KB/s   00:00    
response_body                                 100%  291KB   2.4MB/s   00:00    
request_headers                               100%  358    29.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    31.2KB/s   00:00    
pickled_meta                                  100%  156    21.6KB/s   00:00    
response_headers                              100%  563    45.1KB/s   00:00    
response_body                                 100%  331KB   2.6MB/s   00:00    
request_headers                               100%  358    45.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  231    33.5KB/s   00:00    
pickled_meta                                  100%  157     5.0KB/s   00:00    
response_headers                              100%  582    85.7KB/s   00:00    
response_body                                 100%  284KB   2.9MB/s   00:00    
request_headers                               100%  357    15.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    27.2KB/s   00:00    
pickled_meta                                  100%  157     6.4KB/s   00:00    
response_headers                              100%  582    98.1KB/s   00:00    
response_body                                 100%  311KB   2.5MB/s   00:00    
request_headers                               100%  358    54.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  231    31.9KB/s   00:00    
pickled_meta                                  100%  157    13.0KB/s   00:00    
response_headers                              100%  582    84.2KB/s   00:00    
response_body                                 100%  319KB   1.1MB/s   00:00    
request_headers                               100%  358    26.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  229     7.4KB/s   00:00    
pickled_meta                                  100%  156    21.5KB/s   00:00    
response_headers                              100%  582    88.5KB/s   00:00    
response_body                                 100%  280KB   2.3MB/s   00:00    
request_headers                               100%  357    41.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232     6.4KB/s   00:00    
pickled_meta                                  100%  157     5.6KB/s   00:00    
response_headers                              100%  581    77.1KB/s   00:00    
response_body                                 100%  290KB   3.9MB/s   00:00    
request_headers                               100%  357    49.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  198    31.6KB/s   00:00    
pickled_meta                                  100%  140    20.9KB/s   00:00    
response_headers                              100%  706   101.6KB/s   00:00    
response_body                                 100%  362KB   3.9MB/s   00:00    
request_headers                               100%  246    37.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    34.0KB/s   00:00    
pickled_meta                                  100%  157    17.7KB/s   00:00    
response_headers                              100%  582    40.1KB/s   00:00    
response_body                                 100%  314KB   1.5MB/s   00:00    
request_headers                               100%  358    12.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    12.5KB/s   00:00    
pickled_meta                                  100%  156    22.5KB/s   00:00    
response_headers                              100%  581    69.7KB/s   00:00    
response_body                                 100%  287KB   2.9MB/s   00:00    
request_headers                               100%  357    59.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    41.4KB/s   00:00    
pickled_meta                                  100%  157    18.6KB/s   00:00    
response_headers                              100%  581    83.4KB/s   00:00    
response_body                                 100%  285KB   5.0MB/s   00:00    
request_headers                               100%  357    48.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    23.1KB/s   00:00    
pickled_meta                                  100%  157    24.2KB/s   00:00    
response_headers                              100%  582    69.0KB/s   00:00    
response_body                                 100%  291KB   4.6MB/s   00:00    
request_headers                               100%  357    13.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    17.2KB/s   00:00    
pickled_meta                                  100%  156    10.5KB/s   00:00    
response_headers                              100%  582    35.0KB/s   00:00    
response_body                                 100%  279KB   2.1MB/s   00:00    
request_headers                               100%  357    37.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    38.0KB/s   00:00    
pickled_meta                                  100%  157    23.0KB/s   00:00    
response_headers                              100%  582    23.8KB/s   00:00    
response_body                                 100%  280KB   1.5MB/s   00:00    
request_headers                               100%  357    25.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    20.1KB/s   00:00    
pickled_meta                                  100%  157    21.3KB/s   00:00    
response_headers                              100%  582    86.2KB/s   00:00    
response_body                                 100%  288KB   2.8MB/s   00:00    
request_headers                               100%  357    18.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    31.7KB/s   00:00    
pickled_meta                                  100%  156    16.9KB/s   00:00    
response_headers                              100%  582     1.7KB/s   00:00    
response_body                                 100%  271KB   2.4MB/s   00:00    
request_headers                               100%  357    55.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    14.6KB/s   00:00    
pickled_meta                                  100%  156    17.5KB/s   00:00    
response_headers                              100%  582    81.9KB/s   00:00    
response_body                                 100%  295KB   2.1MB/s   00:00    
request_headers                               100%  357    52.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    19.7KB/s   00:00    
pickled_meta                                  100%  157     9.1KB/s   00:00    
response_headers                              100%  563    42.4KB/s   00:00    
response_body                                 100%  288KB   1.1MB/s   00:00    
request_headers                               100%  357    10.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    21.0KB/s   00:00    
pickled_meta                                  100%  156     7.3KB/s   00:00    
response_headers                              100%  582    50.4KB/s   00:00    
response_body                                 100%  280KB   2.1MB/s   00:00    
request_headers                               100%  357    50.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    26.2KB/s   00:00    
pickled_meta                                  100%  157    22.3KB/s   00:00    
response_headers                              100%  563    68.8KB/s   00:00    
response_body                                 100%  285KB   2.1MB/s   00:00    
request_headers                               100%  357    51.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    24.2KB/s   00:00    
pickled_meta                                  100%  157    22.2KB/s   00:00    
response_headers                              100%  563    85.7KB/s   00:00    
response_body                                 100%  283KB   2.0MB/s   00:00    
request_headers                               100%  359    57.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    21.7KB/s   00:00    
pickled_meta                                  100%  157    13.3KB/s   00:00    
response_headers                              100%  581    56.5KB/s   00:00    
response_body                                 100%  278KB   1.4MB/s   00:00    
request_headers                               100%  357    55.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  229    36.2KB/s   00:00    
pickled_meta                                  100%  156    24.7KB/s   00:00    
response_headers                              100%  582    86.3KB/s   00:00    
response_body                                 100%  311KB   4.6MB/s   00:00    
request_headers                               100%  359    43.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    40.4KB/s   00:00    
pickled_meta                                  100%  157    16.3KB/s   00:00    
response_headers                              100%  582   102.7KB/s   00:00    
response_body                                 100%  293KB   4.1MB/s   00:00    
request_headers                               100%  358    49.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  231    10.5KB/s   00:00    
pickled_meta                                  100%  157    12.0KB/s   00:00    
response_headers                              100%  582    95.4KB/s   00:00    
response_body                                 100%  294KB   1.3MB/s   00:00    
request_headers                               100%  358    34.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    27.9KB/s   00:00    
pickled_meta                                  100%  156     7.0KB/s   00:00    
response_headers                              100%  582    41.2KB/s   00:00    
response_body                                 100%  293KB   4.1MB/s   00:00    
request_headers                               100%  358    44.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    26.0KB/s   00:00    
pickled_meta                                  100%  156    15.4KB/s   00:00    
response_headers                              100%  582    70.2KB/s   00:00    
response_body                                 100%  283KB   3.9MB/s   00:00    
request_headers                               100%  359    43.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    28.3KB/s   00:00    
pickled_meta                                  100%  157    22.1KB/s   00:00    
response_headers                              100%  582    82.6KB/s   00:00    
response_body                                 100%  274KB   4.3MB/s   00:00    
request_headers                               100%  359    36.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    32.2KB/s   00:00    
pickled_meta                                  100%  157    24.1KB/s   00:00    
response_headers                              100%  581    76.4KB/s   00:00    
response_body                                 100%  277KB   2.5MB/s   00:00    
request_headers                               100%  359    16.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  228    16.1KB/s   00:00    
pickled_meta                                  100%  156    21.4KB/s   00:00    
response_headers                              100%  581    89.2KB/s   00:00    
response_body                                 100%  283KB   2.9MB/s   00:00    
request_headers                               100%  359    50.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  229    21.5KB/s   00:00    
pickled_meta                                  100%  156    19.0KB/s   00:00    
response_headers                              100%  581    26.4KB/s   00:00    
response_body                                 100%  292KB   3.1MB/s   00:00    
request_headers                               100%  359    46.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    15.5KB/s   00:00    
pickled_meta                                  100%  157     7.5KB/s   00:00    
response_headers                              100%  582    29.7KB/s   00:00    
response_body                                 100%  304KB   2.4MB/s   00:00    
request_headers                               100%  358    58.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    11.8KB/s   00:00    
pickled_meta                                  100%  156     7.5KB/s   00:00    
response_headers                              100%  563    20.8KB/s   00:00    
response_body                                 100%  277KB   2.8MB/s   00:00    
request_headers                               100%  359    19.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    14.3KB/s   00:00    
pickled_meta                                  100%  157    26.7KB/s   00:00    
response_headers                              100%  582    88.8KB/s   00:00    
response_body                                 100%  281KB 680.5KB/s   00:00    
request_headers                               100%  359     5.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232     2.6KB/s   00:00    
pickled_meta                                  100%  157    28.4KB/s   00:00    
response_headers                              100%  563    36.2KB/s   00:00    
response_body                                 100%  281KB   1.8MB/s   00:00    
request_headers                               100%  359    32.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    27.6KB/s   00:00    
pickled_meta                                  100%  156    23.7KB/s   00:00    
response_headers                              100%  581    74.9KB/s   00:00    
response_body                                 100%  281KB   3.0MB/s   00:00    
request_headers                               100%  359    54.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    16.7KB/s   00:00    
pickled_meta                                  100%  156    12.5KB/s   00:00    
response_headers                              100%  581    68.8KB/s   00:00    
response_body                                 100%  276KB   4.8MB/s   00:00    
request_headers                               100%  359    38.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    26.0KB/s   00:00    
pickled_meta                                  100%  156    19.7KB/s   00:00    
response_headers                              100%  582    50.9KB/s   00:00    
response_body                                 100%  282KB   2.4MB/s   00:00    
request_headers                               100%  359    41.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    31.0KB/s   00:00    
pickled_meta                                  100%  157    21.2KB/s   00:00    
response_headers                              100%  582    94.4KB/s   00:00    
response_body                                 100%  296KB   4.8MB/s   00:00    
request_headers                               100%  359    53.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  228    15.4KB/s   00:00    
pickled_meta                                  100%  155    15.4KB/s   00:00    
response_headers                              100%  563    64.8KB/s   00:00    
response_body                                 100%  284KB   1.8MB/s   00:00    
request_headers                               100%  359    27.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    28.6KB/s   00:00    
pickled_meta                                  100%  156     6.2KB/s   00:00    
response_headers                              100%  563    68.9KB/s   00:00    
response_body                                 100%  294KB   2.9MB/s   00:00    
request_headers                               100%  357    17.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    27.9KB/s   00:00    
pickled_meta                                  100%  157    18.1KB/s   00:00    
response_headers                              100%  582    59.0KB/s   00:00    
response_body                                 100%  299KB   2.1MB/s   00:00    
request_headers                               100%  359    57.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    12.4KB/s   00:00    
pickled_meta                                  100%  157    12.8KB/s   00:00    
response_headers                              100%  582     7.3KB/s   00:00    
response_body                                 100%  294KB   2.1MB/s   00:00    
request_headers                               100%  358    19.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    29.7KB/s   00:00    
pickled_meta                                  100%  157    21.9KB/s   00:00    
response_headers                              100%  582    17.6KB/s   00:00    
response_body                                 100%  300KB   4.7MB/s   00:00    
request_headers                               100%  358    53.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    35.3KB/s   00:00    
pickled_meta                                  100%  157    19.2KB/s   00:00    
response_headers                              100%  582    60.6KB/s   00:00    
response_body                                 100%  297KB   7.6MB/s   00:00    
request_headers                               100%  358    49.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    35.3KB/s   00:00    
pickled_meta                                  100%  157    22.5KB/s   00:00    
response_headers                              100%  582    94.5KB/s   00:00    
response_body                                 100%  296KB   4.9MB/s   00:00    
request_headers                               100%  358    52.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    34.3KB/s   00:00    
pickled_meta                                  100%  156    17.6KB/s   00:00    
response_headers                              100%  582    95.9KB/s   00:00    
response_body                                 100%  298KB   5.8MB/s   00:00    
request_headers                               100%  358    20.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    17.6KB/s   00:00    
pickled_meta                                  100%  156    12.9KB/s   00:00    
response_headers                              100%  563    72.3KB/s   00:00    
response_body                                 100%  300KB   4.5MB/s   00:00    
request_headers                               100%  357    16.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    28.0KB/s   00:00    
pickled_meta                                  100%  156    14.7KB/s   00:00    
response_headers                              100%  582    46.1KB/s   00:00    
response_body                                 100%  287KB   4.6MB/s   00:00    
request_headers                               100%  357    41.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    20.3KB/s   00:00    
pickled_meta                                  100%  156    19.5KB/s   00:00    
response_headers                              100%  563    63.6KB/s   00:00    
response_body                                 100%  319KB   5.3MB/s   00:00    
request_headers                               100%  357    54.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  231    35.8KB/s   00:00    
pickled_meta                                  100%  157    19.6KB/s   00:00    
response_headers                              100%  581    61.4KB/s   00:00    
response_body                                 100%  300KB   4.8MB/s   00:00    
request_headers                               100%  358    57.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  192    13.4KB/s   00:00    
pickled_meta                                  100%  138     8.1KB/s   00:00    
response_headers                              100%  634    23.6KB/s   00:00    
response_body                                 100%  232KB   4.3MB/s   00:00    
request_headers                               100%  246    30.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    33.7KB/s   00:00    
pickled_meta                                  100%  157    29.2KB/s   00:00    
response_headers                              100%  581    50.5KB/s   00:00    
response_body                                 100%  299KB   4.9MB/s   00:00    
request_headers                               100%  358    54.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    21.4KB/s   00:00    
pickled_meta                                  100%  157    15.2KB/s   00:00    
response_headers                              100%  582    57.9KB/s   00:00    
response_body                                 100%  325KB   2.4MB/s   00:00    
request_headers                               100%  358    24.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    38.8KB/s   00:00    
pickled_meta                                  100%  157    16.2KB/s   00:00    
response_headers                              100%  563    53.5KB/s   00:00    
response_body                                 100%  289KB   3.5MB/s   00:00    
request_headers                               100%  358    26.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  230    17.2KB/s   00:00    
pickled_meta                                  100%  156    20.5KB/s   00:00    
response_headers                              100%  563    61.4KB/s   00:00    
response_body                                 100%  314KB   4.2MB/s   00:00    
request_headers                               100%  358    35.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    34.7KB/s   00:00    
pickled_meta                                  100%  157    14.3KB/s   00:00    
response_headers                              100%  563    37.1KB/s   00:00    
response_body                                 100%  302KB   3.1MB/s   00:00    
request_headers                               100%  358     1.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  228    18.9KB/s   00:00    
pickled_meta                                  100%  156     9.4KB/s   00:00    
response_headers                              100%  582    52.4KB/s   00:00    
response_body                                 100%  313KB   4.1MB/s   00:00    
request_headers                               100%  358    41.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  231    28.0KB/s   00:00    
pickled_meta                                  100%  157    25.9KB/s   00:00    
response_headers                              100%  582    98.3KB/s   00:00    
response_body                                 100%  303KB   4.0MB/s   00:00    
request_headers                               100%  358    45.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  232    21.5KB/s   00:00    
pickled_meta                                  100%  157    26.3KB/s   00:00    
response_headers                              100%  582    84.8KB/s   00:00    
response_body                                 100%  329KB   4.9MB/s   00:00    
request_headers                               100%  358    61.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  229    27.5KB/s   00:00    
pickled_meta                                  100%  156    24.3KB/s   00:00    
response_headers                              100%  581    84.9KB/s   00:00    
response_body                                 100%  426KB   4.6MB/s   00:00    
request_headers                               100%  358    33.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  196    30.4KB/s   00:00    
pickled_meta                                  100%  140    18.2KB/s   00:00    
response_headers                              100%  634   108.0KB/s   00:00    
response_body                                 100%  232KB   2.9MB/s   00:00    
request_headers                               100%  246    17.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  200    22.2KB/s   00:00    
pickled_meta                                  100%  142    18.4KB/s   00:00    
response_headers                              100%  634   107.7KB/s   00:00    
response_body                                 100%  232KB   6.8MB/s   00:00    
request_headers                               100%  246    31.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  180    24.4KB/s   00:00    
pickled_meta                                  100%  131    21.1KB/s   00:00    
response_headers                              100%  525    45.4KB/s   00:00    
response_body                                 100%  131    16.7KB/s   00:00    
request_headers                               100%  246    42.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  250    27.6KB/s   00:00    
pickled_meta                                  100%  167    20.5KB/s   00:00    
response_headers                              100%  581    47.9KB/s   00:00    
response_body                                 100%  377KB   5.6MB/s   00:00    
request_headers                               100%  397    52.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  263    36.8KB/s   00:00    
pickled_meta                                  100%  173    20.7KB/s   00:00    
response_headers                              100%  563    56.3KB/s   00:00    
response_body                                 100%  357KB   4.9MB/s   00:00    
request_headers                               100%  408    68.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  272    27.1KB/s   00:00    
pickled_meta                                  100%  177    18.5KB/s   00:00    
response_headers                              100%  581    87.2KB/s   00:00    
response_body                                 100%  378KB   4.1MB/s   00:00    
request_headers                               100%  406    40.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  280    28.5KB/s   00:00    
pickled_meta                                  100%  181    26.5KB/s   00:00    
response_headers                              100%  563    59.1KB/s   00:00    
response_body                                 100%  353KB   4.2MB/s   00:00    
request_headers                               100%  401    47.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  264    31.1KB/s   00:00    
pickled_meta                                  100%  173    16.2KB/s   00:00    
response_headers                              100%  581    73.0KB/s   00:00    
response_body                                 100%  353KB   4.2MB/s   00:00    
request_headers                               100%  399    44.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  287    38.4KB/s   00:00    
pickled_meta                                  100%  185    31.7KB/s   00:00    
response_headers                              100%  687   110.4KB/s   00:00    
response_body                                 100%  336KB   2.2MB/s   00:00    
request_headers                               100%  246    16.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    32.1KB/s   00:00    
pickled_meta                                  100%  175    24.7KB/s   00:00    
response_headers                              100%  563    56.4KB/s   00:00    
response_body                                 100%  372KB   3.2MB/s   00:00    
request_headers                               100%  405    66.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  254    34.4KB/s   00:00    
pickled_meta                                  100%  168    23.6KB/s   00:00    
response_headers                              100%  563    56.9KB/s   00:00    
response_body                                 100%  366KB   3.0MB/s   00:00    
request_headers                               100%  406    24.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  300    37.7KB/s   00:00    
pickled_meta                                  100%  191    23.7KB/s   00:00    
response_headers                              100%  563    67.3KB/s   00:00    
response_body                                 100%  330KB   2.3MB/s   00:00    
request_headers                               100%  297    21.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  258    16.1KB/s   00:00    
pickled_meta                                  100%  170    20.7KB/s   00:00    
response_headers                              100%  563    46.4KB/s   00:00    
response_body                                 100%  361KB   1.6MB/s   00:00    
request_headers                               100%  406    46.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  330    16.0KB/s   00:00    
pickled_meta                                  100%  206     2.0KB/s   00:00    
response_headers                              100%  687    33.3KB/s   00:00    
response_body                                 100%  709KB   1.4MB/s   00:00    
request_headers                               100%  246    20.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  262    23.7KB/s   00:00    
pickled_meta                                  100%  172    19.9KB/s   00:00    
response_headers                              100%  581    87.5KB/s   00:00    
response_body                                 100%  373KB   1.6MB/s   00:00    
request_headers                               100%  394    13.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  274    14.6KB/s   00:00    
pickled_meta                                  100%  178    21.6KB/s   00:00    
response_headers                              100%  582    55.2KB/s   00:00    
response_body                                 100%  339KB   1.4MB/s   00:00    
request_headers                               100%  412    12.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  290    34.9KB/s   00:00    
pickled_meta                                  100%  186     5.6KB/s   00:00    
response_headers                              100%  563    19.7KB/s   00:00    
response_body                                 100%  339KB   2.7MB/s   00:00    
request_headers                               100%  297    33.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  251    35.0KB/s   00:00    
pickled_meta                                  100%  167    19.0KB/s   00:00    
response_headers                              100%  581    78.5KB/s   00:00    
response_body                                 100%  380KB   2.3MB/s   00:00    
request_headers                               100%  399    34.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  262    34.6KB/s   00:00    
pickled_meta                                  100%  172    13.6KB/s   00:00    
response_headers                              100%  581    56.0KB/s   00:00    
response_body                                 100%  369KB   2.9MB/s   00:00    
request_headers                               100%  406    59.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  270    43.2KB/s   00:00    
pickled_meta                                  100%  176    19.7KB/s   00:00    
response_headers                              100%  582    92.2KB/s   00:00    
response_body                                 100%  370KB   5.0MB/s   00:00    
request_headers                               100%  397    54.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  289    25.9KB/s   00:00    
pickled_meta                                  100%  186    10.3KB/s   00:00    
response_headers                              100%  687    91.2KB/s   00:00    
response_body                                 100%  340KB   6.1MB/s   00:00    
request_headers                               100%  246    34.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  304    43.1KB/s   00:00    
pickled_meta                                  100%  193    33.3KB/s   00:00    
response_headers                              100%  706   115.6KB/s   00:00    
response_body                                 100%  346KB   4.2MB/s   00:00    
request_headers                               100%  246    14.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  256    18.7KB/s   00:00    
pickled_meta                                  100%  169    12.6KB/s   00:00    
response_headers                              100%  582    90.8KB/s   00:00    
response_body                                 100%  359KB   4.3MB/s   00:00    
request_headers                               100%  394    58.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  260    41.6KB/s   00:00    
pickled_meta                                  100%  171     0.8KB/s   00:00    
response_headers                              100%  582    87.8KB/s   00:00    
response_body                                 100%  363KB   3.2MB/s   00:00    
request_headers                               100%  412    30.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  274     8.7KB/s   00:00    
pickled_meta                                  100%  178    21.0KB/s   00:00    
response_headers                              100%  705    92.9KB/s   00:00    
response_body                                 100%  362KB   4.1MB/s   00:00    
request_headers                               100%  246    14.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  284    21.0KB/s   00:00    
pickled_meta                                  100%  183    17.8KB/s   00:00    
response_headers                              100%  581    96.7KB/s   00:00    
response_body                                 100%  360KB   4.2MB/s   00:00    
request_headers                               100%  400    61.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  261    18.5KB/s   00:00    
pickled_meta                                  100%  172    23.5KB/s   00:00    
response_headers                              100%  563    61.8KB/s   00:00    
response_body                                 100%  399KB   3.6MB/s   00:00    
request_headers                               100%  405    70.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  291    42.1KB/s   00:00    
pickled_meta                                  100%  187    21.2KB/s   00:00    
response_headers                              100%  706    78.0KB/s   00:00    
response_body                                 100%  321KB   3.6MB/s   00:00    
request_headers                               100%  246    29.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  270    21.8KB/s   00:00    
pickled_meta                                  100%  176    23.0KB/s   00:00    
response_headers                              100%  563    53.8KB/s   00:00    
response_body                                 100%  353KB   2.9MB/s   00:00    
request_headers                               100%  401    41.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  304    22.4KB/s   00:00    
pickled_meta                                  100%  193    26.8KB/s   00:00    
response_headers                              100%  705    27.4KB/s   00:00    
response_body                                 100%  334KB   4.1MB/s   00:00    
request_headers                               100%  246    25.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  294    33.4KB/s   00:00    
pickled_meta                                  100%  188    35.7KB/s   00:00    
response_headers                              100%  582    89.4KB/s   00:00    
response_body                                 100%  358KB   4.1MB/s   00:00    
request_headers                               100%  403    56.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  251    27.1KB/s   00:00    
pickled_meta                                  100%  167    12.6KB/s   00:00    
response_headers                              100%  563    80.9KB/s   00:00    
response_body                                 100%  342KB   3.3MB/s   00:00    
request_headers                               100%  408    55.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    25.6KB/s   00:00    
pickled_meta                                  100%  174    26.6KB/s   00:00    
response_headers                              100%  582    45.6KB/s   00:00    
response_body                                 100%  367KB   3.7MB/s   00:00    
request_headers                               100%  398    48.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  262    24.3KB/s   00:00    
pickled_meta                                  100%  172    27.3KB/s   00:00    
response_headers                              100%  563    67.6KB/s   00:00    
response_body                                 100%  351KB   2.6MB/s   00:00    
request_headers                               100%  397    59.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  254    39.4KB/s   00:00    
pickled_meta                                  100%  168    23.2KB/s   00:00    
response_headers                              100%  581    42.6KB/s   00:00    
response_body                                 100%  356KB   3.8MB/s   00:00    
request_headers                               100%  401    62.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  264    19.7KB/s   00:00    
pickled_meta                                  100%  173    27.7KB/s   00:00    
response_headers                              100%  563    74.1KB/s   00:00    
response_body                                 100%  357KB   5.5MB/s   00:00    
request_headers                               100%  402    27.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  267    39.5KB/s   00:00    
pickled_meta                                  100%  175    26.3KB/s   00:00    
response_headers                              100%  563    79.9KB/s   00:00    
response_body                                 100%  372KB   3.2MB/s   00:00    
request_headers                               100%  408    39.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  298    40.9KB/s   00:00    
pickled_meta                                  100%  190    26.0KB/s   00:00    
response_headers                              100%  706   102.4KB/s   00:00    
response_body                                 100%  343KB   5.3MB/s   00:00    
request_headers                               100%  246    41.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    27.7KB/s   00:00    
pickled_meta                                  100%  174    30.5KB/s   00:00    
response_headers                              100%  582    56.5KB/s   00:00    
response_body                                 100%  371KB   4.3MB/s   00:00    
request_headers                               100%  425     9.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  258    32.2KB/s   00:00    
pickled_meta                                  100%  170    20.4KB/s   00:00    
response_headers                              100%  581    92.0KB/s   00:00    
response_body                                 100%  362KB   3.8MB/s   00:00    
request_headers                               100%  410    32.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  308    44.8KB/s   00:00    
pickled_meta                                  100%  195    28.4KB/s   00:00    
response_headers                              100%  582    35.6KB/s   00:00    
response_body                                 100%  378KB   4.5MB/s   00:00    
request_headers                               100%  297    49.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  264    36.4KB/s   00:00    
pickled_meta                                  100%  173    19.4KB/s   00:00    
response_headers                              100%  563    62.4KB/s   00:00    
response_body                                 100%  363KB   4.9MB/s   00:00    
request_headers                               100%  401    31.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  252    36.9KB/s   00:00    
pickled_meta                                  100%  167    24.7KB/s   00:00    
response_headers                              100%  582    32.4KB/s   00:00    
response_body                                 100%  364KB   2.9MB/s   00:00    
request_headers                               100%  401    57.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    26.6KB/s   00:00    
pickled_meta                                  100%  175    23.7KB/s   00:00    
response_headers                              100%  563    83.0KB/s   00:00    
response_body                                 100%  365KB   3.2MB/s   00:00    
request_headers                               100%  397    46.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  304    33.7KB/s   00:00    
pickled_meta                                  100%  193    15.3KB/s   00:00    
response_headers                              100%  706    80.5KB/s   00:00    
response_body                                 100%  351KB   5.0MB/s   00:00    
request_headers                               100%  246    40.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  260    39.1KB/s   00:00    
pickled_meta                                  100%  171    26.0KB/s   00:00    
response_headers                              100%  581    42.8KB/s   00:00    
response_body                                 100%  366KB   5.9MB/s   00:00    
request_headers                               100%  397    56.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  257    40.3KB/s   00:00    
pickled_meta                                  100%  170    27.5KB/s   00:00    
response_headers                              100%  563    81.3KB/s   00:00    
response_body                                 100%  356KB   4.8MB/s   00:00    
request_headers                               100%  406    60.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    48.0KB/s   00:00    
pickled_meta                                  100%  175    20.0KB/s   00:00    
response_headers                              100%  582    84.3KB/s   00:00    
response_body                                 100%  349KB   4.4MB/s   00:00    
request_headers                               100%  410     2.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  282    32.5KB/s   00:00    
pickled_meta                                  100%  182    21.9KB/s   00:00    
response_headers                              100%  582    60.9KB/s   00:00    
response_body                                 100%  361KB   2.5MB/s   00:00    
request_headers                               100%  397    41.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  304    41.5KB/s   00:00    
pickled_meta                                  100%  193    32.2KB/s   00:00    
response_headers                              100%  687    97.8KB/s   00:00    
response_body                                 100%  327KB   4.4MB/s   00:00    
request_headers                               100%  246    32.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  260    42.1KB/s   00:00    
pickled_meta                                  100%  171    25.4KB/s   00:00    
response_headers                              100%  582    85.5KB/s   00:00    
response_body                                 100%  346KB   2.6MB/s   00:00    
request_headers                               100%  409    42.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  258    33.7KB/s   00:00    
pickled_meta                                  100%  170    25.5KB/s   00:00    
response_headers                              100%  582    77.9KB/s   00:00    
response_body                                 100%  365KB   5.1MB/s   00:00    
request_headers                               100%  413    60.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  272    36.3KB/s   00:00    
pickled_meta                                  100%  177    19.9KB/s   00:00    
response_headers                              100%  581    89.2KB/s   00:00    
response_body                                 100%  382KB   3.5MB/s   00:00    
request_headers                               100%  395    45.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  256    14.3KB/s   00:00    
pickled_meta                                  100%  169    14.0KB/s   00:00    
response_headers                              100%  582    47.8KB/s   00:00    
response_body                                 100%  378KB   2.5MB/s   00:00    
request_headers                               100%  408    58.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  254    34.2KB/s   00:00    
pickled_meta                                  100%  169    27.1KB/s   00:00    
response_headers                              100%  563    86.5KB/s   00:00    
response_body                                 100%  353KB   3.5MB/s   00:00    
request_headers                               100%  395    59.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  259    26.8KB/s   00:00    
pickled_meta                                  100%  171    19.8KB/s   00:00    
response_headers                              100%  581    91.7KB/s   00:00    
response_body                                 100%  366KB   3.4MB/s   00:00    
request_headers                               100%  400    42.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  281    34.4KB/s   00:00    
pickled_meta                                  100%  182    13.8KB/s   00:00    
response_headers                              100%  582    70.0KB/s   00:00    
response_body                                 100%  336KB   3.7MB/s   00:00    
request_headers                               100%  297    50.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  271    42.1KB/s   00:00    
pickled_meta                                  100%  177    33.6KB/s   00:00    
response_headers                              100%  563    86.8KB/s   00:00    
response_body                                 100%  366KB   4.0MB/s   00:00    
request_headers                               100%  402    67.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  285    29.9KB/s   00:00    
pickled_meta                                  100%  184     6.8KB/s   00:00    
response_headers                              100%  706    96.9KB/s   00:00    
response_body                                 100%  327KB   4.5MB/s   00:00    
request_headers                               100%  246    30.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  276    23.3KB/s   00:00    
pickled_meta                                  100%  179    30.4KB/s   00:00    
response_headers                              100%  581    87.4KB/s   00:00    
response_body                                 100%  358KB   3.7MB/s   00:00    
request_headers                               100%  414    61.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  282    24.9KB/s   00:00    
pickled_meta                                  100%  182    26.9KB/s   00:00    
response_headers                              100%  582   103.4KB/s   00:00    
response_body                                 100%  366KB   5.5MB/s   00:00    
request_headers                               100%  409    58.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  252    20.7KB/s   00:00    
pickled_meta                                  100%  168    21.1KB/s   00:00    
response_headers                              100%  581    73.6KB/s   00:00    
response_body                                 100%  351KB   4.0MB/s   00:00    
request_headers                               100%  401    58.9KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  276    42.1KB/s   00:00    
pickled_meta                                  100%  179    31.5KB/s   00:00    
response_headers                              100%  706    97.5KB/s   00:00    
response_body                                 100%  357KB   4.4MB/s   00:00    
request_headers                               100%  246    36.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  258    28.6KB/s   00:00    
pickled_meta                                  100%  170    25.9KB/s   00:00    
response_headers                              100%  582    78.3KB/s   00:00    
response_body                                 100%  377KB   3.2MB/s   00:00    
request_headers                               100%  397    55.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  277    44.1KB/s   00:00    
pickled_meta                                  100%  180    24.5KB/s   00:00    
response_headers                              100%  563    64.3KB/s   00:00    
response_body                                 100%  344KB   3.4MB/s   00:00    
request_headers                               100%  297    43.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  278    39.0KB/s   00:00    
pickled_meta                                  100%  180    29.5KB/s   00:00    
response_headers                              100%  687    84.8KB/s   00:00    
response_body                                 100%  347KB   3.7MB/s   00:00    
request_headers                               100%  246    39.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  275    28.0KB/s   00:00    
pickled_meta                                  100%  179    24.3KB/s   00:00    
response_headers                              100%  582    82.8KB/s   00:00    
response_body                                 100%  343KB   2.4MB/s   00:00    
request_headers                               100%  399    31.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  256    25.2KB/s   00:00    
pickled_meta                                  100%  169    22.1KB/s   00:00    
response_headers                              100%  581    76.0KB/s   00:00    
response_body                                 100%  379KB   2.2MB/s   00:00    
request_headers                               100%  421    61.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    29.7KB/s   00:00    
pickled_meta                                  100%  175    26.5KB/s   00:00    
response_headers                              100%  563    64.8KB/s   00:00    
response_body                                 100%  359KB   2.5MB/s   00:00    
request_headers                               100%  400    49.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    27.0KB/s   00:00    
pickled_meta                                  100%  174    23.2KB/s   00:00    
response_headers                              100%  582   104.4KB/s   00:00    
response_body                                 100%  359KB   3.5MB/s   00:00    
request_headers                               100%  400    57.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  280    39.7KB/s   00:00    
pickled_meta                                  100%  181    26.6KB/s   00:00    
response_headers                              100%  582    69.7KB/s   00:00    
response_body                                 100%  341KB   3.0MB/s   00:00    
request_headers                               100%  297    46.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  276    34.7KB/s   00:00    
pickled_meta                                  100%  179    26.0KB/s   00:00    
response_headers                              100%  563    89.1KB/s   00:00    
response_body                                 100%  365KB   3.4MB/s   00:00    
request_headers                               100%  405    65.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  262    25.5KB/s   00:00    
pickled_meta                                  100%  172     9.8KB/s   00:00    
response_headers                              100%  582    73.4KB/s   00:00    
response_body                                 100%  371KB   4.4MB/s   00:00    
request_headers                               100%  406    44.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    28.5KB/s   00:00    
pickled_meta                                  100%  174    21.2KB/s   00:00    
response_headers                              100%  581    98.4KB/s   00:00    
response_body                                 100%  353KB   2.8MB/s   00:00    
request_headers                               100%  404    51.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  251    29.2KB/s   00:00    
pickled_meta                                  100%  167    26.9KB/s   00:00    
response_headers                              100%  582    83.5KB/s   00:00    
response_body                                 100%  384KB   4.0MB/s   00:00    
request_headers                               100%  402    37.8KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  272    22.0KB/s   00:00    
pickled_meta                                  100%  177    28.4KB/s   00:00    
response_headers                              100%  581    82.0KB/s   00:00    
response_body                                 100%  334KB   2.4MB/s   00:00    
request_headers                               100%  421    61.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  278    34.8KB/s   00:00    
pickled_meta                                  100%  180    23.6KB/s   00:00    
response_headers                              100%  581    70.3KB/s   00:00    
response_body                                 100%  351KB   3.2MB/s   00:00    
request_headers                               100%  411    38.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  257    35.9KB/s   00:00    
pickled_meta                                  100%  170    25.3KB/s   00:00    
response_headers                              100%  582   101.7KB/s   00:00    
response_body                                 100%  362KB   4.5MB/s   00:00    
request_headers                               100%  410    57.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  276    20.7KB/s   00:00    
pickled_meta                                  100%  179    21.1KB/s   00:00    
response_headers                              100%  563    70.4KB/s   00:00    
response_body                                 100%  351KB   5.1MB/s   00:00    
request_headers                               100%  414    45.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  280    36.6KB/s   00:00    
pickled_meta                                  100%  181    28.6KB/s   00:00    
response_headers                              100%  563    67.3KB/s   00:00    
response_body                                 100%  368KB   4.8MB/s   00:00    
request_headers                               100%  409    61.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    40.7KB/s   00:00    
pickled_meta                                  100%  174    26.4KB/s   00:00    
response_headers                              100%  582    70.6KB/s   00:00    
response_body                                 100%  367KB   4.9MB/s   00:00    
request_headers                               100%  401    55.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  254    29.6KB/s   00:00    
pickled_meta                                  100%  168    20.3KB/s   00:00    
response_headers                              100%  563    42.9KB/s   00:00    
response_body                                 100%  354KB   6.0MB/s   00:00    
request_headers                               100%  397    61.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    34.7KB/s   00:00    
pickled_meta                                  100%  174    21.1KB/s   00:00    
response_headers                              100%  581    83.3KB/s   00:00    
response_body                                 100%  322KB   4.7MB/s   00:00    
request_headers                               100%  410    60.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  270    28.2KB/s   00:00    
pickled_meta                                  100%  176    19.1KB/s   00:00    
response_headers                              100%  705   121.3KB/s   00:00    
response_body                                 100%  367KB   5.1MB/s   00:00    
request_headers                               100%  246    39.4KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  265    37.7KB/s   00:00    
pickled_meta                                  100%  174    22.7KB/s   00:00    
response_headers                              100%  563    74.7KB/s   00:00    
response_body                                 100%  365KB   4.6MB/s   00:00    
request_headers                               100%  408    44.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  274    25.2KB/s   00:00    
pickled_meta                                  100%  178    23.7KB/s   00:00    
response_headers                              100%  581    87.2KB/s   00:00    
response_body                                 100%  356KB   3.8MB/s   00:00    
request_headers                               100%  406    95.5KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    40.2KB/s   00:00    
pickled_meta                                  100%  175    17.1KB/s   00:00    
response_headers                              100%  581    97.2KB/s   00:00    
response_body                                 100%  368KB   3.8MB/s   00:00    
request_headers                               100%  402    59.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  290    23.6KB/s   00:00    
pickled_meta                                  100%  186    26.4KB/s   00:00    
response_headers                              100%  706   108.2KB/s   00:00    
response_body                                 100%  329KB   5.4MB/s   00:00    
request_headers                               100%  246    42.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  258    15.9KB/s   00:00    
pickled_meta                                  100%  170    18.4KB/s   00:00    
response_headers                              100%  563    66.6KB/s   00:00    
response_body                                 100%  406KB   2.5MB/s   00:00    
request_headers                               100%  394    59.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    42.6KB/s   00:00    
pickled_meta                                  100%  175    29.6KB/s   00:00    
response_headers                              100%  706   115.0KB/s   00:00    
response_body                                 100%  368KB   3.5MB/s   00:00    
request_headers                               100%  246    32.1KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  264    28.4KB/s   00:00    
pickled_meta                                  100%  173    21.5KB/s   00:00    
response_headers                              100%  581   103.4KB/s   00:00    
response_body                                 100%  380KB   4.6MB/s   00:00    
request_headers                               100%  414    59.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    38.8KB/s   00:00    
pickled_meta                                  100%  174    24.6KB/s   00:00    
response_headers                              100%  563    57.8KB/s   00:00    
response_body                                 100%  350KB   5.5MB/s   00:00    
request_headers                               100%  410    40.2KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  290    38.2KB/s   00:00    
pickled_meta                                  100%  186    27.8KB/s   00:00    
response_headers                              100%  706    96.2KB/s   00:00    
response_body                                 100%  353KB   5.4MB/s   00:00    
request_headers                               100%  246    32.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  268    29.1KB/s   00:00    
pickled_meta                                  100%  175    19.8KB/s   00:00    
response_headers                              100%  581    73.5KB/s   00:00    
response_body                                 100%  370KB   3.0MB/s   00:00    
request_headers                               100%  404    63.7KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  266    32.6KB/s   00:00    
pickled_meta                                  100%  174    27.8KB/s   00:00    
response_headers                              100%  581    69.3KB/s   00:00    
response_body                                 100%  354KB   3.1MB/s   00:00    
request_headers                               100%  413    72.3KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  254    16.7KB/s   00:00    
pickled_meta                                  100%  168    16.6KB/s   00:00    
response_headers                              100%  582    85.5KB/s   00:00    
response_body                                 100%  367KB   3.1MB/s   00:00    
request_headers                               100%  397    53.6KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
meta                                          100%  279    36.0KB/s   00:00    
pickled_meta                                  100%  181    25.4KB/s   00:00    
response_headers                              100%  582    85.9KB/s   00:00    
response_body                                 100%  339KB   2.6MB/s   00:00    
request_headers                               100%  408    60.0KB/s   00:00    
request_body                                  100%    0     0.0KB/s   00:00    
^Zzsh: suspended (signal)  scp -r ftm3@node.zoo.cs.yale.edu:~/transfermarkt-scraper-main .
(base) fishermarks@Fishers-MBP Downloads % ssh ftm3@node.zoo.cs.yale.edu
Enter passphrase for key '/Users/fishermarks/.ssh/id_rsa': 
Last login: Wed Oct 18 20:17:28 2023 from 98.238.126.217
                                  Welcome!


                  If you are missing a course directory, create it with
                  $ sudo register csXYZ
                  Please report any issues to cs.support@yale.edu.

                  REBOOT CYCLE:  Every Thursday ~07:00
[ftm3@viper ~]$ cd soccerdata
[ftm3@viper soccerdata]$ ls
config  data  logs
[ftm3@viper soccerdata]$ cd ..
[ftm3@viper ~]$ cd soccerdata-master
[ftm3@viper soccerdata-master]$ ls
CONTRIBUTING.rst  Makefile      output          README.rst  tests
docs              my_scrape.py  poetry.lock     setup.cfg
LICENSE.rst       noxfile.py    pyproject.toml  soccerdata
[ftm3@viper soccerdata-master]$ ls
CONTRIBUTING.rst  Makefile      output          README.rst  tests
docs              my_scrape.py  poetry.lock     setup.cfg
LICENSE.rst       noxfile.py    pyproject.toml  soccerdata
[ftm3@viper soccerdata-master]$ cd soccerdata
[ftm3@viper soccerdata]$ ls
clubelo.py  espn.py             __init__.py       sofifa.py
_common.py  fbref.py            match_history.py  whoscored.py
_config.py  fivethirtyeight.py  __pycache__
[ftm3@viper soccerdata]$ ls -l
total 200
-rw-rw-r-- 1 ftm3 ftm3  6382 Nov 13 14:54 clubelo.py
-rw-rw-r-- 1 ftm3 ftm3 21223 Nov 13 14:54 _common.py
-rw-rw-r-- 1 ftm3 ftm3  5829 Nov 13 16:39 _config.py
-rw-rw-r-- 1 ftm3 ftm3 12890 Nov 13 14:54 espn.py
-rw-rw-r-- 1 ftm3 ftm3 47108 Nov 13 16:39 fbref.py
-rw-rw-r-- 1 ftm3 ftm3  8536 Nov 13 14:54 fivethirtyeight.py
-rw-rw-r-- 1 ftm3 ftm3   457 Nov 13 14:54 __init__.py
-rw-rw-r-- 1 ftm3 ftm3  4657 Nov 13 14:54 match_history.py
drwxrwxr-x 2 ftm3 ftm3  4096 Nov 13 16:39 __pycache__
-rw-rw-r-- 1 ftm3 ftm3 16859 Nov 13 14:54 sofifa.py
-rw-rw-r-- 1 ftm3 ftm3 33034 Nov 13 14:54 whoscored.py
[ftm3@viper soccerdata]$ cd fbref.py
-bash: cd: fbref.py: Not a directory
[ftm3@viper soccerdata]$ vim fbref.py
[ftm3@viper soccerdata]$ client_loop: send disconnect: Broken pipe
(base) fishermarks@Fishers-MBP Downloads % 
  [Restored Dec 4, 2023 at 5:15:16 PM]
Last login: Thu Nov 30 21:36:11 on ttys001
Restored session: Sun Dec  3 19:07:47 EST 2023
(base) fishermarks@Fishers-MacBook-Pro Downloads % ssh ftm3@node.zoo.cs.yale.edu
Warning: Permanently added the ED25519 host key for IP address '10.66.2.194' to the list of known hosts.
Enter passphrase for key '/Users/fishermarks/.ssh/id_rsa': 
Last login: Mon Oct 16 23:38:06 2023 from 172.26.62.240
                                  Welcome!


                  If you are missing a course directory, create it with
                  $ sudo register csXYZ
                  Please report any issues to cs.support@yale.edu.

                  REBOOT CYCLE:  Every Monday ~07:00
[ftm3@peacock ~]$ ls
api.py                  cs421             pset2_test
-cs201-20220531.tar.gz  cs437             soccerdata
cs202                   enigma-simulator  soccerdata-master
-cs223-20220531.tar.gz  hw2-solution      transfermarkt-scraper-main
cs323                   hw5-skeleton      tutorial
cs365                   pset1_test
[ftm3@peacock ~]$ cd soccerdata-master
[ftm3@peacock soccerdata-master]$ ls
CONTRIBUTING.rst  Makefile      output          README.rst  tests
docs              my_scrape.py  poetry.lock     setup.cfg
LICENSE.rst       noxfile.py    pyproject.toml  soccerdata
[ftm3@peacock soccerdata-master]$ cd soccerdata
[ftm3@peacock soccerdata]$ ls
clubelo.py  espn.py             __init__.py       sofifa.py
_common.py  fbref.py            match_history.py  whoscored.py
_config.py  fivethirtyeight.py  __pycache__
[ftm3@peacock soccerdata]$ cd fbref.py
-bash: cd: fbref.py: Not a directory
[ftm3@peacock soccerdata]$ vim fbref.py
[ftm3@peacock soccerdata]$ vim fbref.py

        df = (
            pd.concat(dfs)
            .pipe(standardize_colnames)
            .rename(columns={"competition_name": "league"})
            .pipe(self._translate_league)
            .drop_duplicates(subset="league")
            .set_index("league")
            .sort_index()
        )
        df["first_season"] = df["first_season"].apply(season_code)
        df["last_season"] = df["last_season"].apply(season_code)

        leagues = self.leagues
        if "Big 5 European Leagues Combined" in self.leagues and split_up_big5:
            leagues = list(
                (set(self.leagues) - {"Big 5 European Leagues Combined"})
                | set(BIG_FIVE_DICT.values())
            )
        return df[df.index.isin(leagues)]

    def read_seasons(self, split_up_big5: bool = False) -> pd.DataFrame:
        """Retrieve the selected seasons for the selected leagues.

                                                              163,1         11%
