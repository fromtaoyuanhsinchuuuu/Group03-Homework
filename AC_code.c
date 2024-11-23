#include <stdio.h>

#define MAX_BLOCKS 25
#define MAX_BLOCK_NAME 20
#define MAX_LINE_LENGTH 30

int parse_block_file(const char *filename, unsigned int *previous_hash) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Error opening file: %s\n", filename);
        return -1;
    }

    char line[MAX_LINE_LENGTH];
    int line_number = 0;
    unsigned int h = 0;

    while (fgets(line, MAX_LINE_LENGTH, file)) {
        line_number++;
        if (line[0] == 'P') {
            sscanf(line, "P: %u", previous_hash);
        } else if (line[0] >= '1' && line[0] <= '9') {
            int value;
            sscanf(line, "%*d: %d", &value);
            if ((line_number - 1) % 25 == 0)
                h = (((h ^ value) << 1) & 0x3FFFFFFF); // 左移 1 位後取模 2^30
            else
                h = (h ^ value) & 0x3FFFFFFF; // 僅取低 30 位
        } else if (line[0] == 'N') {
            int nonce;
            sscanf(line, "N: %d", &nonce);
            if ((line_number - 1) % 25 == 0)
                h = (((h ^ nonce) << 1) & 0x3FFFFFFF); // 左移 1 位後取模 2^30
            else
                h = (h ^ nonce) & 0x3FFFFFFF; // 僅取低 30 位
        }
    }

    fclose(file);
    return h;
}

int main() {
    int n;
    char filenames[MAX_BLOCKS][MAX_BLOCK_NAME];

    // 讀取輸入
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", filenames[i]);
    }

    unsigned int previous_hash = 0;
    for (int i = 0; i < n; i++) {
        unsigned int expected_previous_hash = previous_hash;
        unsigned int current_hash;

        current_hash = parse_block_file(filenames[i], &previous_hash);
        if (current_hash == -1) {
            return 1; // 文件讀取失敗
        }

        if (expected_previous_hash != previous_hash) {
            printf("%d\n", i);
            return 0;
        }

        previous_hash = current_hash;
    }

    printf("-1\n");
    return 0;
}
