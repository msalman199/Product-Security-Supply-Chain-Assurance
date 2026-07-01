#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void buffer_overflow_vuln(char* input) {
    char buffer[64];
    strcpy(buffer, input);  // Vulnerability: no bounds checking
    printf("Data: %s\n", buffer);
}

void format_string_vuln(char* input) {
    printf(input);  // Vulnerability: format string
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    
    // Vulnerability: command injection
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "echo %s", argv[1]);
    system(cmd);
    
    buffer_overflow_vuln(argv[1]);
    return 0;
}
