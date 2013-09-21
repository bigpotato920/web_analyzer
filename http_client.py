import socket


class HttpClient(object):

    def __init__(self):
        self.req_str = 'GET %s HTTP/1.1\r\nHOST: %s\r\nUser-Agent:Weg-Crawler\r\nConnection:Close\r\n\r\n'

    def do_get(self, server_name, file_path):
        """
        do http get request to specific host for specific file

        :param server_name: server name of the target host
        :param file_path: file wanna get
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((server_name, 80))
        self.client.send(self.req_str % (file_path, server_name))

    def get_status(self):
        """
        get http response status code

        """
        line = self.recv_line()
        return [int(s) for s in line.split() if s.isdigit()][0]

    def get_body(self):
        """
        get the content of the response
        :return: content string
        """
        nread = 0
        total_read = 0;
        tobe_read = self.get_body_len()

        content = ''
        partial = ''

        while True:
            line = self.recv_line()
            if self.is_blank(line):
                break

        while True:
            partial = self.client.recv(tobe_read)
            content += partial
            nread = len(partial)
            total_read += nread
            tobe_read -= nread

            if tobe_read <= 0:
                break

        return content

    def get_body_len(self):
        """
        get the length of the content body

        """
        while True:
            line = self.recv_line()
            if "Content-Length" in line:
                return [int(s) for s in line.split() if s.isdigit()][0]

    def close(self):
        """
        close the connection to the server

        """
        self.client.close()

    def is_blank(self, line):

        """
        judge whether the line is a blank line
        :param line: line of string
        :return: True on blank or False
        """
        if line == '\r\n':
            return True

        return False

    def recv_line(self):
        """

        receive a line from the low level socket
        :return: a line of string
        """
        rv = ''
        while True:
            c = self.client.recv(1)
            if c == '\n':
                rv += c
                break
            else:
                rv += c

        return rv



