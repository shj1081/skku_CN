#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
int main() {
    int s = socket(2, 1, 0);
    struct sockaddr_in a = {.sin_family = 2, .sin_port = htons(12000)};
    inet_pton(2, "127.0.0.1", &a.sin_addr);
    connect(s, (void*)&a, sizeof a);
    char c[500], d[500];
    int r = recv(s, d, 499, 0);
    if (r) d[r] = 0, printf("%s", d);
    while (fgets(c, 500, stdin)) {
        if (!strncmp(c, "exit", 4)) break;
        send(s, c, strlen(c), 0);
        r = recv(s, d, 499, 0);
        if (r) d[r] = 0, printf("%s", d);
    }
    close(s);
}
