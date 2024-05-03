#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
  FILE *ifile;
  int sum = 0;
  ifile = fopen(argv[1], "r");

  if (ifile == NULL) {
    perror("Error opening file");
    return (-1);
  }
  // ASCII 48-57 = ints 0-9
  char buff[512];
  while (fgets(buff, sizeof(buff), ifile) != NULL) {
    printf("buff is: %s", buff);
    char n1 = '?';
    char n2 = '?';
    int i = 0;
    int j = strlen(buff) - 2;
    while (i <= j) {
      // printf("i: %d, buff[i]: %c\n", i, buff[i]);
      // printf("j: %d, buff[j]: %c\n", j, buff[j]);
      if (buff[i] < 58 && buff[i] > 47 && n1 == '?') {
        n1 = buff[i];
      } else if (n1 == '?') {
        i++;
      }

      if (buff[j] < 58 && buff[j] > 47 && n2 == '?') {
        n2 = buff[j];
      } else if (n2 == '?') {
        j--;
      }

      if (n1 != '?' && n2 != '?') {
        break;
      }
    }
    int num;
    char str[3] = "";
    if (n1 == '?') {
      str[0] = n2;
      str[1] = n2;
      str[3] = '\0';
    } else if (n2 == '?') {
      str[0] = n1;
      str[1] = n1;
      str[3] = '\0';
    } else {
      str[0] = n1;
      str[1] = n2;
      str[3] = '\0';
    }
    num = atoi(str);
    // printf("chars are: %c, %c\n", n1, n2);
    // printf("str is: %s\n", str);
    printf("num is: %d\n", num);
    sum += num;
  }
  printf("sum is %d\n", sum);
  fclose(ifile);
  return 0;
}