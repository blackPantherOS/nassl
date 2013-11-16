import unittest
import socket
import tempfile
from nassl import SSLV23, SSL_FILETYPE_PEM, _nassl, SSL_VERIFY_NONE
from nassl.SslClient import SslClient


class SslClient_Tests_PrivateKey(unittest.TestCase):

    def setUp(self):
        self.sslClient = SslClient(sslVersion=SSLV23, sslVerify=SSL_VERIFY_NONE)

        testFile = tempfile.NamedTemporaryFile(delete=False)
        testFile.write("""-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,7D15D836EE9E1B77

fzTe/7+BUBBpW7rFqfffSMeNTNwjVT8uT6+aQFkv1sazU295heEWcvnqYPQ2suDS
dqud4pxLizkSRZpAIoKZV/E0z3iM1zsrGiyNXZ3mouRjSZdESEBnPEbtIdsyHLkL
9arhA/kvuMqXMjgun+tPD0+ETlaFf5GCKgfFQzbF2W4WpeEXii43ZLZ9UmObUUql
5Y65K/07+ga/dj3E+l1dLtA7VhVV5CK+8TTmVdqOr85pEZ/BC3U09vnwovDWJ+l0
sV7GhzsDFSpwxeArZy7wSMkSOTe71O1gvjOxWlupznFcZvirhRtI+5k1/btcn7hx
8b7dp36pTb/GfwaeUVsAvJBqwdSun3NOWX7zJxIDGU6LxA80eiV4z3SxAykS52gl
rlb2e+F6dV+tRuREfaDaeS1DSlDMp1mQjPSD2ix6nSypv19FHdh01OoCd0OFxM6D
xs5RQnUeu4J9g45Wdp6lmXM62EhUqYLKRbjXnZbFMlVMq81UwpMazwAruTEOCxl4
iQk3rNzfREONa9HeshiMlkeRAQpyB1qLZwhoTwTl6xKaMkt6nFEE6qX1KrrACHkH
CFJVbuWVJCyoRFv+0Gypi7zn1ZZGkE4inDHxqIzUa0sSmbShEWooTxCyGUSoosaY
u2ozh8ESQCy03JFR9DY6mo3YekbIcCEjgdmE35nK4lJQFbo3A8YlHunEdVK0tb8Z
Wxf7cJ6J55bG5/Kft65kJnXAHrV9LnM1tPiRkB8umZkj/ou5NpDKiuLjR+WBfwi0
tqXk90NdSqJtMMGgrtVM84TYFPXP58QCBnE9oAI7XYM1rusuVBOXZw==
-----END RSA PRIVATE KEY-----
""")
        testFile.close()
        self.testFile = testFile
        testFile2 = tempfile.NamedTemporaryFile(delete=False)
        testFile2.write("""-----BEGIN CERTIFICATE-----
MIIDCjCCAnOgAwIBAgIBAjANBgkqhkiG9w0BAQUFADCBgDELMAkGA1UEBhMCRlIx
DjAMBgNVBAgMBVBhcmlzMQ4wDAYDVQQHDAVQYXJpczEWMBQGA1UECgwNRGFzdGFy
ZGx5IEluYzEMMAoGA1UECwwDMTIzMQ8wDQYDVQQDDAZBbCBCYW4xGjAYBgkqhkiG
9w0BCQEWC2xvbEBsb2wuY29tMB4XDTEzMDEyNzAwMDM1OFoXDTE0MDEyNzAwMDM1
OFowgZcxCzAJBgNVBAYTAkZSMQwwCgYDVQQIDAMxMjMxDTALBgNVBAcMBFRlc3Qx
IjAgBgNVBAoMGUludHJvc3B5IFRlc3QgQ2xpZW50IENlcnQxCzAJBgNVBAsMAjEy
MRUwEwYDVQQDDAxBbGJhbiBEaXF1ZXQxIzAhBgkqhkiG9w0BCQEWFG5hYmxhLWMw
ZDNAZ21haWwuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlnvP1ltVO
8JDNT3AA99QqtiqCi/7BeEcFDm2al46mv7looz6CmB84osrusNVFsS5ICLbrCmeo
w5sxW7VVveGueBQyWynngl2PmmufA5Mhwq0ZY8CvwV+O7m0hEXxzwbyGa23ai16O
zIiaNlBAb0mC2vwJbsc3MTMovE6dHUgmzQIDAQABo3sweTAJBgNVHRMEAjAAMCwG
CWCGSAGG+EIBDQQfFh1PcGVuU1NMIEdlbmVyYXRlZCBDZXJ0aWZpY2F0ZTAdBgNV
HQ4EFgQUYR45okpFsqTYB1wlQQblLH9cRdgwHwYDVR0jBBgwFoAUP0X2HQlaca7D
NBzVbsjsdhzOqUQwDQYJKoZIhvcNAQEFBQADgYEAWEOxpRjvKvTurDXK/sEUw2KY
gmbbGP3tF+fQ/6JS1VdCdtLxxJAHHTW62ugVTlmJZtpsEGlg49BXAEMblLY/K7nm
dWN8oZL+754GaBlJ+wK6/Nz4YcuByJAnN8OeTY4Acxjhks8PrAbZgcf0FdpJaAlk
Pd2eQ9+DkopOz3UGU7c=
-----END CERTIFICATE-----
""")
        testFile2.close()
        self.sslClient.use_certificate_file(testFile2.name, SSL_FILETYPE_PEM)


    def test_use_privateKey_file(self):
        self.assertIsNone(self.sslClient.use_privateKey_file(self.testFile.name, SSL_FILETYPE_PEM, 'testPW'))

    def test_use_privateKey_file_bad(self):
        self.assertRaisesRegexp(_nassl.OpenSSLError, 'bad decrypt', self.sslClient.use_privateKey_file, self.testFile.name, SSL_FILETYPE_PEM, 'badPW')


class SslClient_Tests_Handshake(unittest.TestCase):

    def setUp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect(("www.google.com", 443))

        sslClient = SslClient(sslVersion=SSLV23, sock=sock, sslVerify=SSL_VERIFY_NONE)
        self.sslClient = sslClient


    def test_do_handshake(self):
        self.assertTrue(self.sslClient.do_handshake())


class SslClient_Tests_Online(unittest.TestCase):

    def setUp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect(("www.google.com", 443))

        sslClient = SslClient(sslVersion=SSLV23, sock=sock, sslVerify=SSL_VERIFY_NONE)
        sslClient.do_handshake()
        self.sslClient = sslClient


    def test_write(self):
        self.assertGreater(self.sslClient.write('GET / HTTP/1.0\r\n\r\n'), 1)


    def test_read(self):
        self.sslClient.write('GET / HTTP/1.0\r\n\r\n')
        self.assertRegexpMatches(self.sslClient.read(1024), 'google')


    def test_get_peer_certificate(self):
        self.assertIsNotNone(self.sslClient.get_peer_certificate())


    def test_shutdown(self):
        self.assertIsNone(self.sslClient.shutdown())


    def test_shutdown(self):
        self.assertIsNone(self.sslClient.shutdown())


    def test_get_certificate_chain_verify_result(self):
        self.assertEqual(20, self.sslClient.get_certificate_chain_verify_result()[0])



def main():
    unittest.main()

if __name__ == '__main__':
    main()