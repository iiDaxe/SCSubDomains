import requests
import re
import socket
import time
from bs4 import BeautifulSoup as BS
from colorama import Fore, init
from threading import Thread, Lock
import threading
import json
from datetime import datetime
import os
import platform
init()


def BurteForceSub(target):
    Subs = [
        'mail', 'mail2', 'www', 'ns2', 'ns1', 'blog', 'localhost', 'm', 'ftp',
        'mobile', 'ns3', 'smtp', 'search', 'api', 'dev', 'secure', 'webmail',
        'admin', 'img', 'news', 'sms', 'test', 'video', 'www2', 'media',
        'static', 'ads', 'mail2', 'beta', 'wap', 'dns2', 'support', 'pop',
        'my', 'origin-www', 'help', 'newsletter', 'ns4', 'upload', 'mail3',
        'blogs', 'download', 'dns1', 'www3', 'shop', 'forum', 'chat', 'www1',
        'image', 'app', 'tv', 'dns', 'services', 'music', 'images', 'game',
        'pay', 'new', 'host', 'www4', 'service', 'ad', 'monitor', 'web2',
        'wiki', 'mx1', 'sports', 'lists', 'm1', 'games', 'db', 'm2',
        'business', 'dns3', 'ws', 'counter', 'travel', 'photo', 'gateway',
        'members', 'c', 'g', 'mail4', 'crm', 'tools', 'backup', 'mail1',
        'apps', 't', 'email', 'img3', 'cms', 'demo', 'local', 'ns', 'i', 's',
        'community', 'connect', 'cdn', 'w12', 'iphone', 'cacti', 'w11',
        'www.mail', 'auth', 'rss', 'nagios', 'www.search', 'home', 'data',
        'img2', 'live', 'files', 'www5', 'login', 'stat', 'sso', 'member',
        'jira', 'w4', 'img5', 'ipad', 'web1', 'shopping', 'core', 'soccer',
        'jp', 'a', 'acceptatie', 'access', 'accounting', 'accounts', 'ad',
        'adm', 'admin', 'administrator', 'ads', 'adserver', 'affiliate',
        'affiliates', 'agenda', 'alpha', 'alumni', 'analytics', 'ann', 'api',
        'apollo', 'app', 'apps', 'ar', 'archive', 'art', 'assets', 'atlas',
        'auth', 'auto', 'autoconfig', 'autodiscover', 'av', 'ayuda', 'b',
        'b2b', 'backup', 'backups', 'banner', 'barracuda', 'bb', 'bbs', 'beta',
        'biblioteca', 'billing', 'blackboard', 'blog', 'blogs', 'board',
        'book', 'booking', 'bookings', 'broadcast-ip', 'bsd', 'bt', 'bug',
        'bugs', 'business', 'c', 'ca', 'cache', 'cacti', 'cal', 'calendar',
        'cam', 'careers', 'cart', 'cas', 'catalog', 'catalogo', 'catalogue',
        'cc', 'cctv', 'cdn', 'cdn1', 'cdn2', 'chat', 'chimera', 'chronos',
        'ci', 'cisco', 'citrix', 'classroom', 'client', 'clientes', 'clients',
        'cloud', 'cloudflare-resolve-to', 'club', 'cms', 'cn', 'co',
        'community', 'conference', 'config', 'connect', 'contact', 'contacts',
        'content', 'control', 'controller', 'controlp', 'controlpanel', 'corp',
        'corporate', 'correo', 'correoweb', 'cp', 'cpanel', 'crm', 'cs', 'css',
        'customers', 'cvs', 'd', 'da', 'data', 'database', 'db', 'db1', 'db2',
        'dbadmin', 'dbs', 'dc', 'de', 'default', 'demo', 'demo2', 'demon',
        'demostration', 'descargas', 'design', 'desktop', 'dev', 'dev01',
        'dev1', 'dev2', 'devel', 'developers', 'development', 'dialin',
        'diana', 'direct', 'directory', 'dl', 'dmz', 'dns', 'dns1', 'dns2',
        'dns3', 'dns4', 'doc', 'docs', 'domain', 'domain-controller',
        'domainadmin', 'domaincontrol', 'domaincontroller',
        'domaincontrolpanel', 'domainmanagement', 'domains', 'download',
        'downloads', 'drupal', 'e', 'eaccess', 'echo', 'ecommerce', 'edu',
        'ektron', 'elearning', 'email', 'en', 'eng', 'english',
        'enterpriseenrollment', 'enterpriseregistration', 'erp', 'es', 'event',
        'events', 'ex', 'example', 'examples', 'exchange', 'external',
        'extranet', 'f', 'facebook', 'faq', 'fax', 'fb', 'feedback', 'feeds',
        'file', 'files', 'fileserver', 'finance', 'firewall', 'folders',
        'forms', 'foro', 'foros', 'forum', 'forums', 'foto', 'fr', 'free',
        'freebsd', 'fs', 'ftp', 'ftp1', 'ftp2', 'ftpadmin', 'ftpd', 'fw', 'g',
        'galeria', 'gallery', 'game', 'games', 'gate', 'gateway', 'gilford',
        'gis', 'git', 'gmail', 'go', 'google', 'groups', 'groupwise', 'gu',
        'guest', 'guia', 'guide', 'gw', 'health', 'help', 'helpdesk', 'hera',
        'heracles', 'hercules', 'hermes', 'home', 'homer', 'host', 'host2',
        'hosting', 'hotspot', 'hr', 'hypernova', 'i', 'id', 'idp', 'im',
        'image', 'images', 'images1', 'images2', 'images3', 'images4',
        'images5', 'images6', 'images7', 'images8', 'imail', 'imap', 'imap3',
        'imap3d', 'imapd', 'imaps', 'img', 'img1', 'img2', 'img3', 'imgs',
        'imogen', 'in', 'incoming', 'info', 'inmuebles', 'internal', 'interno',
        'intra', 'intranet', 'io', 'ip', 'ip6', 'ipfixe', 'iphone', 'ipmi',
        'ipsec', 'ipv4', 'ipv6', 'irc', 'ircd', 'is', 'isa', 'it', 'j', 'ja',
        'jabber', 'jboss', 'jboss2', 'jira', 'job', 'jobs', 'jp', 'js',
        'jupiter', 'k', 'kb', 'kerberos', 'l', 'la', 'lab', 'laboratories',
        'laboratorio', 'laboratory', 'labs', 'ldap', 'legacy', 'lib',
        'library', 'link', 'links', 'linux', 'lisa', 'list', 'lists', 'live',
        'lms', 'local', 'localhost', 'log', 'loghost', 'login', 'logon',
        'logs', 'london', 'loopback', 'love', 'lp', 'lync', 'lyncdiscover',
        'm', 'm1', 'm2', 'magento', 'mail', 'mail01', 'mail1', 'mail2',
        'mail3', 'mail4', 'mail5', 'mailadmin', 'mailbackup', 'mailbox',
        'mailer', 'mailgate', 'mailhost', 'mailing', 'mailman', 'mailserver',
        'main', 'manage', 'manager', 'mantis', 'map', 'maps', 'market',
        'marketing', 'mars', 'master', 'math', 'mb', 'mc', 'mdm', 'media',
        'meet', 'member', 'members', 'mercury', 'meta', 'meta01', 'meta02',
        'meta03', 'meta1', 'meta2', 'meta3', 'miembros', 'mijn', 'minerva',
        'mirror', 'ml', 'mm', 'mob', 'mobil', 'mobile', 'monitor',
        'monitoring', 'moodle', 'movil', 'mrtg', 'ms', 'msoid', 'mssql',
        'munin', 'music', 'mx', 'mx-a', 'mx-b', 'mx0', 'mx01', 'mx02', 'mx03',
        'mx1', 'mx2', 'mx3', 'my', 'mysql', 'mysql2', 'n', 'nagios', 'nas',
        'nat', 'nelson', 'neon', 'net', 'netmail', 'netscaler', 'network',
        'network-ip', 'networks', 'new', 'newmail', 'news', 'newsgroups',
        'newsite', 'newsletter', 'nl', 'noc', 'novell', 'ns', 'ns0', 'ns01',
        'ns02', 'ns03', 'ns1', 'ns10', 'ns11', 'ns12', 'ns2', 'ns3', 'ns4',
        'ns5', 'ns6', 'ns7', 'ns8', 'nt', 'ntp', 'ntp1', 'o', 'oa', 'office',
        'office2', 'old', 'oldmail', 'oldsite', 'oldwww', 'on', 'online', 'op',
        'openbsd', 'operation', 'operations', 'ops', 'ora', 'oracle', 'origin',
        'orion', 'os', 'osx', 'ou', 'outgoing', 'outlook', 'owa', 'ox', 'p',
        'painel', 'panel', 'partner', 'partners', 'pay', 'payment', 'payments',
        'pbx', 'pcanywhere', 'pda', 'pegasus', 'pendrell', 'personal', 'pgsql',
        'phoenix', 'photo', 'photos', 'php', 'phpmyadmin', 'pm', 'pma',
        'poczta', 'pop', 'pop3', 'portal', 'portfolio', 'post', 'postgres',
        'postgresql', 'postman', 'postmaster', 'pp', 'ppp', 'pr', 'pre-prod',
        'pre-production', 'preprod', 'press', 'preview', 'private', 'pro',
        'prod', 'production', 'project', 'projects', 'promo', 'proxy',
        'prueba', 'pruebas', 'pt', 'pub', 'public', 'q', 'qa', 'r', 'ra',
        'radio', 'radius', 'ras', 'rdp', 'redirect', 'redmine', 'register',
        'relay', 'remote', 'remote2', 'repo', 'report', 'reports', 'repos',
        'research', 'resources', 'restricted', 'reviews', 'robinhood', 'root',
        'router', 'rss', 'rt', 'rtmp', 'ru', 's', 's1', 's2', 's3', 's4', 'sa',
        'sales', 'sample', 'samples', 'sandbox', 'sc', 'search', 'secure',
        'security', 'seo', 'server', 'server1', 'server2', 'service',
        'services', 'sftp', 'share', 'sharepoint', 'shell', 'shop', 'shopping',
        'signup', 'sip', 'site', 'siteadmin', 'sitebuilder', 'sites', 'skype',
        'sms', 'smtp', 'smtp1', 'smtp2', 'smtp3', 'snmp', 'social', 'software',
        'solaris', 'soporte', 'sp', 'spam', 'speedtest', 'sport', 'sports',
        'sql', 'sqlserver', 'squirrel', 'squirrelmail', 'ssh', 'ssl', 'sslvpn',
        'sso', 'st', 'staff', 'stage', 'staging', 'start', 'stat', 'static',
        'static1', 'static2', 'stats', 'status', 'storage', 'store', 'stream',
        'streaming', 'student', 'sun', 'support', 'survey', 'sv', 'svn', 't',
        'team', 'tech', 'telewerk', 'telework', 'temp', 'test', 'test1',
        'test2', 'test3', 'testing', 'testsite', 'testweb', 'tfs', 'tftp',
        'thumbs', 'ticket', 'tickets', 'time', 'tools', 'trac', 'track',
        'tracker', 'tracking', 'train', 'training', 'travel', 'ts', 'tunnel',
        'tutorials', 'tv', 'tw', 'u', 'uat', 'uk', 'unix', 'up', 'update',
        'upload', 'uploads', 'us', 'user', 'users', 'v', 'v2', 'vc', 'ventas',
        'video', 'videos', 'vip', 'virtual', 'vista', 'vle', 'vm', 'vms',
        'vmware', 'vnc', 'vod', 'voip', 'vpn', 'vpn1', 'vpn2', 'vpn3', 'vps',
        'vps1', 'vps2', 'w', 'w3', 'wap', 'wc', 'web', 'web0', 'web01',
        'web02', 'web03', 'web1', 'web2', 'web3', 'web4', 'web5', 'webadmin',
        'webcam', 'webconf', 'webct', 'webdb', 'webdisk', 'weblog', 'webmail',
        'webmail2', 'webmaster', 'webmin', 'webservices', 'webstats',
        'webstore', 'whm', 'wifi', 'wiki', 'win', 'win32', 'windows',
        'wordpress', 'work', 'wp', 'ws', 'wsus', 'ww', 'ww0', 'ww01', 'ww02',
        'ww03', 'ww1', 'ww2', 'ww3', 'www-test', 'www0', 'www01', 'www02',
        'www03', 'www1', 'www2', 'www3', 'www4', 'www5', 'www6', 'www7',
        'wwwm', 'wwwold', 'wwww', 'x', 'xml', 'zabbix', 'zeus', 'zimbra'
    ]

    for Sub in Subs:
        Url_HTTPS = f"https://{Sub}.{target}".strip()
        Url_HTTP = f"http://{Sub}.{target}".strip()
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
        }
        try:
            req_https = requests.get(url=Url_HTTPS, headers=headers)
            req_http = requests.get(url=Url_HTTP, headers=headers)

            if req_https.status_code == 200:
                BurteForc.append(Url_HTTPS)
                print("\t",
                      Fore.GREEN + "[" + Fore.WHITE + "+" + Fore.GREEN + "]",
                      Fore.YELLOW, " [  HTTPS : ]", Fore.CYAN, Url_HTTPS,
                      Fore.LIGHTYELLOW_EX, req_https.status_code)
            elif req_http.status_code == 200:
                BurteForc.append(Url_HTTP)
                print("\t",
                      Fore.GREEN + "[" + Fore.WHITE + "+" + Fore.GREEN + "]",
                      Fore.YELLOW, " [  HTTP : ]", Fore.CYAN, Url_HTTP,
                      Fore.LIGHTYELLOW_EX, req_http.status_code)
            else:
                pass
        except requests.exceptions.SSLError:
            pass
        except requests.exceptions.ConnectionError:
            pass


BurteForc = []


def SubDomain(url):
    crf = "https://crt.sh/?q="
    url = crf + url
    res = requests.get(url)
    findtd = r'<TD>(.*)</TD>'
    src = res.text
    findl = re.findall(findtd, src)
    findings = []
    for found in findl:
        testing = found.lower()
        if "<br>" in testing:
            for splited in testing.split("<br>"):
                findings.append(splited)
    with open('Subdomaint.txt', mode='w') as f:
        for found in findings:
            f.write(found + "\n")


def Scan_Protocol(SubDomain):
    try:

        URL_Susubbdomains_https = f"https://{SubDomain}".strip()
        URL_Susubbdomains_http = f"http://{SubDomain}".strip()
        request_https = requests.get(url=URL_Susubbdomains_https)
        request_http = requests.get(url=URL_Susubbdomains_http)
        if request_https.status_code == 200:
            status_code_is_200.append(URL_Susubbdomains_https)
            print("\t", Fore.GREEN + "[" + Fore.WHITE + "+" + Fore.GREEN + "]",
                  Fore.YELLOW, " [  HTTPS : ]", Fore.CYAN,
                  URL_Susubbdomains_https, Fore.LIGHTYELLOW_EX,
                  request_https.status_code)

        elif request_http.status_code == 200:
            status_code_is_200.append(URL_Susubbdomains_http)
            print("\t", Fore.GREEN + "[" + Fore.WHITE + "+" + Fore.GREEN + "]",
                  Fore.YELLOW, " [  HTTP : ]", Fore.CYAN,
                  URL_Susubbdomains_http, Fore.LIGHTYELLOW_EX,
                  request_http.status_code)
        else:
            pass
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.TooManyRedirects:
        pass
    except KeyboardInterrupt:
        exit()


def https_http(url):
    if url.startswith('http://'):
        url = url.replace('http://', '')
    elif url.startswith("https://"):
        url = url.replace('https://', '')
    else:
        pass
    return url


SubDomain_After_Split = []


def SplitSkar():
    global SubDomain_After_Split
    ListSubdomains = open('Subdomaint.txt', 'r').readlines()
    for Doamin in ListSubdomains:
        if "*." in Doamin:
            c = Doamin.replace("*.", "")
            SubDomain_After_Split.append(c)
        else:
            SubDomain_After_Split.append(Doamin)


def Link_Page(target):
    paths = open('Path_Forcing.txt', 'r').readlines()
    for path in paths:
        Url = f"{target}/{path}".strip()
        try:
            req = requests.get(url=Url)
            if req.status_code == 200:
                print("\t\t",
                      Fore.YELLOW,
                      "[",
                      Fore.WHITE,
                      "+",
                      Fore.YELLOW,
                      "]",
                      Fore.CYAN,
                      Url,
                      end='\n')
                link.append(Url)
            else:
                pass
        except requests.exceptions.ConnectionError:
            pass
        except UnicodeError:
            pass
        except requests.exceptions.InvalidURL:
            pass


BASEPORTS = [
    1, 3, 4, 6, 7, 9, 13, 17, 19, 26, 30, 32, 33, 37, 42, 43, 49, 53, 70, 79,
    85, 88, 90, 99, 100, 106, 109, 111, 113, 119, 125, 135, 139, 143, 144, 146,
    161, 163, 179, 199, 211, 212, 222, 254, 256, 259, 264, 280, 301, 306, 311,
    340, 366, 389, 406, 407, 416, 417, 425, 427, 443, 445, 458, 464, 465, 481,
    497, 500, 512, 515, 524, 541, 543, 545, 548, 554, 555, 563, 587, 593, 616,
    617, 625, 631, 636, 646, 648, 666, 668, 683, 687, 691, 700, 705, 711, 714,
    720, 722, 726, 749, 765, 777, 783, 787, 800, 801, 808, 843, 873, 880, 888,
    898, 900, 903, 911, 912, 981, 987, 990, 992, 993, 995, 999, 1002, 1007,
    1009, 1011, 1021, 1100, 1102, 1104, 1108, 1110, 1114, 1117, 1119, 1121,
    1124, 1126, 1130, 1132, 1137, 1138, 1141, 1145, 1147, 1149, 1151, 1152,
    1154, 1163, 1166, 1169, 1174, 1175, 1183, 1185, 1187, 1192, 1198, 1199,
    1201, 1213, 1216, 1218, 1233, 1234, 1236, 1244, 1247, 1248, 1259, 1271,
    1272, 1277, 1287, 1296, 1300, 1301, 1309, 1311, 1322, 1328, 1334, 1352,
    1417, 1433, 1434, 1443, 1455, 1461, 1494, 1500, 1501, 1503, 1521, 1524,
    1533, 1556, 1580, 1583, 1594, 1600, 1641, 1658, 1666, 1687, 1688, 1700,
    1717, 1721, 1723, 1755, 1761, 1782, 1783, 1801, 1805, 1812, 1839, 1840,
    1862, 1864, 1875, 1900, 1914, 1935, 1947, 1971, 1972, 1974, 1984, 1998,
    2010, 2013, 2020, 2022, 2030, 2033, 2035, 2038, 2040, 2043, 2045, 2049,
    2065, 2068, 2099, 2100, 2103, 2105, 2107, 2111, 2119, 2121, 2126, 2135,
    2144, 2160, 2161, 2170, 2179, 2190, 2191, 2196, 2200, 2222, 2251, 2260,
    2288, 2301, 2323, 2366, 2381, 2383, 2393, 2394, 2399, 2401, 2492, 2500,
    2522, 2525, 2557, 2601, 2602, 2604, 2605, 2607, 2608, 2638, 2701, 2702,
    2710, 2717, 2718, 2725, 2800, 2809, 2811, 2869, 2875, 2909, 2910, 2920,
    2967, 2968, 2998, 3000, 3001, 3003, 3005, 3007, 3011, 3013, 3017, 3030,
    3031, 3052, 3071, 3077, 3128, 3168, 3211, 3221, 3260, 3261, 3268, 3269,
    3283, 3300, 3301, 3306, 3322, 3325, 3333, 3351, 3367, 3369, 3372, 3389,
    3390, 3404, 3476, 3493, 3517, 3527, 3546, 3551, 3580, 3659, 3689, 3690,
    3703, 3737, 3766, 3784, 3800, 3801, 3809, 3814, 3826, 3828, 3851, 3869,
    3871, 3878, 3880, 3889, 3905, 3914, 3918, 3920, 3945, 3971, 3986, 3995,
    3998, 4000, 4006, 4045, 4111, 4125, 4126, 4129, 4224, 4242, 4279, 4321,
    4343, 4443, 4446, 4449, 4550, 4567, 4662, 4848, 4899, 4900, 4998, 5000,
    5004, 5009, 5030, 5033, 5050, 5051, 5054, 5060, 5061, 5080, 5087, 5100,
    5102, 5120, 5190, 5200, 5214, 5221, 5222, 5225, 5226, 5269, 5280, 5298,
    5357, 5405, 5414, 5431, 5432, 5440, 5500, 5510, 5544, 5550, 5555, 5560,
    5566, 5631, 5633, 5666, 5678, 5679, 5718, 5730, 5800, 5802, 5810, 5811,
    5815, 5822, 5825, 5850, 5859, 5862, 5877, 5900, 5904, 5906, 5907, 5910,
    5911, 5915, 5922, 5925, 5950, 5952, 5959, 5963, 5987, 5989, 5998, 6007,
    6009, 6025, 6059, 6100, 6101, 6106, 6112, 6123, 6129, 6156, 6346, 6389,
    6502, 6510, 6543, 6547, 6565, 6567, 6580, 6646, 6666, 6669, 6689, 6692,
    6699, 6779, 6788, 6789, 6792, 6839, 6881, 6901, 6969, 7000, 7002, 7004,
    7007, 7019, 7025, 7070, 7100, 7103, 7106, 7200, 7201, 7402, 7435, 7443,
    7496, 7512, 7625, 7627, 7676, 7741, 7777, 7778, 7800, 7911, 7920, 7921,
    7937, 7938, 7999, 8002, 8007, 8011, 8021, 8022, 8031, 8042, 8045, 8080,
    8090, 8093, 8099, 8100, 8180, 8181, 8192, 8194, 8200, 8222, 8254, 8290,
    8292, 8300, 8333, 8383, 8400, 8402, 8443, 8500, 8600, 8649, 8651, 8652,
    8654, 8701, 8800, 8873, 8888, 8899, 8994, 9000, 9003, 9009, 9011, 9040,
    9050, 9071, 9080, 9081, 9090, 9091, 9099, 9103, 9110, 9111, 9200, 9207,
    9220, 9290, 9415, 9418, 9485, 9500, 9502, 9503, 9535, 9575, 9593, 9595,
    9618, 9666, 9876, 9878, 9898, 9900, 9917, 9929, 9943, 9944, 9968, 9998,
    10004, 10009, 10010, 10012, 10024, 10025, 10082, 10180, 10215, 10243,
    10566, 10616, 10617, 10621, 10626, 10628, 10629, 10778, 11110, 11111,
    11967, 12000, 12174, 12265, 12345, 13456, 13722, 13782, 13783, 14000,
    14238, 14441, 14442, 15000, 15002, 15004, 15660, 15742, 16000, 16001,
    16012, 16016, 16018, 16080, 16113, 16992, 16993, 17877, 17988, 18040,
    18101, 18988, 19101, 19283, 19315, 19350, 19780, 19801, 19842, 20000,
    20005, 20031, 20221, 20222, 20828, 21571, 22939, 23502, 24444, 24800,
    25734, 25735, 26214, 27000, 27352, 27353, 27355, 27356, 27715, 28201,
    30000, 30718, 30951, 31038, 31337, 32768, 32785, 33354, 33899, 34571,
    34573, 35500, 38292, 40193, 40911, 41511, 42510, 44176, 44442, 44443,
    44501, 45100, 48080, 49152, 49161, 49163, 49165, 49167, 49175, 49176,
    49400, 49999, 50003, 50006, 50300, 50389, 50500, 50636, 50800, 51103,
    51493, 52673, 52822, 52848, 52869, 54045, 54328, 55055, 55056, 55555,
    55600, 56737, 56738, 57294, 57797, 58080, 60020, 60443, 61532, 61900,
    62078, 63331, 64623, 64680, 65000, 65129, 65389, 280, 4567, 7001, 8008,
    908021, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995,
    1723, 3306, 3389, 5900, 8080
]
PortScanned = int()
PortTimeout = int()
PortClosed = int()
PortThreadsLock = Lock()
OpenPorts = []
''' End '''


def PortScanner(target):
    try:
        init()
        threads = int(100)
        if threads > 999: threads = 999

        ports = len(BASEPORTS)
        toCheck_limit = threads
        toChecks = 0
        toChecks_list = []
        if ports > toCheck_limit:
            toCheck = []
            for i in range(ports):
                if i != 0 and i % toCheck_limit == 0:
                    toChecks += 1
                    toChecks_list.append(toCheck)
                    toCheck = []
                    if (ports - (toChecks * toCheck_limit)) < toCheck_limit:
                        break

                toCheck.append(BASEPORTS[i])
            left = (ports - (toChecks * toCheck_limit))

            toCheck = []
            for port in BASEPORTS[-left:]:
                toCheck.append(port)
            toChecks_list.append(toCheck)
            toChecks += 1

            threads_list = []
            print("\t", Fore.YELLOW, "Scanning ", Fore.WHITE, len(BASEPORTS),
                  Fore.YELLOW, "Port ...")

            for toCheck in toChecks_list:

                t = Thread(target=Port_Scanner, args=[target, toCheck])
                t.daemon = True
                threads_list.append(t)
                t.start()

            for t in threads_list:
                t.join()

            print("\t", Fore.GREEN, len(OpenPorts), Fore.YELLOW,
                  "Ports Are Open")
            print("\t", Fore.RED, PortTimeout, Fore.YELLOW, "Ports Timeouted")
            print("\t", Fore.RED, PortClosed, Fore.YELLOW, "Ports Closed")
            print()
    except socket.gaierror:
        pass


def Port_Scanner(target, ports):
    global PortScanned, OpenPorts, PortTimeout, PortClosed

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(3)

    for port in ports:
        result = None
        try:
            result = s.connect_ex((target, port))
        except Exception as ex:
            with PortThreadsLock:
                PortTimeout += 1
            continue
        except socket.gaierror:
            pass

        if result == 0:
            with PortThreadsLock:
                OpenPorts.append(port)
                print("\t", Fore.GREEN, port, Fore.YELLOW, "is open")
        else:
            with PortThreadsLock:
                PortClosed += 1
        with PortThreadsLock:
            PortScanned += 1


def Infotmation_Gethring(target):
    print(Fore.WHITE, "\n[+]",
          Fore.WHITE + "[ " + Fore.LIGHTGREEN_EX + " INFO " + Fore.WHITE + "]",
          Fore.LIGHTWHITE_EX, "Some ", Fore.LIGHTGREEN_EX, "Infotmation ",
          Fore.LIGHTWHITE_EX, "About Target  . ")
    target = "www." + target

    ip = socket.gethostbyname(target)

    url = f"https://ipapi.co/{ip}/json"
    res = requests.get(url=url)
    JsonSRC = json.loads(res.content)
    print(Fore.WHITE, "\t[+] ", Fore.CYAN, "IP : ", JsonSRC['ip'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.BLUE, "version :", JsonSRC['version'],
          Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.GREEN, "city : ", JsonSRC['city'])
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTMAGENTA_EX, "region : ",
          JsonSRC['region'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.WHITE, "region_code : ",
          JsonSRC['region_code'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTYELLOW_EX, "country : ",
          JsonSRC['country'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.MAGENTA, "country_name : ",
          JsonSRC['country_name'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTMAGENTA_EX, "country_code : ",
          JsonSRC['country_code'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTBLACK_EX, "country_code_iso3 : ",
          JsonSRC['country_code_iso3'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.CYAN, "country_capital : ",
          JsonSRC['country_capital'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.BLUE, "country_tld : ",
          JsonSRC['country_tld'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.GREEN, "continent_code : ",
          JsonSRC['continent_code'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.WHITE, "in_eu : ", JsonSRC['in_eu'],
          Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.MAGENTA, "postal : ", JsonSRC['postal'],
          Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTMAGENTA_EX, "latitude : ",
          JsonSRC['latitude'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTBLACK_EX, "longitude : ",
          JsonSRC['longitude'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTCYAN_EX, "timezone : ",
          JsonSRC['timezone'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.WHITE, "utc_offset : ",
          JsonSRC['utc_offset'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTGREEN_EX, "country_calling_code : ",
          JsonSRC['country_calling_code'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTCYAN_EX, "currency : ",
          JsonSRC['currency'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.BLUE, "currency_name : ",
          JsonSRC['currency_name'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.RED, "languages : ", JsonSRC['languages'],
          Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.YELLOW, "country_area : ",
          JsonSRC['country_area'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.CYAN, "country_population : ",
          JsonSRC['country_population'], Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTRED_EX, "asn : ", JsonSRC['asn'],
          Fore.RESET)
    print(Fore.WHITE, "\t[+] ", Fore.LIGHTGREEN_EX, "org : ", JsonSRC['org'],
          Fore.RESET)
    print("")


def system():
    my_system = platform.uname()
    if my_system.system == "Windows":
        return os.system('cls')
    else:
        return os.system('clear')


link = []
system()
print(
    Fore.LIGHTWHITE_EX, '''
                                                                      
                                                            ,,        
 .M"""bgd                                .M"""bgd          *MM        
,MI    "Y                               ,MI    "Y           MM        
`MMb.      ,p6"bo   ,6"Yb.  `7MMpMMMb.  `MMb.   `7MM  `7MM  MM,dMMb.  
  `YMMNq. 6M'  OO  8)   MM    MM    MM    `YMMNq. MM    MM  MM    `Mb 
.     `MM 8M        ,pm9MM    MM    MM  .     `MM MM    MM  MM     M8 
Mb     dM YM.    , 8M   MM    MM    MM  Mb     dM MM    MM  MM.   ,M9 
P"Ybmmd"   YMbmd'  `Moo9^Yo..JMML  JMML.P"Ybmmd"  `Mbod"YML.P^YbmdP'  

By : Daxe
Github : https://github.com/iiDaxe

Example : google.com , instagram.com

                                                                      
                                                                      ''')
print(Fore.YELLOW, "Start Scan at : ", Fore.WHITE, datetime.now())
url = input(" Enter Domain : ")
Infotmation_Gethring(url)
SubDomain(url)
SplitSkar()
remove_ref = tuple(dict.fromkeys(SubDomain_After_Split))
status_code_is_200 = []
print("",
      Fore.WHITE + "\n[ " + Fore.LIGHTGREEN_EX + " INFO " + Fore.WHITE + "]",
      Fore.LIGHTWHITE_EX, "Filter The SubDomains / Scan protocol  : - \n")
for U in remove_ref:
    Url = f"{U}".strip()
    Scan_Protocol(Url)
print("",
      Fore.WHITE + "\n[ " + Fore.LIGHTGREEN_EX + " INFO " + Fore.WHITE + "]",
      Fore.LIGHTWHITE_EX, "Brute Force  SubDomains ", Fore.LIGHTRED_EX,
      "[Anthor Technics]: - \n")
BurteForceSub(url)

print("",
      Fore.WHITE + "\n[ " + Fore.LIGHTGREEN_EX + " INFO " + Fore.WHITE + "]",
      Fore.LIGHTRED_EX, "Now Is Start Port Scan . ", Fore.LIGHTYELLOW_EX,
      "The Number of SubDomains : ", Fore.CYAN,
      len(status_code_is_200) + len(BurteForc))
for start_scan_onDomin in status_code_is_200:
    tar = https_http(start_scan_onDomin)
    URL = f"{tar}".strip()
    try:
        IP = IpForTarget = socket.gethostbyname(URL)
        print(Fore.LIGHTWHITE_EX, "\n\t[ ** ]Now start Scan in  : ",
              Fore.YELLOW, URL, Fore.LIGHTWHITE_EX, "IP :", Fore.YELLOW, IP,
              "\n")
        PortScanner(IP)
    except socket.gaierror:
        pass

print(Fore.WHITE + "\n[ " + Fore.LIGHTGREEN_EX + " INFO " + Fore.WHITE + "]",
      Fore.LIGHTRED_EX, "Now Is Start ", Fore.LIGHTCYAN_EX, "[ ", Fore.WHITE,
      "Burte Force Link Page", Fore.LIGHTCYAN_EX, " ] ", " :  ")

for start_scan_onDomin in status_code_is_200:
    URL = f"{start_scan_onDomin}".strip()
    print(Fore.LIGHTWHITE_EX, "\n\t[ ** ]Now start Burte Force Link in  : ",
          Fore.YELLOW, URL, Fore.LIGHTWHITE_EX, "\n")
    Link_Page(URL)
