/int$/N
s/^\s*int\s\+main\s*(.*)/#include <stdlib.h>\n#ifndef ANGELIX_OUTPUT\n#define ANGELIX_OUTPUT(type, expr, id) expr\n#endif\nint main(int argc, char *argv[])/
/printf[^%0-9]\+$/d
s/\(^.*\)scanf.*,\s*&\(.*\)\s*);/\1\2 = atoi(argv[1]);/
s/printf.*%.*,\s*\(.\+\)\s*);/printf("%d\\n", ANGELIX_OUTPUT(int, \1, "stdout"));/
s/\r$//
s/\bdouble\b/int/g
s/\bfloat\b/int/g
